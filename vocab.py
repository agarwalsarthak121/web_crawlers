#! /usr/bin/python

import pynotify
import random
from time import sleep

fw = open('.vocab.txt','r')
vocab = fw.read()
vocab = vocab.split('\n')

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return
    
while True:
    i = random.randint(0,len(vocab)-1)
    if i % 2 == 0:
        sendmessage(vocab[i],vocab[i+1])
        sleep(300)
    else:
        continue
