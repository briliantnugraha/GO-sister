#
# Weather update client
# Connects SUB socket to tcp://localhost:5556
# Collects weather updates and finds avg temp in zipcode
#

import sys
import zmq

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
port = "15556"
if len(sys.argv) > 1:
	for iter in range(1,len(sys.argv)):
		port = sys.argv[iter]
		int(port)

		print("Connect to port %s" %port)
		socket.connect("tcp://localhost:%s" % port)
else: socket.connect("tcp://localhost:%s" % port)

while True:
	# Subscribe to zipcode, default is NYC, 100001
	zip_filter = "USD"

	# Python 2 - ascii bytes to unicode
	socket.setsockopt(zmq.SUBSCRIBE, zip_filter)

	string = socket.recv_string()
	zipcode, portpub, rate, idr, usd = string.split()

	print "\nPesan dari publisher dengan port: %s" % portpub 
	print "Nilai rate IDR to USD = %s" %rate
	print "Nilai IDR yang diinput publisher = %s" % idr
	print "Nilai USD = %s\n\n" % usd

