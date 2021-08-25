import random
#                 范围
num=random.randint(0, 5)#   随机一个数字赋值给num
#        这是一个随机数函数   起始值为0     终止值为20000
print(num)#打印一个随机数
x = 100
while 1:
    a = input("请输入一个数字")# 从键盘上输入一个   字符    赋值给a
    x = x-10
    a = int(a)
    if a == num:
        print("你成功了")
        break
    elif x == 0:
        print("你的金币已用完")
        break
    elif a < num:
        print("猜小了")
    elif a > num:
        print("猜大了")
