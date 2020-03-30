#简单的付款验证
import time

isflog = False
def login():#定义登陆函数
    username = input('请输入用户名')
    password = input('请输入密码')
    if username == 'admin' and password == '123456': #判断账户与密码是否正确
        print('账号与密码正确')
        return True
    else:
        print('密码与账号错误，请再次登录')
        return False

def denglu(func):#定义验证状态的还是
    def wrapper(*args,**arges):
        print('正在检测登录状态')
        global isflog
        if isflog:
            print('登陆成功')
            func(*args,**arges)
        else:
            print('请您前去登陆')
            isflog =login()

    return wrapper


@denglu #在付款前加上装饰器，用户没有登陆就不能付款
def pay(money):
    global flog
    print('你需要付{}元，才能买下此商品'.format(money))
    print('------付款中----')
    time.sleep(2)
    print('付款成功，你已经买下此商品')
    flog = False


# pay(100)#第一次付款因没登录导致前去登录
# pay(100)#有了第一次的登陆成功就可以付款
money = input('请输入你的付款金额')
flog = True
while flog:
    pay(money)
