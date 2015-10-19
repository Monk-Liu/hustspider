from config import DB_USER,DB_PASSWORD,DB_DATABASE
import mysql.connector

class DB(object):

    def __init__(self):
        self.conn = mysql.connector.connect(user=DB_USER,password=DB_PASSWORD,database=DB_DATABASE)
        self.insert_sql = ("insert into student_info (name,sid,idcard,class,sex\
        ,dormitory,mail,address,income,phone)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

    def insert_info(self,person):
        cur = self.conn.cursor()
        student_data = (person.name,person.sid,person.idcard,person._class,person.sex,\
                person.dormitory,person.mail,person.address,person.income,person.phone)

        cur.execute(self.insert_sql,student_data)

        self.conn.commit()
        cur.close()
