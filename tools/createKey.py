from Crypto import Random
from Crypto.PublicKey import RSA
import os

# 项目路径
path = os.getcwd().split("person_manage")[0] + "person_manage"
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