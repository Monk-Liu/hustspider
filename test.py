from db import DB
from hustparser import HustParser 
from spider import HustSpider

def main():
    S = HustSpider()
    D = DB()
    res = S.get_info('U201410001')
    res = HustParser(res)
    D.insert_info(res)
    print("end")

if __name__ == "__main__":
    main()
