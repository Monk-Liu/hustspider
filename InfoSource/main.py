from db import DB
from hustparser import HustParser
from spider import HustSpider

class Main(object):

    def __init__(self):
        self.mainspider = HustSpider()
        self.db = DB()

    def do(self,id):
        res = self.mainspider.get_info(id)
        if not res:
            self.mainspider = HustSpider()
            return
        res = HustParser(res)
        if res.name:
            self.db.insert_info(res)
        else:
            pass
        return 

    def run(self):

        for i in range(1,8000):
            i = str(i)
            while len(i)<4:
                i = '0'+i
            id = 'U20121'+i
            try:
                self.do(id)
            except:
                print(("#error:%s"%id))
                continue


if __name__ == "__main__":
    p = Main()
    p.run()
