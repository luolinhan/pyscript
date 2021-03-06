'''
def main():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()
'''
import flask,json
from flask import request

'''
flask: seb框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传入url,username,passwd
'''

#创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)
#访问地址 http://127.0.0.1:8888/login?username=lhluo&pwd=1
#server.route()可以将普通函数转变为服务　登录接口的路径、请求方式
@server.route('/login',methods=['get','post'])
def login():
    #获取通过url请求传参的数据
    username = request.values.get('name')
    #获取url请求传的密码，明文
    pwd=request.values.get('pwd')
    #判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None
    if username and pwd:
        if username == 'lhluo' and pwd == '1':
            resu={'code':200,'message':'登录成功'}
            return json.dumps(resu,ensure_ascii=False)#将字典转换为Json串，json是字符串
        else:
            resu={'code':-1,'message':'账号密码错误'}
            return json.dumps(resu,ensure_ascii=False)

    else:
        resu={'code':1001,'message':'参数不能为空'}
        return json.dumps(resu,ensure_ascii=False)

if __name__== '__main__':
    server.run(debug=True,port = 8888,host='0.0.0.0')#指定端口,host,0.0.0.0代表不管几个网卡，任何ip都可访问