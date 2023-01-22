import requests
import base64
import json
import ddddocr

#https://truecaptcha.org/每天免费100次
def truecaptcha(pic_code):
    with open(pic_code, 'rb') as f:
        image_base64 = base64.b64encode(f.read())
        #print(image_base64)
    try:
        url="https://api.apitruecaptcha.org/one/gettext"
        data={
        	"userid":"",#用户名
        	"apikey":"",#apikey
        	"data":str(image_base64, encoding = "utf-8")
        }
        res=requests.post(url,data=json.dumps(data)).text
        res=json.loads(res)
        res=res["result"]
    except:
        res='失败'
    return res


#图鉴http://ttshitu.com/register.html?inviter=5dcabc3453734ac08335902139a500af  一元起充，识别率更高，一元500次
def ttshitu(pic_code):
    with open(pic_code, 'rb') as f:
        image_base64 = base64.b64encode(f.read())
    try:
        url="http://api.ttshitu.com/predict"
        data={
            "username": "", #用户名
            "password": "", #密码
            "typeid": 7, #识别类型
            "image": str(image_base64, encoding = "utf-8")
        }
        res=requests.post(url,data=json.dumps(data)).text
        res=json.loads(res)
        res=res["data"]["result"]
    except:
        res='失败'
    return res

#ddddocr为本地打码 无需注册账号 pip3 install ddddocr
def ddocr(pic_code):
    ocr = ddddocr.DdddOcr(beta=True)
    with open(pic_code, 'rb') as f:
        image = f.read()
    res = ocr.classification(image)
    return res
