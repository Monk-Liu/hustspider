import urllib.request,urllib.parse,http.cookiejar
from config import LOGURL,INFOURL,HEADERS

class VerifySpider(object):

    def __init__(self):
        self._opener = urllib.request.build_opener()
        urllib.request.install_opener(self._opener)
        self.logurl = LOGURL
        self.infourl = INFOURL
        self._headers = HEADERS
        self.add_header()
        self.add_cookie()
    
    def add_header(self):
        T = []
        for key,value in self._headers.items():
            T.append((key,value))
        self._opener.addheaders = T

    def add_cookie(self):
        cookie = http.cookiejar.CookieJar()
        cookieproc = urllib.request.HTTPCookieProcessor(cookie)
        self._opener.add_handler(cookieproc)

    def req_login(self,name,password):
        data = urllib.parse.urlencode({'name':name,'password':password})
        data = data.encode()
        res = urllib.request.urlopen(self.logurl,data)
        html = res.read().decode('GBK','ignore')
        return html
        
    def req_info(self):
        res = urllib.request.urlopen(self.infourl)
        html = res.read().decode('GBK','ignore')
        return html

    #def do(self,name,password):
    #   self.req_login(name,password)


if __name__ == '__main__':
    obj = VerifySpider()
    obj.req_login('U201414680','lqf33211')
    html = obj.req_info()
    print(html)
