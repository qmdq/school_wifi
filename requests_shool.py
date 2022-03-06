from email import header
from sys import flags
import requests
def Longin(UserId,password,cooking,Referer,qs):#USerId账号password密码#cooking你的cooking,
    #Referer#通过浏览器抓取包含mac地址等本信息
    url = "http://192.168.255.2/eportal/InterFace.do?method=login"
    data = {
        "userId": UserId,
        "password": password,
        "service":" ",
        "queryString": qs,
        "operatorPwd": " ",
        "operatorUserId": " ",
        "validcode": " ",
        "passwordEncrypt": "false"

    }
    header = {
       

        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Length": "647",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": cooking,

        "Host": "192.168.255.2",
        "Origin": "http://192.168.255.2",

        "Referer":Referer,

        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
    }
    rpon = requests.post(url,data,headers=header)#post请求
    if(rpon.status_code<=400):#判读是否登录成功

        print(rpon.text)
        print(rpon.status_code)
        return True#
    else:
        print(rpon.text)
        return False

if __name__=="__main__":
    user = "15488877"
    pwd = "123321"
    cook = "EPORTAL_COOKIE_SAVEPASSWORD=true; EPORTAL_COOKIE_USERNAME=15662706297; EPORTAL_COOKIE_PASSWORD=123321; EPORTAL_USER_GROUP=root; JSESSIONID=771ECF55FB8518D8DC9564C11C6AA98A; JSESSIONID=EE2D8BAE4FFC9B88EF9C49A99DAF27CB"
    rf = "http://192.168.255.2/eportal/index.jsp?wlanuserip=3a53a032429e05f71d211fe3b3cc705b&wlanacname=8fa0cee68308b61e850d0bdea29859fe&ssid=&nasip=a599d5b4bd54ade7415734f1c58c2da5&snmpagentip=&mac=b86fb900c5f046d147df944ec8b1f5e3&t=wireless-v2&url=ed3aaf1ff49edb56a8aa51ef436e689ac7c7c96bbdb258c0&apmac=&nasid=8fa0cee68308b61e850d0bdea29859fe&vid=38a07c734649deed&port=f6516ab02a224608&nasportid=4574fd3057584d100f5cec73992841aeaf306a9bc14aa23c77fb2334b8bdda90a33dfc6b0f6092c7"
    Longin(user,pwd,cook,rf)