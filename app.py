import json

from flask import Flask
from zapi import ZApi

app = Flask(__name__)

'''
功能：调用zb.com REST APi接口demo
使用指南：demo中只提供了getAccountInfo接口使用方法，其他接口使用方法类推
'''
@app.route("/getAccountInfo")
def hello_world():
    #r = requests.get(url='https://trade.zb.cn/api/getAccountInfo?accesskey=youraccesskey&method=getAccountInfo')  # 最基本的GET请求

    print("zb is creating!")   #帮助信息
    #构建对象
    zb = ZApi(access_key='646023d1-a536-4ef3-86ab-aa1c1577dca4', secret_key='94b9ed6a-6bde-430b-a898-7aeef54b820d')
    # a = zb.all_ticker()
    print("zb is created!")     #帮助信息
    #调用api
    a = zb.get_account_info()
    #控制台日志
    print(a)
    #数据返回前端
    return json.dumps(a)


@app.route("/test")
def test():
    return "test"

if __name__ == '__main__':
    app.run()
