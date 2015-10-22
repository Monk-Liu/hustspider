#from func import Func
#from db import DB
import threading 
import random
import time
'''使用condition的bug是，当有多个consumer在wait状态时，productor的notify会使所有
comsumer运行，于是有了竞争状态'''


queuelist = []
MAX_NUM = 10
condition = threading.Condition()

class Productor(threading.Thread):

    def __init__(self):
        super(Productor,self).__init__()

    def run(self):
        nums = range(5)
        global queuelist
        while True:
            condition.acquire()
            if len(queuelist) == MAX_NUM:
                print('queue is ful, producer is waiting')
                condition.wait()
                print("Space in queue, consumr notiried the producer")
            num = random.choice(nums)
            queuelist.append(num)
            print('produced %s'%num)
            condition.notify()
            condition.release()
            time.sleep(random.random())


class Consumer(threading.Thread):

    def __init__(self):
        super(Consumer,self).__init__()

    def run(self):
        global queuelist
        while True:
            condition.acquire()
            if not queuelist:
                print("Nothing in queue, consumer is wartting")
                condition.wait()
                print('Producer add something to queue and notified the consumer')
            num = queuelist.pop(0)
            print("Consumed: %s"%num)
            condition.notify()
            condition.release()
            time.sleep(random.random())


if __name__ == '__main__':
    a = Productor()
    a.start()
    b = Productor()
    b.start()
    c = Productor()
    c.start()

    d = Consumer()
    d.start()
    e = Consumer()
    e.start()
    f = Consumer()
    f.start()


