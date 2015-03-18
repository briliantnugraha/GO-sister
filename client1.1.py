import rpyc
import os
import cv2
import threading
import pickle
import time

def serv(idServer):
	
	path=0
	bit_size = 4096
	fileobj= ''
	proxy = rpyc.connect('localhost', 15000, config={'allow_public_attrs': True})
	img = 'a.jpg'
	img2 = ['a.jpg','b.jpg', 'c.jpg', 'd.jpg']
	cek = 0
	c_server1 = 0
	c_server2 = 1

	while True:
		global path
		global c_server1
		global c_server2

		if idServer==0 and c_server1!=-1:
			path = c_server1
		elif idServer==1 and c_server2!=-1:
			path = c_server2
		else:
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

#serv(0)
t1 = threading.Thread(target = serv, args={0,})
t1.start()
t2 = threading.Thread(target = serv, args={1,})
t2.start()