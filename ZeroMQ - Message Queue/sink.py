import sys
import time
import zmq
import pickle
import numpy
import cv2
import os
import xmlrpclib

context = zmq.Context()

#menerima dari worker
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5000")

#wait for start of batch
s = receiver.recv_pyobj()

#start clock now
timeStart = time.time()
count = 1

while True:
    print count
    work = receiver.recv_pyobj()
    data = work['filename']
    data2 = work['img']
    nData = work['jmlh']
    temp = pickle.loads(data2)
    cv2.imwrite(data, temp[0])
    
    print data
    if count == int(nData):
        break;
    count += 1
timeEnd = time.time()
print("Total elapsed time: %d msec" % ((timeEnd-timeStart)*1000))
