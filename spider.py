import urllib.request,urllib.parse,http.cookiejar
from config import USERNAME,PASSWORD,LOGINURL,INFOURL

HEADERS = {'Accept': 'ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36', 'Accept_language': 'en-US,en;q=0.8'}

class HustSpider(object):
    
    def __init__(self):
        self._opener = urllib.request.build_opener()
        urllib.request.install_opener(self._opener)
        self.loginurl = LOGINURL
        self.url = INFOURL 
        self._headers = HEADERS
        self.add_header()
        #其实没有必要用add_cookie 因为有用的cookie都在header里的session里了
        self.add_cookie()
        self.get_permission()

    def add_header(self):
        T = []
        for key,value in self._headers.items():
            T.append((key,value))
        self._opener.addheaders = T

    def add_cookie(self):
        cookie = http.cookiejar.CookieJar()
        cookieproc = urllib.request.HTTPCookieProcessor(cookie)
        self._opener.add_handler(cookieproc)

    def get_permission(self):
        #获取session 否则不能登录
        res = urllib.request.urlopen(self.loginurl)
        if res.code != 200:
            print("res.code == %s" %res.code)
        # 模拟表单提交
        data = urllib.parse.urlencode({'user_name':USERNAME,
                                       "pass_word":PASSWORD
                                      })
        data = data.encode()
        
        req = urllib.request.Request(self.loginurl,data)
        res = urllib.request.urlopen(req)
        if res.code == 200:
            print('init OK!')
        else:
            print('sorry,res.code == %s'%res.code)

    def get(self,url):
        res = urllib.request.urlopen(url)
        html = res.read().decode("UTF-8")
        return html

    def get_info(self,id):
        url = self.url%id
        return self.get(url)


if __name__ == "__main__":
    p = HustSpider()
