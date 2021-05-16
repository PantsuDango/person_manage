from Crypto import Random
from Crypto.PublicKey import RSA
import os

from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64


# 项目路径
path = os.getcwd().split("person_manage")[0] + "person_manage"


# 创建Key
def crateKey() :

    # 伪随机数生成器
    random_generator = Random.new().read
    # rsa算法生成实例
    rsa = RSA.generate(1024, random_generator)
    # 私钥的生成
    private_pem = rsa.exportKey()
    with open("%s/config/private.pem"%path, "wb") as f:
        f.write(private_pem)
    # 公钥的生成
    public_pem = rsa.publickey().exportKey()
    with open("%s/config/public.pem"%path, "wb") as f:
        f.write(public_pem)


# 加密
def encrypt() :

    message = "123456"
    rsakey = RSA.importKey(open("%s/config/public.pem"%path).read())
    # 创建用于执行pkcs1_v1_5加密或解密的密码
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(message.encode('utf-8')))
    print(cipher_text.decode('utf-8'))

    return cipher_text.decode('utf-8')


# 解密
def decryption(cipher_text) :

    encrypt_text = str(cipher_text).encode('utf-8')
    rsakey = RSA.importKey(open("%s/config/private.pem"%path).read())
    # 创建用于执行pkcs1_v1_5加密或解密的密码
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(encrypt_text), "解密失败")

    return text.decode('utf-8')


if __name__ == "__main__" :

    cipher_text = encrypt()
    decryption(cipher_text)