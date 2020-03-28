import random
print('-'*40)
print('\t欢迎来到王者荣耀')
print('-'*40)
role = input('请选择游戏人物（1.鲁班 2.后羿 3.李白 4.孙尚香）')
coins = 1000
print('欢迎！{}来到王者荣耀，当前金币为：{}'.format(role,coins))
weapons = [['屠龙刀',500],['倚天剑',800],['98k',1000],['鹅毛扇',800],['手榴弹',200],['樱花枪',500]]
weapon_list = []
while True:
    choice = input('请输入：\n1.购买武器\n2.打仗\n3.删除武器\n4.查看武器\n5.退出游戏\n')
    if choice == '1':
        #购买武器
        print('欢迎进入武器库：')
        for weapon in weapons:
            print(weapon[0],weapon[1],sep = '   ')
        #提示输入购买武器

        weaponname = input('请输入要购买的武器')
        if weaponname not in weapon_list: #判断输入武器在不在玩家武器库中
            for weapon in weapons:#判断武器在不在武器库中
                if weaponname == weapon[0]:
                    if coins >= weapon[1]:
                        weapon_list.append(weapon[0])#添加到自己的武器库
                        print('{}购买{}成功'.format(role,weapon[0]))
                        coins -=weapon[1]
                        break
                    else :
                        print('金币不足请去赚钱')
            else:
                print('没有此武器，请重新输入')
        else:
            print('已有此武器武器')
    elif choice =='2':
        #假设你有多个武器
        print('进入战场......')
        #选择武器
        if weapon_list:
            print('{}拥有的武器如下'.format(role))
            for weapon in weapon_list:
                print(weapon)
                while True:
                    weaponname = input('请选择使用那款武器打仗')
                    if weaponname in weapon_list:
                        #进入战争状态 默认与曹操打仗
                        ran1 = random.randint(1,20)#曹操
                        ran2 = random.randint(1,20)#玩家
                        if ran1>ran2:
                            print('张飞胜利！！！')
                            print('张飞攻击力为{}，{}攻击力为{}'.format(ran1,role,ran2))
                        elif ran1<ran2:
                            print('{}胜利'.format(role))
                            coins +=200
                            print('张飞攻击力为{}，{}攻击力为{}，金币为{}'.format(ran1, role, ran2,coins))
                        else:
                            print('此次平局，可以继续打仗')
                    else:
                        print('输入有误，请重新输入')
                    answer = input('是否继续打仗:Y/N').upper()#是否继续进行
                    if answer == 'N':
                        break
                    else:
                        print('请继续打仗')
        else:
            print('没有武器，请前往购买武器')
    elif choice =='3':
        #删除武器
        print('武器太多，很沉，丢几个...')
        if len(weapon_list):
            print('{}拥有的武器如下'.format(role))
            for weapon in weapon_list:
                print(weapon)
            while True:
                weaponname = input('请输入要删除的武器：')
                if weaponname in weapon_list:
                        #删除武器
                        for weapon in weapons:#准备回收 武器

                            if weaponname == weapon[0]:
                                coins += weapon[1]#回收武器成功
                                print('你的金币为：',coins)
                        weapon_list.remove(weaponname)
                        break
                else:
                    print('抱歉，你还没有这个武器')
        else :
            print('没有武器，不可以删除')
    elif choice =='4':
        print('你有{}金币'.format(coins))
        for weapon in weapon_list:
            print('{}拥有{}武器'.format(role,weapon))

    elif choice =='5':
        back =input('确认退出？Y/N').upper()
        if back == 'Y':
            break
    else:
        print('输入有误，请重新输入')