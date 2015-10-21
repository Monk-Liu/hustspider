from bs4 import BeautifulSoup

class InfoParser(object):

    def __init__(self):
        pass

    def check_online(self,html):
        soup = BeautifulSoup(html,'lxml')
        info_list1 = soup.find_all('span',attrs={'class':'big'})
        if info_list1 and len(info_list1) >1:
            tmp_str = info_list1[1].text
            self.online_count = int(tmp_str.strip())
        else:
            self.online_count = 10
        info_list2 = soup.find('input',attrs={'id':'packageName'})
        if info_list2:
            self.package = info_list2['value']

    def check_login(self,html):
        index = html.find('self.location=\'../../../module/webcontent/web/index_self_hk.jsf?')
        if index !=-1:
            return True
        else:
            return False



