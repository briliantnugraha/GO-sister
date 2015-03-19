import cv2
import pickle
import xmlrpclib
import platform

def server_version():
	return platform.system() + '\n'+ platform.release()+ '\n'+ platform.version()

def img_conversion(fileobj):
	print "data masuk ke fungsi"
	temp = pickle.loads(fileobj)
	gray_img = cv2.cvtColor(temp[0], cv2.COLOR_BGR2GRAY)

	kirim = []
	kirim.append(gray_img)
	kirim = pickle.dumps(kirim)
	print "data berhasil dikirim"
	return kirim

print "Masukkan port address server: ",
port = raw_input()

from SimpleXMLRPCServer import SimpleXMLRPCServer
serv = SimpleXMLRPCServer(("localhost",int(port) ) )

serv.register_function(img_conversion,"img_conversion")
serv.register_function(server_version,"server_version")
serv.serve_forever()