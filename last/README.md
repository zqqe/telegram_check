# telegram_check
telegram签到

___请放在空白文件夹，包含删除本文件夹内验证码jpg图片的代码___
```
pip3 install telethon
pip3 install requests
pip3 install ddddocr #本地打码
```
提供三种打码，默认打码为ddddocr( https://github.com/sml2h3/ddddocr ),若觉得识别率低，可更换另外两种打码(修改main.py第31，46行)
仅支持以下两类验证码

![图片验证码](/pic/tianruo_2023-1-13-638092035331045066.png "图片验证码")
![图片验证码及内联键盘](/pic/tianruo_2023-1-13-638092035172167098.png "图片验证码及内联键盘")
