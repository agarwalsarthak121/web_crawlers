#! /usr/bin/python3

from win10toast import ToastNotifier
import random
from time import sleep

fw = open('.quotes.txt','r')
vocab = fw.read()
vocab = vocab.split('\n')

def sendmessage(title, message):
    #pynotify.init("Test")
    #notice = pynotify.Notification(title, message)
    #notice.show()
    toaster = ToastNotifier()
    toaster.show_toast(title,
                   message,
                   icon_path=None,
                   duration=20)
    return
    
while True:
    i = random.randint(0,2002)
    if i % 2 == 0 and len(vocab[i]) < 170:
        sendmessage(vocab[i+1],vocab[i])
        sleep(300)
    else:
        continue
    
