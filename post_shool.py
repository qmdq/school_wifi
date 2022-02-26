from datetime import date

import requests
from requests_shool import Longin
class Shool_Wif():
    def __init__(self,user,passwd) -> None:
        #file文件名
        self.user = user#账号
        self.pwd = passwd#密码
        #self.file = file
       
    def open_config(self):#打开cook和Referer文件
        with open("rf.txt","r") as f:
            self.Referer = f.read()
        with open("cook.txt",) as cf:
            self.cook = cf.read()
        with open("qs.txt","r") as qs:
            self.qs = qs.read()
    def shool_post(self):
        stata =  Longin(self.user,self.pwd,self.cook,self.Referer,self.qs)
        if(stata == True):
            print("登录成功")
            print(stata)
            return True
        else:
            print("登录失败")
            return False

if __name__ =="__main__":
    user = "15662706297"
    pwd = "123321"
    S1 = Shool_Wif(user,pwd)
    S1.open_config()
    S1.shool_post()