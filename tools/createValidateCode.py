from PIL import Image, ImageDraw, ImageFont
import random
import os
import base64


def validate_code():

    # 项目路径
    path = os.getcwd().split("person_manage")[0] + "person_manage"
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (255,255,255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = '0123456789'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象
    font = ImageFont.truetype("%s/config/FreeMono.ttf"%path, 23)
    # 绘制4个字
    for i in range(4):
        # 构造字体颜色
        fontcolor = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        draw.text((5+23*i, 2), rand_str[i], font=font, fill=fontcolor)

    # 释放画笔
    del draw

    # 将图片保存在内存中，文件类型为png
    im.save("%s/config/validateCode.png"%path)

    # 转base64
    with open("%s/config/validateCode.png"%path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        return s


if __name__ == "__main__" :

    validate_code()