from flask import Flask, request, jsonify, session
import json
import uuid
from db import Database
from tools.createValidateCode import validate_code
import time
import os


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'please-generate-a-random-secret_key'
path = os.getcwd().split("person_manage")[0] + "person_manage"


def jsonFail(message) :

    post_data = {
        "Code": -1,
        "Message": str(message),
        "RequestId": str(uuid.uuid4())
    }

    return jsonify(post_data)


def jsonSuccess(data) :

    post_data = {
        "Code": 0,
        "Message": "Success",
        "RequestId": str(uuid.uuid4()),
        "Data": data
    }

    return jsonify(post_data)


# 登录
def Login(post_data) :

    return jsonSuccess(post_data)


# 获取rsa公钥
def GetPublicKey() :

    with open("%s/config/public.pem"%path, "r") as file :
        data = file.read()
        data = data.replace("-----BEGIN PUBLIC KEY-----", "")
        data = data.replace("-----END PUBLIC KEY-----", "")
        data = "".join(data.split("\n"))
        return jsonSuccess(data)


# 图片验证码
def GetValidateCode() :

    rand_str, image_base64 = validate_code()
    session['ValidateCode'] = rand_str
    return jsonSuccess(image_base64)


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
    else :
        return jsonFail("Action %s doesn't exist"%post_data["Action"])


if __name__ == "__main__":

    app.run(debug=False, host="0.0.0.0", port=6666)