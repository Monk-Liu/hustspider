#from func import Func
#from db import DB
import threading 
import random
import time
'''使用condition的bug是，当有多个consumer在wait状态时，productor的notify会使所有
comsumer运行，于是有了竞争状态'''
from queue import Queue

queuelist = Queue(5)
condition = threading.Condition()

class Productor(threading.Thread):

    def __init__(self):
        super(Productor,self).__init__()

    def run(self):
        nums = range(5)
        global queuelist
        while True:
            if queuelist.full():
                print('queue is ful, producer is waiting')
            num = random.choice(nums)
            queuelist.put(num)
            print('produced %s'%num)
            #queuelist.task_done()
            time.sleep(random.random())


class Consumer(threading.Thread):

    def __init__(self):
        super(Consumer,self).__init__()

    def run(self):
        global queuelist
        while True:
            if queuelist.empty():
                print("Nothing in queue, consumer is wartting")
            num = queuelist.get()
            print("Consumed: %s"%num)
            queuelist.task_done()
            time.sleep(random.random())


if __name__ == '__main__':
    for i in range(4):
        a = Productor()
        a.start()

    for i in range(2):
        a = Consumer()
        a.start()


