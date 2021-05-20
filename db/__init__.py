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
        """%(user_id, addr_id, master_name, json_data)
        self.cur.execute(sql)

        if addr_id > 0 :
            check_sql = """
                select * from addr_info where id=%d;
            """%(addr_id)
            self.cur.execute(check_sql)
            family = self.sql_fetch_json()
            if not family:
                err = "AddrId doesn't exist"
                return err

            sql = """
                select * from family_info order by id desc limit 1;
            """
            self.cur.execute(sql)
            family_info = self.sql_fetch_json()

            sql = """
                update addr_info set family_id=%d, lastupdate=now() where id=%d;
            """%(family_info[0]["id"], addr_id)
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

        if addr_id > 0:
            check_sql = """
                select * from addr_info where id=%d;
            """ % (id)
            self.cur.execute(check_sql)
            family = self.sql_fetch_json()
            if not family:
                err = "AddrId doesn't exist"
                return err

            sql = """
                select * from family_info order by id desc limit 1;
            """
            self.cur.execute(sql)
            family_info = self.sql_fetch_json()

            sql = """
                update addr_info set family_id=%d, lastupdate=now() where id=%d;
            """ % (family_info[0]["id"], addr_id)
            self.cur.execute(sql)


    # 查询家庭信息列表
    def select_family(self, user_id, type):

        if type == 3:
            sql = """
                select * from family_info;
            """
        else:
            sql = """
                select * from family_info where user_id=%d;
            """ % (user_id)

        self.cur.execute(sql)
        family = self.sql_fetch_json()
        return family


    def insert_user(self, register_id, username, password, type, personnel_id) :

        if type == 1 :
            check_sql = """
                select * from personnel_info where id=%d;
            """%(personnel_id)
            self.cur.execute(check_sql)
            rows = self.sql_fetch_json()
            if not rows :
                err = "PersonnelId doesn't exist"
                return err

        sql = """
            INSERT INTO `user_info` (id, username, password, type, status, createtime, lastupdate) 
            VALUES (null, '%s', '%s', %d, 0, now(), now());
        """%(username, password, type)
        self.cur.execute(sql)

        sql = """
            select * from user_info where username='%s';
        """ % (username)
        self.cur.execute(sql)
        rows = self.sql_fetch_json()

        if type == 1 :
            sql = """
                update personnel_info set user_id=%d where id=%d;
            """%(rows[0]["id"], personnel_id)
            self.cur.execute(sql)

        sql = """
            INSERT INTO `register_map` (id, register_id, registered_id, createtime) 
            VALUES (null, %d, %d, now());
        """%(register_id, rows[0]["id"])
        self.cur.execute(sql)


    # 添加人员信息
    def insert_personnel(self, user_id, family_id, type, domicile, json_data) :

        check_sql = """
            select * from family_info where id=%d;
        """%(family_id)
        self.cur.execute(check_sql)
        family = self.sql_fetch_json()
        if not family:
            err = "FamilyId doesn't exist"
            return err

        sql = """
            INSERT INTO `personnel_info` (id, user_id, family_id, type, domicile, json_data, createtime, lastupdate) 
            VALUES (null, %d, %d, %d, '%s', '%s', now(), now());
        """%(user_id, family_id, type, domicile, json_data)

        self.cur.execute(sql)

    # 更新人员信息
    def update_personnel(self, id, user_id, type, domicile, json_data):

        check_sql = """
            select * from personnel_info where id=%d;
        """%(id)
        self.cur.execute(check_sql)
        family = self.sql_fetch_json()
        if not family:
            err = "PersonnelId doesn't exist"
            return err

        sql = """
            update personnel_info set user_id=%d, type=%d, domicile='%s', json_data='%s', lastupdate=now() where id=%d;
        """%(user_id, type, domicile, json_data, id)
        self.cur.execute(sql)


    # 查询个人信息列表
    def select_personnel(self, family_id) :

        sql = """
            select * from personnel_info where family_id=%d;
        """%(family_id)
        self.cur.execute(sql)
        family = self.sql_fetch_json()
        return family


    # 普通用户登录查询用户信息
    def select_personnel_by_normal_user(self, user_id) :

        sql = """
            select * from personnel_info where user_id=%d;
        """%(user_id)
        self.cur.execute(sql)
        personnel = self.sql_fetch_json()

        result = {}
        if personnel :
            result["personnel_info"] = personnel[0]
            sql = """
                select * from family_info where id=%d;
            """%personnel[0]["family_id"]
            self.cur.execute(sql)
            family = self.sql_fetch_json()
            if family:
                result["family_info"] = family

        return result

    # 查询账号列表
    def select_user(self, user_id, type) :

        if type == 3 :
            sql = """
                select * from user_info where status=0;
            """
            self.cur.execute(sql)
            result = self.sql_fetch_json()

        else :
            sql = """
                select * from register_map where register_id=%d;
            """%(user_id)
            self.cur.execute(sql)
            rows = self.sql_fetch_json()

            result = []
            for row in rows :
                id = row["registered_id"]
                sql = """
                    select * from user_info where id=%d and status=0;
                """%id
                self.cur.execute(sql)
                user_info = self.sql_fetch_json()
                result += user_info

        return result

    # 信息检索
    def select_info(self, user_id, type, post_data) :

        if type == 3 :
            sql = """
                select * from addr_info where family_id != 0;
            """
        else :
            sql = """
                select * from addr_info where family_id != 0 and user_id=%d;
            """%user_id
        self.cur.execute(sql)
        rows = self.sql_fetch_json()

        addr_info = []
        if "Community" in post_data :
            for row in rows :
                if post_data["Community"] in row["community"] :
                    addr_info.append(row)
        else :
            addr_info = rows

        rows = []
        for row in addr_info :
            sql = """
                select * from family_info where addr_id=%d;
            """%(row["family_id"])
            self.cur.execute(sql)
            tmp = self.sql_fetch_json()
            if tmp :
                tmp[0]["community"] = row["community"]
            rows += tmp

        family_info = []
        if "MasterName" in post_data :
            for row in rows :
                if post_data["MasterName"] in row["master_name"] :
                    family_info.append(row)
        else :
            family_info = rows

        rows = []
        for row in family_info :
            sql = """
                select * from personnel_info where family_id=%d;
            """%(row["id"])
            self.cur.execute(sql)
            tmp = self.sql_fetch_json()
            if tmp :
                for index in range(len(tmp)) :
                    tmp[index]["master_name"] = row["master_name"]
                    tmp[index]["community"] = row["community"]
                    tmp[index]["family_json_data"] = row["json_data"]
            rows += tmp

        personnel_info = []
        if "Type" in post_data :
            for row in rows :
                if post_data["Type"] == row["type"] :
                    personnel_info.append(row)
        else :
            personnel_info = rows

        result = []
        if "Domicile" in post_data :
            for row in personnel_info :
                if post_data["Domicile"] in row["domicile"] :
                    result.append(row)
        else :
            result = personnel_info

        for index in range(len(result)) :
            result[index]["personnel_json_data"] = result[index]["json_data"]
            del result[index]["json_data"]
            del result[index]["createtime"]
            del result[index]["lastupdate"]

        return result


    # 查询家庭详情
    def select_family_info(self, id) :

        sql = """
            select * from family_info where id=%d;
        """%id
        self.cur.execute(sql)
        family_info = self.sql_fetch_json()

        sql = """
            select * from personnel_info where family_id=%d;
        """%id
        self.cur.execute(sql)
        personnel_info = self.sql_fetch_json()
        
        result = {}
        if family_info :
            result["family_info"] = family_info[0]
        result["personnel_info"] = personnel_info
        
        return result


    def modify_user(self, id, password) :

        check_sql = """
            select * from user_info where id=%d;
        """ % (id)
        self.cur.execute(check_sql)
        rows = self.sql_fetch_json()
        if not rows:
            err = "UserId doesn't exist"
            return err

        sql = """
            update user_info set password='%s' where id=%d;
        """%(password, id)
        self.cur.execute(sql)


if __name__ == "__main__" :

    db = Database()