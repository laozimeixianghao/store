import random

import pymysql
con = pymysql.connect(host="localhost",user='root',password='',database='yinghang')

cursor = con.cursor()
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")


#开户逻辑
bankname="狼腾测试猿银行"
#                第一个对应第一个 不是名称对应名称
# def bank_adduser(account,username,password,country,province,street,door,money):
#

#     if  len(bank) >100:
#         return 3
#     if username in bank:#  如变量在容器内执行下面的代码
#         return 2
#     bank[username]={
#         "account":account,#
#         "password":password,
#         "country":country,
#         "province":province,
#         "street":street,
#         "door":door,
#         "money":money,
#         "bank_name":bank_name
#     }

    # return 1




def adduser():#定义了一个方法
    username=input("请输入您的用户名")
    password = input("请输入您的密码")                                                                                    
    print("请输入您的地址")
    country=input("\t\t请输入您的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    money=int(input("请输入您的余额"))
    account=random.randint(10000000,99999999)
    sql = "select count(*) from  zhanghao"  # count(*)  ->  ((25,),)
    cursor.execute(sql)
    data = cursor.fetchall()  # ((56,),)
    if data[0][0] >= 100:
        print("你去别的银行吧")

        # 查询数据库是否存在该用户
        sql1 = "select count(*) from  zhanghao where username = %s"
        param = [username]
        cursor.execute(sql1, param)
        data = cursor.fetchall()  # ((lisi,),)
    if data[0][0] != 0:
            # return 2  # 已存在
            print("开户失败，你别重复")
    else:  # 正常开户：存储到银行 ，插入数据库
        sql2 = "insert into zhanghao values(%s,%s,%s,%s,%s,%s,%s,%s)"
        param = [account, username, password, country, province, street, door, money]
        cursor.execute(sql2, param)
        con.commit()

        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''

        print(info % (username, account, country, province, street, door, money, bankname))
#{'frank': {'account': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 0, 'bank_name': '狼腾测试猿银行'}}
def save():
    username=input("请输入用户名")
    account=int(input("请输入账号"))
    sql = "select count(*) from  zhanghao where username = %s"
    param = [username]
    cursor.execute(sql, param)
    data = cursor.fetchall()  # ((lisi,),)

    if data[0][0] == 0:
    # if username not in  bank.keys():
        print("用户名不存在")


    sql1 = "select count(*) from  zhanghao where account = %s"
    param = [account]
    cursor.execute(sql1, param)
    data = cursor.fetchall()  # ((lisi,),)

    if data[0][0] == 0:
    # if username not in  bank.keys():
        print("账号不存在")


    else:
        money1 = int(input("输入存款款金额"))
        sql = "update zhanghao set money = money + %s where username = %s"
        param = [money1,username]
        cursor.execute(sql,param)
        con.commit()

        sql = "select money from  zhanghao where account = %s"
        param = [account]
        cursor.execute(sql, param)
        data1 = cursor.fetchall()
        print("存款完成,余额为",data1[0][0])




def get():
    username = input("请输入用户名")
    account = int(input("输入账号"))
    password = input("请输入密码")
    money = int(input("请输入取款金额"))
    sql = "select count(*) from  zhanghao where username = %s"
    param = [username]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if data[0][0] == 0:
    # if username not in  bank.keys():
        print("用户名不存在")

    sql1 = "select count(*) from  zhanghao where account = %s and password = %s"
    param = [account,password]
    cursor.execute(sql1, param)
    data = cursor.fetchall()  # ((lisi,),)

    if data[0][0] == 0:
        # if username not in  bank.keys():
        print("密码错误")
    sql1 = "select money from  zhanghao where account = %s and password = %s"
    param = [12664804, 1]
    cursor.execute(sql1, param)
    data1 = cursor.fetchall()
    if data1[0][0]<money:
        print("余额不足")
    else:
        sql = "update zhanghao set money = money - %s where username = %s"
        param = [money, username]
        cursor.execute(sql, param)
        con.commit()

        sql = "select money from  zhanghao where account = %s"
        param = [account]
        cursor.execute(sql, param)
        data1 = cursor.fetchall()

        print("取款完成,余额为",data1[0][0])



def trans():
    username = input("输入转出用户名")
    username1 = input("输入转入用户名")
    account = int(input("输入转出账号"))
    account1 = int(input("输入转入账号"))
    password = input("输入转出账号密码")
    money =int(input("输入转出金额"))

    sql = "select count(*) from  zhanghao where username = %s"
    param = [username]
    cursor.execute(sql, param)
    data = cursor.fetchall()

    if data[0][0] == 0:
        print("转出用户名不存在")

    sql = "select count(*) from  zhanghao where username = %s"
    param = [username1]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if data[0][0] == 0:
        print("转入用户名不存在")

    sql = "select count(*) from  zhanghao where account = %s"
    param = [account]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if data[0][0] == 0:
        print("转出账户不存在")
    sql = "select count(*) from  zhanghao where account = %s"
    param = [account1]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if data[0][0] == 0:
        print("转入账户不存在")
    sql = "select count(*) from  zhanghao where account = %s and password=%s"
    param = [account,password]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if data[0][0] == 0:
        print("密码错误")
    sql = "select money from  zhanghao where account = %s"
    param = [account]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if data[0][0]<money:
        print("余额不足")
    else:
        sql = "update zhanghao set money = money - %s where username = %s"
        param = [money, username]
        cursor.execute(sql, param)
        con.commit()

        sql = "update zhanghao set money = money + %s where username = %s"
        param = [money, username1]
        cursor.execute(sql, param)
        con.commit()

        sql = "select money from  zhanghao where account = %s"
        param = [account]
        cursor.execute(sql, param)
        data = cursor.fetchall()

        sql = "select money from  zhanghao where account = %s"
        param = [account1]
        cursor.execute(sql, param)
        data1 = cursor.fetchall()

        print("转账成功,转出余额：",data[0][0],"转入余额:",data1[0][0])


def find():
    username = input("输入用户名")
    account = int(input("请输入账号"))
    password = input("请输入密码")
    sql = "select count(*) from  zhanghao where username = %s"
    param = [username]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if data[0][0] == 0:
        print("用户名不存在")
    sql = "select count(*) from  zhanghao where account = %s"
    param = [account]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if data[0][0] == 0:
        print("该账号不存在")
    sql = "select count(*) from  zhanghao where account = %s and password=%s"
    param = [account,password]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if data[0][0] == 0:
        print("密码错误")
    else:
        sql = "select * from  zhanghao where account = %s and password=%s"
        param = [account, password]
        cursor.execute(sql, param)
        data = cursor.fetchall()
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username,account,data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],bankname))

while True:
    begin = input("请选择业务")
    if begin =="1":#您输入的业务等于1执行开户操作
        adduser()
    elif begin == "2":
        print(2, "存钱")
        save()

    elif begin == "3":
        print(3, "、取钱")
        get()
    elif begin == "4":
        print(4,"转账")
        trans()
    elif begin == "5":
        find()
    else:
        print(6,"、退出")
        break