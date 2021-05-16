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
        jsonFail("Please get the ValidateCode first")

    check_list = ["ValidateCode", "UserName", "Password", "Type"]
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
        user, err = db.check_login(post_data["UserName"], post_data["Password"], post_data["Type"])
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


# 添加小区房屋
def AddFamily(post_data) :

    # 校验请求参数是否符合预期
    if ("ID" not in session) or ("Type" not in session) :
        jsonFail("Login information is invalid, please to login")
    if (session['Type'] != 2) or (session['Type'] != 3) :
        jsonFail("user type error")

    check_list = ["Community", "Building", "Dormitory"]
    check_result = checkPostData(check_list, post_data)
    if check_result:
        return jsonFail(check_result)


    try :
        db = Database()
        db.insert_family(session["ID"], post_data["Community"], post_data["Building"], post_data["Dormitory"])
    except Exception as err :
        return jsonFail(err)
    else :
        db.close()
        return jsonSuccess("Success")



# 主接口
@app.route("/person_manage/api", methods=["POST"])
def postData():

    try :
        post_data = request.get_data()
        post_data = json.loads(post_data.decode("utf-8"))
    except Exception as err:
        return jsonFail(err)

    if "Action" not in post_data :
        return jsonFail("Action must exist, but it does not")

    if post_data["Action"] == "Login" :
        return Login(post_data)
    if post_data["Action"] == "GetPublicKey":
        return GetPublicKey()
    if post_data["Action"] == "GetValidateCode":
        return GetValidateCode()
    if post_data["Action"] == "AddFamily":
        return AddFamily(post_data)
    else :
        return jsonFail("Action %s doesn't exist"%post_data["Action"])


if __name__ == "__main__":

    app.run(debug=False, host="0.0.0.0", port=6666)