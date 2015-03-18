import xmlrpclib
import os
import cv2
import threading
import pickle
import time
c_server1 = 0
c_server2 = 1

server= ["",""]
print "Masukkan ipv4 dan port server 1 (ex: 10.0.0.0:8080): ",
server[0] = raw_input()
print "Masukkan ipv4 dan port server 2 (ex: 10.0.0.0:8080): ",
server[1] = raw_input()

def serv(idServer):
	bit_size = 4096
	fileobj= ''
	

	img2 = ['a.jpg','b.jpg', 'c.jpg', 'd.jpg']
	cek = 0

	while True:
		global c_server1
		global c_server2
		
		if idServer==0 and  c_server1!=-1:
			path = c_server1
			proxy = xmlrpclib.ServerProxy('http://'+server[0])
		elif idServer==1 and  c_server2!=-1:
			path = c_server2
			proxy = xmlrpclib.ServerProxy('http://'+server[1])
		else:
			return
		print path
		if os.path.exists(img2[path]):
			r = cv2.imread(img2[path])
			msg = []
			msg.append(r)
			msg = pickle.dumps(msg)

			linecount=proxy.img_conversion(msg)

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

		else: print "Data tidak ada"

t1 = threading.Thread(target = serv, args={0,})
t1.start()
t2 = threading.Thread(target = serv, args={1,})
t2.start()
