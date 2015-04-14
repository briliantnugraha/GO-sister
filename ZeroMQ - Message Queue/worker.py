import sys
import time
import zmq
import random
import cv2
import pickle
import numpy
import base64

context = zmq.Context()

#receive from sender
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:4000")

#send to sink
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5000")

while True:
    work  = receiver.recv_pyobj()
    data  = work['filename']
    data2 = work['img']
    nData = work['jmlh']

    print data
    temp = pickle.loads(data2)
    gray_img = cv2.cvtColor(temp[0],cv2.COLOR_BGR2GRAY)

    msg = []
    msg.append(gray_img)
    msg = pickle.dumps(msg)
    work_message = { 'filename' : data, 'img' : msg , 'jmlh' : nData}
    sender.send_pyobj(work_message)

