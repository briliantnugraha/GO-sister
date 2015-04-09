import rpyc
import os
import cv2
tit = ''
temp = ''
f=''
class MyService(rpyc.Service):
	def exposed_title(self,title):
		global tit
		global temp
		global f
		tit = title
		temp = "server/" + title
		f= open(temp,"wb")
		return "title yang diinput: "+ temp

	def exposed_img_conversion(self,fileobj):
		print "data masuk ke fungsi"
		if fileobj:
			f.write(fileobj)
			img = cv2.imread(temp)
			gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			cv2.imwrite("server/grey_"+tit,gray_img)
			f.close()
			cv2.destroyAllWindows()
			return 'data berhasil dibuat'

from rpyc.utils.server import ThreadedServer
t = ThreadedServer(MyService, port=15100)
t.start()
