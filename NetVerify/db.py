from config import DB_USER,DB_PASSWORD,DB_DATABASE,SELECT,INSERT
import mysql.connector

class DB(object):

    def __init__(self):
        self.conn1 = mysql.connector.connect(user=DB_USER,
                    password=DB_PASSWORD,database=DB_DATABASE)

        self.conn2 = mysql.connector.connect(user=DB_USER,
                    password=DB_PASSWORD,database=DB_DATABASE)

        self.select_sql = SELECT
        self.insert_sql = INSERT
    
    def get_info(self):
        cur = self.conn1.cursor()
        cur.execute(self.select_sql)
        return cur
    
    def insert_info(self,sid,idcard):
        cur = self.conn2.cursor()
        cur.execute(self.insert_sql,(sid,idcard))

        self.conn2.commit()
        cur.close()
