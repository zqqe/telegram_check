import requests
import base64
import json

#验证码平台https://truecaptcha.org/，每天免费100次
def truecaptcha():
    with open("1.jpg", 'rb') as f:
        image_base64 = base64.b64encode(f.read())
        #print(image_base64)
    try:
        url="https://api.apitruecaptcha.org/one/gettext"
        data={
        	"userid":"",#userid
        	"apikey":"",#apikey
        	"data":str(image_base64, encoding = "utf-8")
        }
        res=requests.post(url,data=json.dumps(data)).text
        res=json.loads(res)
        res=res["result"]
    except:
        res='失败'
    return res
