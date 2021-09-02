import random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank={}#创建一个空的字典

#开户逻辑
bank_name="狼腾测试猿银行"
#                第一个对应第一个 不是名称对应名称
def bank_adduser(account,username,password,country,province,street,door,money):
    if  len(bank) >100:
        return 3
    if username in bank:#  如变量在容器内执行下面的代码
        return 2
    bank[username]={
        "account":account,#
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "bank_name":bank_name
    }
    return 1
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
    stast=bank_adduser(account,username,password,country,province,street,door,money)
    #        调用方法   （元素，，，，，，，，，）
    if stast ==3 :
        print("你去别的银行吧")
    elif stast== 2:
        print("开户失败，你别重复")
    elif stast== 1:
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
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
#{'frank': {'account': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 0, 'bank_name': '狼腾测试猿银行'}}
def save():
    username=input("请输入用户名")
    account=int(input("输入账号"))
    if  account == bank[username]["account"]:
        money = int(input("输入存款金额"))
        bank[username]["money"]+=money
        a = bank[username]["money"]
        print(a)
    else:
        print("账号不存在")

def get():
    username = input("请输入用户名")
    account = int(input("输入账号"))
    passworl = input("请输入密码")
    money = int(input("请输入取款金额"))
    if account != bank[username]["account"]:
        print("账号不存在")
    elif passworl != bank[username]["password"]:
        print("密码错误")
    elif money > bank[username]["money"]:
        print("余额不足")
    else:
        a = bank[username]["money"]-money
        print(a)


def trans():
    username = input("输入转出用户名")
    username1 = input("输入转入用户名")
    account = int(input("输入转出账号"))
    account1 = int(input("输入转入账号"))
    password = input("输入转出账号密码")
    money = int(input("输入转出金额"))
    if account != bank[username]["account"]:
        print("转出用户不存在")
    elif account1 != bank[username1]["account"]:
        print("转入用户不存在")
    elif password != bank[username]["password"]:
        print("密码错误")
    elif money > bank[username]["money"]:
        print("余额不足")
    else:
        bank[username]["money"] -= money
        bank[username1]["money"] += money
        a=bank[username]["money"]
        b=bank[username1]["money"]
        print(a,b)

def find():
    username = input("输入用户名")
    account = int(input("请输入账号"))
    password = input("请输入密码")
    if account != bank[username]["account"]:
        print("用户不存在")
    elif password != bank[username]["password"]:
        print("密码错误")
    else:
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
        print(info % (username, account,bank[username]["country"],bank[username]["province"] , bank[username]["street"],bank[username]["door"] , bank[username]["money"], bank_name))

while True:
    begin = input("请选择业务")
    if begin =="1":#您输入的业务等于1执行开户操作
        adduser()
    elif begin == "2":
        save()
        # print(2,"存钱")
    elif begin == "3":
        get()
        # print(3,"、存钱")
    elif begin == "4":
        trans()
    elif begin == "5":
        find()
    else:
        print(6,"、退出")
        break
