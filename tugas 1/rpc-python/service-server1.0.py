import os
import cv2
import pickle
import xmlrpclib

def img_conversion(fileobj):
	print "data masuk ke fungsi"
	temp = pickle.loads(fileobj)
	gray_img = cv2.cvtColor(temp[0], cv2.COLOR_BGR2GRAY)

	kirim = []
	kirim.append(gray_img)
	kirim = pickle.dumps(kirim)
	print "data berhasil dikirim"
	return kirim

from SimpleXMLRPCServer import SimpleXMLRPCServer
serv = SimpleXMLRPCServer(("localhost",10000))

serv.register_function(img_conversion,"img_conversion")
serv.serve_forever()