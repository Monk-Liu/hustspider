from func import Func
from queue import Queue
import threading
from db import DB
import time
import random


q = Queue(50)
threadlist = []

class SpiderOperator(threading.Thread):

    def __init__(self):
        super(SpiderOperator,self).__init__()
        self.operator = Func()

    def run(self):
        global q
        while True:
            sid,password = q.get()
            self.operator.check(sid,password)
            q.task_done()


class Productor(threading.Thread):
    
    def __init__(self):
        self.db = DB()
        super(Productor,self).__init__()

    def run(self):
        global q
        infos = self.db.get_info()
        for info in infos:
            if q.full():
                time.sleep(random.random())
                continue
            q.put(info)
        

def main():
    starttime = time.time()
    
    p = Productor()
    p.start()
    
    for i in range(20):
        consumer = SpiderOperator()
        consumer.setDaemon(True)
        threadlist.append(consumer)
        consumer.start()

    #这里用join等待子进程的话，会由于子进程一直在 queue.get()而导致无法推出
    #for i in threadlist:
    #    i.join()

    p.join()
    time.sleep(4)
    during = time.time() - starttime
    
    print('end:total time:%s' %during)

if __name__ == '__main__':
    main()

