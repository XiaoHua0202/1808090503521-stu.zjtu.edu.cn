'''
这是一个仿博客园系统

'''
import module #导入同文件的自定义模块
isflog_circle = True
while isflog_circle:
    welcome_list = [
        '欢迎进入博客园系统',
        '1.请登录',
        '2.请注册',
        '3.进入文章页面',
        '4.进入评论界面',
        '5.进入日记界面',
        '6.进入收藏页面',
        '7.注销账号',
        '8.退出整个程序',

        ]
    for i in welcome_list:#打印选项列表
        print(i)

    choice_user = input('请选择你的操作')

    def exit():#定义函数登陆三次不成功就退出程序
        global isflog_circle
        if module.count >3:
            isflog_circle = False

    def judge():#定义一个选项调用模块
        if choice_user == '1':
            # global isflog_circle
            exit()
            module.f1()

        elif choice_user == '2':
            exit()
            module.f2()
        elif choice_user == '3':
            exit()
            module.f3()
        elif choice_user == '4':
            exit()

            module.f4()
        elif choice_user == '5':
            exit()
            module.f5()
        elif choice_user == '6':
            exit()
            module.f6()
        elif choice_user == '7':
            exit()
            module.f7()
        elif choice_user == '8':
                global isflog_circle
                isflog_circle = False

        else :
                print('你输入有误，请重新输入')

    judge()#调用定义选项函数


