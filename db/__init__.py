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
    def check_login(self, username, password, type) :

        sql = """
            select * from user_info where username='%s' and type=%d and status=0;
        """%(username, type)

        self.cur.execute(sql)
        user = self.sql_fetch_json()

        if not user :
            err = "user doesn't exist"
            return None, err

        if user[0]["password"] != password :
            err = "password error"
            return None, err


        return user[0], None


    # 写入房屋数据
    def insert_family(self, user_id, community, building, dormitory) :

        sql = """
            INSERT INTO `family_info` 
            (id, user_id, community, building, dormitory, master_name, json_data, createtime) 
            VALUES (null, %d, '%s', '%s', '%s', null, null, now());
        """%(user_id, community, building, dormitory)

        self.cur.execute(sql)



    # 更新家庭信息
    def update_family(self, id, master_name, json_data) :

        check_sql = """
            select * from family_info where id=%d;
        """%(id)
        self.cur.execute(check_sql)
        family = self.sql_fetch_json()
        if not family :
            err = "FamilyId doesn't exist"
            return err


        sql = """
            update family_info set master_name='%s', json_data='%s' where id=%d;
        """%(master_name, json_data, id)
        self.cur.execute(sql)



if __name__ == "__main__" :

    db = Database()