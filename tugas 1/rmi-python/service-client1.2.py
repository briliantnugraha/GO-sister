import rpyc
import os
import cv2
import threading
import pickle
import datetime

c_server1 = 0
c_server2 = 1

server= ["",""]
port= ["",""]
print "Masukkan ipv4 server 1: ",
server[0] = raw_input()
print "Masukkan port server 1: ",
port[0] = raw_input()

print "Masukkan ipv4 server 2: ",
server[1] = raw_input()
print "Masukkan port server 2: ",
port[1] = raw_input()

def serv(idServer):
	bit_size = 4096
	fileobj= ''
	global c_server1
	global c_server2
	
	if idServer==0 and  c_server1!=-1:
		path = c_server1
		proxy = rpyc.connect(server[0], int(port[0]), config={'allow_public_attrs': True})
		print "Start time server 1: %s" % datetime.datetime.now()
		vers=proxy.root.server_version()
		print "Server 1: %s" % vers + "\n\n"

	elif idServer==1 and  c_server2!=-1:
		path = c_server2
		proxy = rpyc.connect(server[1], int(port[1]), config={'allow_public_attrs': True})
		print "Start time server 2: %s" % datetime.datetime.now()
		vers=proxy.root.server_version()
		print "Server 2: %s" % vers 

	img2 = ['a.jpg','b.jpg', 'c.jpg', 'd.jpg']
	cek = 0
	
	while True:

		if idServer==0 and c_server1!=-1:
			path = c_server1
		elif idServer==1 and c_server2!=-1:
			path = c_server2
		else:
			end = datetime.datetime.now()
			print "end server",end
			return

		if os.path.exists(img2[path]):
			r = cv2.imread(img2[path])
		
			msg = []
			msg.append(r)
			msg = pickle.dumps(msg)

			linecount=proxy.root.img_conversion(msg)

			output = pickle.loads(linecount)
			cv2.imwrite("gray_"+img2[path],output[0])

			if idServer==0:
				if(c_server1+2<len(img2)):
					c_server1+=2
				else:
					c_server1=-1
			else:
				if(c_server2+2<len(img2)):
					c_server2+=2
				else:
					c_server2=-1

		else: print "tidak jalan"

t1 = threading.Thread(target = serv, args={0,})
t1.start()
t2 = threading.Thread(target = serv, args={1,})
t2.start()