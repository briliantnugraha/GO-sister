import rpyc
import os
import cv2
import pickle
import platform

class MyService(rpyc.Service):
	def exposed_server_version(self):
		cek = platform.system() + '\n'+ platform.release()+ '\n'+ platform.version()
		print cek
		return cek

	def exposed_img_conversion(self,fileobj):
		print "data masuk ke fungsi"
		temp = pickle.loads(fileobj)
		gray_img = cv2.cvtColor(temp[0], cv2.COLOR_BGR2GRAY)
		kirim = []
		kirim.append(gray_img)
		kirim = pickle.dumps(kirim)
		return kirim

from rpyc.utils.server import ThreadedServer
t = ThreadedServer(MyService, port=15000)
t.start()
