import time
import zmq
import xmlrpclib
import os
import cv2
import threading
import pickle
import datetime
import numpy
import random

context = zmq.Context()

#send to worker
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:4000")

#send to sink
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5000")

print("Tekan Enter jika workers sudah siap ")
_ = raw_input()
print("Working")

word = "hai"
wr = []
wr.append(word)
wr = pickle.dumps(wr)
sink.send_pyobj(wr)

random.seed()

pathImg = "/home/peni/sister/dataset/"
dirs = os.listdir(pathImg)
#print dirs

counter = 1
total_msec = 0
nData = "50"

for file in dirs:
    print counter
    print file
    img = cv2.imread(pathImg+file)
    msg = []
    msg.append(img)
    msg = pickle.dumps(msg)
    work_message= {'filename' : file, 'img' : msg, 'jmlh' : nData} #dictionary
    sender.send_pyobj(work_message)
    counter +=1
    workload = random.randint(1,100)
    total_msec += workload

time.sleep(2)
print("Total expected cost: %s msec" % total_msec)
