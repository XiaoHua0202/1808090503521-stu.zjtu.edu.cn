'''
        自定义模块
为了使主文件项目看着没那么繁琐，
将本模块的函数导入到仿博客园系统中
    '1.请登录',
    '2.请注册',
    '3.进入文章页面',
    '4.进入评论界面',
    '5.进入日记界面',
    '6.进入收藏页面',
    '7.注销账号',
    '8.退出整个程序'
'''
import time #导入时间模块


isflog = False #定义一个标识符，判断是否登陆

user_dic = {}   #定义一个空字典，来存放用户信息
def wrapper(f):#装饰器 判断用户是否登陆
    def inner(*args,**kwargs):

        global isflog
        if isflog :
            ret = f(*args,**kwargs)
        else:
            print('请你先去登陆')
            ret = f1()
        return ret
    return inner


count = 0 #计数器，用来计数登陆次数

def f1():
    global isflog
    global count

    count +=1#计数

    global isflog_circle

    print('正在检测登录状态')

    time.sleep(2)
    username = input('请你输入用户名')
    password = input('请你输入你的密码')

    if username in user_dic.keys():
        if password == user_dic[username]:
            print('登陆成功')
            isflog =True
        else:
            print('你输入的用户名或密码错误')
    else:
        print('没有该用户，请你前去注册')
        f2()


def f2():
    print('欢迎来到注册界面')
    count = 0

    username = input('请输入你的用户名')

    password = input('请输入你的密码')
    if username.isalnum(): #用户名只能是字母和数字，不能为特殊字符
        if username not in user_dic.keys(): #判断注册用户在不在已注册信息中
            if 6<=len(password)<=14:#判断密码 只能为6-14个字符
                dic_add = {username:password}
                user_dic.update(dic_add)

            else:
                print('密码不符合规范')
        else:
            print('该用户已经存在')
    else:
        print('用户名中含有特殊字符，请再次注册')


@wrapper
def f3():
    f3_list = [
        '请选择下面操作',
        '1.进入文章编写',
        '2.选择上传md文件',

    ]
    print('欢迎进入文章页面')
    for i in f3_list :
        print(i)
    choice = input('请输入选项')
    if choice == '1':
        text = input('请开始写文章')
    elif choice == '2':
        print('请写入你的md文件的路径')
    else:
        print('你输入的有误，请重新输入')
@wrapper
def f4():
    print('欢迎进入评论界面，请开始你的评论')
@wrapper
def f5():
    print('欢迎进入日记页面')
@wrapper
def f6():
    print('欢迎进入收藏界面')
@wrapper
def f7():#注销功能
    global isflog#声明全局变量isflog
    global count#声明登陆计数器
    isflog =False #注销功能开启后 则用户下线
    count = 0#刷新登陆次数

# def f8():
#     isflog_circle = False









