import rpyc
import os

bit_size = 4096
fileobj= ''
proxy = rpyc.connect('localhost', 15100, config={'allow_public_attrs': True})
img = 'a.jpg'
cek = 0

if os.path.exists(img):
	r = open(img,'rb')
	title = proxy.root.title(img)
	print title
	while True:
		cek =  len(fileobj)
		fileobj += r.read(bit_size)
		if len(fileobj) == cek: break
	linecount=proxy.root.img_conversion(fileobj)
	print linecount
else: print "tidak jalan"


