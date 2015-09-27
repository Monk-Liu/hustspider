from bs4 import BeautifulSoup

class HustParser(object):

    def __init__(self,html):
        self.soup = BeautifulSoup(html,'lxml')
        self._parser()
        self.soup = None
        print(self.name,self.sid,self.sex)

    def get_input_by_name(self,name):
        input = self.soup.find('input',attrs={'name':name})
        if input:
            return input['value']
        else:
            return None

    def _parser(self):
        self.sid = self.get_input_by_name('STD_INFO_XH')
        self.name = self.get_input_by_name("STD_INFO_XM")
        self.sex = self.get_input_by_name("STD_INFO_XB")
        self.idcard = self.get_input_by_name("STD_INFO_SFZH")
        self._class = self.get_input_by_name("STD_INFO_BJMC")
        self.dormitory = self.get_input_by_name("STD_INFO_XNDZ")
        self.mail = self.get_input_by_name("STD_INFO_EMAIL")
        self.income = self.get_input_by_name("STD_INFO_QNSRZS")
        self.address = self.get_input_by_name("STD_INFO_HKSZDZ")
        self.phone = self.get_input_by_name("STD_INFO_SJ")
        if not self.address:
            self.address = self.get_input_by_name("STD_INFO_HKD")
        self.income = int(self.income)
