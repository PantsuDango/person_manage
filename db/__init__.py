from configparser import ConfigParser
from traceback import print_exc
import pymysql
import time
import os


class Database() :

    def __init__(self) :

        taeget = ConfigParser()
        path = os.getcwd().split("person_manage")[0] + "person_manage"
        taeget.read("%s/config/db.ini"%path, encoding='utf-8')

        user = taeget.get("mysql", "user")
        password = taeget.get("mysql", "password")
        url = taeget.get("mysql", "url")
        port = int(taeget.get("mysql", "port"))
        database = taeget.get("mysql", "database")

        self.db = pymysql.connect(host=url, port=port, user=user, password=password, database=database, charset='UTF8MB4')
        self.cur = self.db.cursor()



if __name__ == "__main__" :

    db = Database()