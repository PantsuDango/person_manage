from flask import Flask, request, jsonify, session
import json
import uuid
from db import Database
from tools.createValidateCode import validate_code
from tools.createKey import decryption
import time
import os
from traceback import print_exc


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'please-generate-a-random-secret_key'
PATH = os.getcwd().split("person_manage")[0] + "person_manage"


# 失败的返回
def jsonFail(message) :

    post_data = {
        "Code": -1,
        "Message": str(message),
        "RequestId": str(uuid.uuid4())
    }
    return jsonify(post_data)


# 成功的返回
def jsonSuccess(data) :

    post_data = {
        "Code": 0,
        "Message": "Success",
        "RequestId": str(uuid.uuid4()),
        "Data": data
    }
    return jsonify(post_data)


# 检查前端的参数
def checkPostData(check_list, post_data) :

    for tmp in check_list:
        if tmp not in post_data:
            return "%s must exist, but it does not"%tmp


# 登录
def Login(post_data) :

    # 校验请求参数
    if 'ValidateCode' not in session :
        return jsonFail("Please get the ValidateCode first")

    check_list = ["ValidateCode", "UserName", "Password"]
    check_result = checkPostData(check_list, post_data)
    if check_result :
        return jsonFail(check_result)

    if post_data['ValidateCode'] != session['ValidateCode'] :
        return jsonFail('ValidateCode error')

    try :
        post_data["Password"] = decryption(post_data["Password"])
    except Exception :
        return jsonFail('password ras decryption error')
    else :
        if post_data["Password"] == "解密失败" :
            return jsonFail('password ras decryption error')

    # 数据库校验账号密码是否正确
    try :
        db = Database()
        user, err = db.check_login(post_data["UserName"], post_data["Password"])
    except Exception as err :
        return jsonFail(err)
    else :
        db.close()
        if err :
            return jsonFail(err)

    # 保存登录信息
    session['ID'] = user["id"]
    session['UserName'] = user["username"]
    session['Password'] = user["password"]
    session['Type'] = user["type"]

    # 删除不需要返回给前端的参数
    del user["createtime"]
    del user["password"]
    del user["lastupdate"]
    del user["status"]

    return jsonSuccess(user)


def Logout() :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session):
        return jsonFail("Login information is invalid, please to login")

    session.clear()
    return jsonSuccess("Success")


# 获取rsa公钥
def GetPublicKey() :

    with open("%s/config/public.pem"%PATH, "r") as file :
        data = file.read()
        data = data.replace("-----BEGIN PUBLIC KEY-----", "")
        data = data.replace("-----END PUBLIC KEY-----", "")
        data = "".join(data.split("\n"))
        return jsonSuccess(data)


# 图片验证码
def GetValidateCode() :

    rand_str, image_base64 = validate_code()
    session['ValidateCode'] = rand_str
    print(rand_str)
    return jsonSuccess(image_base64)


# 添加房屋地址
def AddAddr(post_data) :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session) :
        return jsonFail("Login information is invalid, please to login")
    if session['Type'] not in [2, 3] :
        return jsonFail("user type error")

    check_list = ["Community", "Building", "Dormitory"]
    check_result = checkPostData(check_list, post_data)
    if check_result:
        return jsonFail(check_result)

    try :
        db = Database()
        db.insert_addr(session["ID"], post_data["Community"], post_data["Building"], post_data["Dormitory"])
    except Exception as err :
        return jsonFail(err)
    else :
        db.close()
        return jsonSuccess("Success")


# 更新房屋地址
def UpdateAddr(post_data) :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session) :
        return jsonFail("Login information is invalid, please to login")
    if session['Type'] not in [2, 3] :
        return jsonFail("user type error")

    check_list = ["AddrId", "Community", "Building", "Dormitory"]
    check_result = checkPostData(check_list, post_data)
    if check_result:
        return jsonFail(check_result)

    if "FamilyId" not in post_data :
        post_data["FamilyId"] = 0

    # 更新房屋地址
    try :
        db = Database()
        err = db.update_addr(post_data["AddrId"], post_data["Community"], post_data["Building"], post_data["Dormitory"], post_data["FamilyId"])
    except Exception as err :
        return jsonFail(err)
    else :
        db.close()
        if err :
            return jsonFail(err)

        return jsonSuccess("Success")


# 查询房屋地址信息列表
def ListAddr() :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session) :
        return jsonFail("Login information is invalid, please to login")
    if session['Type'] not in [2, 3] :
        return jsonFail("user type error")

    try :
        db = Database()
        family = db.select_addr(session["ID"], session['Type'])
    except Exception as err :
        return jsonFail(err)
    else :
        db.close()
        # 删除不需要返回给前端的参数
        for index in range(len(family)) :
            del family[index]["createtime"]
            del family[index]["lastupdate"]
            del family[index]["user_id"]

        return jsonSuccess(family)


# 添加家庭信息
def AddFamily(post_data) :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session):
        return jsonFail("Login information is invalid, please to login")
    if session['Type'] not in [2, 3]:
        return jsonFail("user type error")

    check_list = ["JsonData"]
    check_result = checkPostData(check_list, post_data)
    if check_result:
        return jsonFail(check_result)

    if "AddrId" not in post_data :
        post_data["AddrId"] = 0
    if "MasterName" not in post_data :
        post_data["MasterName"] = ""

    try:
        db = Database()
        err = db.insert_family(session["ID"], post_data["AddrId"], post_data["MasterName"], post_data["JsonData"])
    except Exception as err:
        return jsonFail(err)
    else :
        if err :
            return jsonFail(err)
        db.close()
        return jsonSuccess("Success")


# 更新家庭信息
def UpdateFamily(post_data) :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session):
        return jsonFail("Login information is invalid, please to login")
    if session['Type'] not in [2, 3]:
        return jsonFail("user type error")

    check_list = ["FamilyId", "JsonData"]
    check_result = checkPostData(check_list, post_data)
    if check_result:
        return jsonFail(check_result)

    if "AddrId" not in post_data :
        post_data["AddrId"] = 0
    if "MasterName" not in post_data :
        post_data["MasterName"] = ""

    try:
        db = Database()
        err = db.update_family(post_data["FamilyId"], post_data["AddrId"], post_data["MasterName"], post_data["JsonData"])
    except Exception as err:
        return jsonFail(err)
    else:
        db.close()
        if err :
            return jsonFail(err)

        return jsonSuccess("Success")


# 查询家庭信息列表
def ListFamily() :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session) :
        return jsonFail("Login information is invalid, please to login")
    if session['Type'] not in [2, 3] :
        return jsonFail("user type error")

    try :
        db = Database()
        family = db.select_family(session["ID"], session['Type'])
    except Exception as err :
        return jsonFail(err)
    else :
        db.close()
        # 删除不需要返回给前端的参数
        for index in range(len(family)) :
            del family[index]["createtime"]
            del family[index]["lastupdate"]
            del family[index]["user_id"]

        return jsonSuccess(family)


# 注册用户
def Register(post_data) :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session) :
        return jsonFail("Login information is invalid, please to login")
    if session['Type'] not in [2, 3] :
        return jsonFail("user type error")

    check_list = ["UserName", "Type"]
    check_result = checkPostData(check_list, post_data)
    if check_result:
        return jsonFail(check_result)

    if "Password" not in post_data :
        post_data["Password"] = "123456"

    if post_data["Type"] == 3 :
        return jsonFail("user type error")
    if post_data["Type"] == 2 and session['Type'] != 3 :
        return jsonFail("user type error")
    if post_data["Type"] not in [1, 2, 3] :
        return jsonFail("user type error")
    if post_data["Type"] == 1 and "PersonnelId" not in post_data :
        return jsonFail("PersonnelId must exist")

    try :
        db = Database()
        err = db.insert_user(session["ID"], post_data["UserName"], post_data["Password"], post_data["Type"], post_data["PersonnelId"])
    except Exception as err :
        return jsonFail(err)
    else :
        if err :
            return jsonFail(err)
        db.close()
        return jsonSuccess("Success")


# 新增用户信息
def AddPersonnel(post_data) :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session) :
        return jsonFail("Login information is invalid, please to login")
    if session['Type'] not in [2, 3] :
        return jsonFail("user type error")

    check_list = ["FamilyId", "JsonData"]
    check_result = checkPostData(check_list, post_data)
    if check_result:
        return jsonFail(check_result)

    if "UserId" not in post_data :
        post_data["UserId"] = 0
    if "Type" not in post_data :
        post_data["Type"] = 0
    if "Domicile" not in post_data :
        post_data["Domicile"] = ""

    try :
        db = Database()
        err = db.insert_personnel(post_data["UserId"], post_data["FamilyId"], post_data["Type"], post_data["Domicile"], post_data["JsonData"])
    except Exception as err :
        return jsonFail(err)
    else :
        if err :
            return jsonFail(err)
        db.close()
        return jsonSuccess("Success")


# 更新用户信息
def UpdatePersonnel(post_data) :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session) :
        return jsonFail("Login information is invalid, please to login")

    check_list = ["PersonnelId", "JsonData"]
    check_result = checkPostData(check_list, post_data)
    if check_result:
        return jsonFail(check_result)

    if "UserId" not in post_data :
        post_data["UserId"] = 0
    if "Type" not in post_data :
        post_data["Type"] = 0
    if "Domicile" not in post_data :
        post_data["Domicile"] = ""

    try :
        db = Database()
        err = db.update_personnel(post_data["PersonnelId"], post_data["UserId"], post_data["Type"], post_data["Domicile"], post_data["JsonData"])
    except Exception as err :
        return jsonFail(err)
    else :
        if err :
            return jsonFail(err)
        db.close()
        return jsonSuccess("Success")


# 查询用户信息列表
def ListPersonnel() :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session) :
        return jsonFail("Login information is invalid, please to login")

    # 如果是管理员登录
    if session["Type"] in [2, 3] :
        try :
            result = []
            db = Database()
            family = db.select_family(session["ID"], session['Type'])
            for index, tmp in enumerate(family) :
                # 查询个人信息
                personnel = db.select_personnel(tmp["id"])
                # 删除不需要返回给前端的参数
                for index in range(len(personnel)) :
                    del personnel[index]["createtime"]
                    del personnel[index]["lastupdate"]
                result.append(personnel)

        except Exception as err :
            return jsonFail(err)
        else :
            db.close()
            return jsonSuccess(result)

    # 如果是普通用户登录
    else :
        try :
            db = Database()
            result = db.select_personnel_by_normal_user(session["ID"])
        except Exception as err:
            return jsonFail(err)
        else:
            db.close()
            return jsonSuccess(result)


# 获取账号列表
def ListUser() :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session) :
        return jsonFail("Login information is invalid, please to login")
    if session['Type'] not in [2, 3] :
        return jsonFail("user type error")

    try:
        db = Database()
        result = db.select_user(session["ID"], session["Type"])
    except Exception as err:
        return jsonFail(err)
    else:
        for index in range(len(result)) :
            del result[index]["createtime"]
            del result[index]["lastupdate"]
            del result[index]["status"]

        db.close()
        return jsonSuccess(result)


# 信息检索
def SelectInfo(post_data) :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session) :
        return jsonFail("Login information is invalid, please to login")
    if session['Type'] not in [2, 3] :
        return jsonFail("user type error")

    try:
        db = Database()
        result = db.select_info(session["ID"], session["Type"], post_data)
    except Exception as err:
        print_exc()
        return jsonFail(err)
    else:
        db.close()
        return jsonSuccess(result)


# 查询家庭详情
def FamilyInfo(post_data) :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session):
        return jsonFail("Login information is invalid, please to login")

    check_list = ["FamilyId"]
    check_result = checkPostData(check_list, post_data)
    if check_result:
        return jsonFail(check_result)

    try:
        db = Database()
        result = db.select_family_info(post_data["FamilyId"])
    except Exception as err:
        return jsonFail(err)
    else:
        db.close()
        return jsonSuccess(result)


# 修改账户信息
def ModifyUser(post_data) :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session):
        return jsonFail("Login information is invalid, please to login")
    if session['Type'] not in [2, 3] :
        return jsonFail("user type error")

    check_list = ["UserId", "Password"]
    check_result = checkPostData(check_list, post_data)
    if check_result:
        return jsonFail(check_result)

    try:
        db = Database()
        err = db.modify_user(post_data["UserId"], post_data["Password"])
    except Exception as err:
        return jsonFail(err)
    else:
        if err :
            return jsonFail(err)
        db.close()
        return jsonSuccess("Success")


# 删除账户
def DeleteUser(post_data) :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session):
        return jsonFail("Login information is invalid, please to login")
    if session['Type'] not in [2, 3] :
        return jsonFail("user type error")

    check_list = ["UserId"]
    check_result = checkPostData(check_list, post_data)
    if check_result:
        return jsonFail(check_result)

    try:
        db = Database()
        err = db.delete_user(post_data["UserId"])
    except Exception as err:
        return jsonFail(err)
    else:
        if err :
            return jsonFail(err)
        db.close()
        return jsonSuccess("Success")


# 查询人员详情
def PersonnelInfo(post_data) :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session) :
        return jsonFail("Login information is invalid, please to login")

    check_list = ["PersonnelId"]
    check_result = checkPostData(check_list, post_data)
    if check_result:
        return jsonFail(check_result)

    try :
        db = Database()
        err, result = db.select_personnel_info(post_data["PersonnelId"])
    except Exception as err :
        return jsonFail(err)
    else :
        if err :
            return jsonFail(err)
        db.close()
        return jsonSuccess(result)

# 主接口
@app.route("/person_manage/api", methods=["POST"])
def postData():

    # 接收前端请求
    try :
        post_data = request.get_data()
        post_data = json.loads(post_data.decode("utf-8"))
    except Exception as err:
        return jsonFail(err)

    if "Action" not in post_data :
        return jsonFail("Action must exist, but it does not")

    # 注册
    if post_data["Action"] == "Register" :
        return Register(post_data)
    # 登录
    elif post_data["Action"] == "Login" :
        return Login(post_data)
    # 登出
    elif post_data["Action"] == "Logout" :
        return Logout()
    # 获取公钥
    elif post_data["Action"] == "GetPublicKey" :
        return GetPublicKey()
    # 获取验证码图片
    elif post_data["Action"] == "GetValidateCode" :
        return GetValidateCode()
    # 添加房屋地址
    elif post_data["Action"] == "AddAddr" :
        return AddAddr(post_data)
    # 更新房屋地址
    elif post_data["Action"] == "UpdateAddr" :
        return UpdateAddr(post_data)
    # 查询房屋地址列表
    elif post_data["Action"] == "ListAddr" :
        return ListAddr()
    # 添加房屋家庭信息
    elif post_data["Action"] == "AddFamily" :
        return AddFamily(post_data)
    # 更新家庭信息
    elif post_data["Action"] == "UpdateFamily" :
        return UpdateFamily(post_data)
    # 查看家庭信息列表
    elif post_data["Action"] == "ListFamily" :
        return ListFamily()
    # 添加人员信息
    elif post_data["Action"] == "AddPersonnel" :
        return AddPersonnel(post_data)
    # 更新人员信息
    elif post_data["Action"] == "UpdatePersonnel":
        return UpdatePersonnel(post_data)
    # 更新人员信息
    elif post_data["Action"] == "ListPersonnel":
        return ListPersonnel()
    # 更新人员信息
    elif post_data["Action"] == "ListUser":
        return ListUser()
    # 信息检索
    elif post_data["Action"] == "SelectInfo":
        return SelectInfo(post_data)
    # 查询家庭详情
    elif post_data["Action"] == "FamilyInfo":
        return FamilyInfo(post_data)
    # 修改账户信息
    elif post_data["Action"] == "ModifyUser":
        return ModifyUser(post_data)
    # 删除账户信息
    elif post_data["Action"] == "DeleteUser":
        return DeleteUser(post_data)
    # 查询人员详情
    elif post_data["Action"] == "PersonnelInfo":
        return PersonnelInfo(post_data)
    else :
        return jsonFail("Action %s doesn't exist"%post_data["Action"])


if __name__ == "__main__":

    app.run(debug=False, host="0.0.0.0", port=6666)