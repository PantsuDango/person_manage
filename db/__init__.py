from configparser import ConfigParser
from traceback import print_exc
import pymysql
import time
import os
import json


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


    # 关闭数据库连接
    def close(self):

        self.db.commit()
        self.cur.close()
        self.db.close()


    # 查询结果转json格式
    def sql_fetch_json(self):

        keys = []
        for column in self.cur.description:
            keys.append(column[0])
        key_number = len(keys)

        json_data = []
        for row in self.cur.fetchall():
            item = dict()
            for q in range(key_number):
                item[keys[q]] = row[q]
            json_data.append(item)

        return json_data


    # 检查登录
    def check_login(self, username, password) :

        sql = """
            select * from user_info where username='%s' and status=0;
        """%(username)

        self.cur.execute(sql)
        user = self.sql_fetch_json()

        if not user :
            err = "user doesn't exist"
            return None, err

        if user[0]["password"] != password :
            err = "password error"
            return None, err


        return user[0], None


    # 写入房屋地址
    def insert_addr(self, user_id, community, building, dormitory) :

        sql = """
            INSERT INTO `addr_info` 
            (id, user_id, community, building, dormitory, family_id, createtime, lastupdate) 
            VALUES (null, %d, '%s', '%s', '%s', 0, now(), now());
        """%(user_id, community, building, dormitory)

        self.cur.execute(sql)


    # 更新房屋地址
    def update_addr(self, id, community, building, dormitory, family_id) :

        check_sql = """
            select * from addr_info where id=%d;
        """%(id)
        self.cur.execute(check_sql)
        family = self.sql_fetch_json()
        if not family :
            err = "AddrId doesn't exist"
            return err


        sql = """
            update addr_info set community='%s', building='%s', dormitory='%s', family_id=%d, lastupdate=now() where id=%d;
        """%(community, building, dormitory, family_id, id)
        self.cur.execute(sql)


    # 查询房屋地址列表
    def select_addr(self, user_id, type) :

        if type == 3 :
            sql = """
                select * from addr_info;
            """
        else :
            sql = """
                select * from addr_info where user_id=%d;
            """%(user_id)

        self.cur.execute(sql)
        family = self.sql_fetch_json()
        return family


    # 写入家庭信息
    def insert_family(self, user_id, addr_id, master_name, json_data):

        sql = """
            INSERT INTO `family_info` 
            (id, user_id, addr_id, master_name, json_data, createtime, lastupdate) 
            VALUES (null, %d, %d, '%s', '%s', now(), now());
        """ % (user_id, addr_id, master_name, json_data)

        self.cur.execute(sql)


    # 更新家庭信息
    def update_family(self, id, addr_id, master_name, json_data):

        check_sql = """
            select * from family_info where id=%d;
        """%(id)
        self.cur.execute(check_sql)
        family = self.sql_fetch_json()
        if not family :
            err = "FamilyId doesn't exist"
            return err

        sql = """
            update family_info set addr_id=%d, master_name='%s', json_data='%s', lastupdate=now() where id=%d;
        """ % (addr_id, master_name, json_data, id)
        self.cur.execute(sql)


    def insert_user(self, username, password, type) :

        sql = """
            INSERT INTO `user_info` (id, username, password, type, status, createtime, lastupdate) 
            VALUES (null, '%s', '%s', %d, 0, now(), now());
        """%(username, password, type)

        self.cur.execute(sql)


    def insert_personnel(self, user_id, family_id, type, domicile, json_data) :

        sql = """
            INSERT INTO `personnel_info` (id, user_id, family_id, type, domicile, json_data, createtime) 
            VALUES (null, %d, %d, %d, '%s', '%s', now());
        """%(user_id, family_id, type, domicile, json_data)

        self.cur.execute(sql)





if __name__ == "__main__" :

    db = Database()