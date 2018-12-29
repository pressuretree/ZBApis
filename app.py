from flask import Flask
import requests

app = Flask(__name__)


@app.route('/getAccountInfo')
def hello_world():
    r = requests.get(url='https://trade.zb.cn/api/getAccountInfo?accesskey=youraccesskey&method=getAccountInfo')  # 最基本的GET请求
    # print(r.status_code)  # 获取返回状态
    # print(r.content.decode())

    return r.content


if __name__ == '__main__':
    app.run()
