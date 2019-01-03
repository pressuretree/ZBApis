import json

from flask import Flask
from zapi import ZApi

app = Flask(__name__)

'''
功能：调用zb.com REST APi接口demo
使用指南：demo中只提供了getAccountInfo接口使用方法，其他接口使用方法类推
'''
@app.route("/getAccountInfo")
def get_account_Info():
    #构建对象，这里需要把AK和SK修改为自己的AK/SK
    zb = ZApi(access_key='646023d1-a536-4ef3-86ab-aa1c1577dca4', secret_key='94b9ed6a-6bde-430b-a898-7aeef54b820d')

    #调用api
    a = zb.get_account_info()

    #数据返回前端
    return json.dumps(a)

@app.route("/test")
def test():
    return "test"

if __name__ == '__main__':
    app.run()
