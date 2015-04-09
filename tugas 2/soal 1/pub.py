#
# Weather update server
# Binds PUB socket to tcp://*:5556
# Publishes random weather updates
#

import zmq
from random import randrange
import requests
import sys
port = "15556"

if len(sys.argv) > 1:
        port = sys.argv[1]
        int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

while True:
	zipcode = "USD"
	print "Masukkan IDR: ",
	inp = raw_input()
        response = requests.get(
                'http://jsonrates.com/get/?' +
                'apiKey=jr-eda1b668d65900e98fc11dabecbcd2e2' +
                '&from=IDR' +
                '&to=USD'
        )  
        response2 = requests.get(
                'http://jsonrates.com/convert/?' +
                'apiKey=jr-eda1b668d65900e98fc11dabecbcd2e2' +
                '&from=IDR' +
                '&to=USD' +
                '&amount=' + inp
        )

        json = response.json()
        ratestr = str(json['rate'])
        json2 = response2.json()
        amountstr = str(json2['amount'])
	socket.send_string("%s %s %s %s %s" % (zipcode, port, ratestr, inp, amountstr))

