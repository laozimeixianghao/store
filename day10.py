from threading import Thread

eggshell = 0
import time
class chef(Thread):
    username=""
    count=0

    def run(self) -> None:
        global eggshell
        while True:
            if eggshell == 500:
                print("篮子已满")
                time.sleep(3)
            else:
                self.count = self.count + 1
                eggshell = eggshell + 1
                print(self.username, "做了一个蛋挞！还剩", eggshell)

class consumer(Thread):
    username=""
    money=0
    def run(self) -> None:
        global eggshell
        while True:
            if self.money<=0:
                print("余额不足.................................................")
                break
            if eggshell==0:
                print("蛋挞卖完了，稍等一会儿")
            else:
                self.money=self.money-2
                eggshell = eggshell -1
                print(self.username,"买了一个蛋挞! 还剩",eggshell)

c1 = chef()
c1.username='厨师1号'

c2 = chef()
c2.username='厨师2号'

c3 = chef()
c3.username='厨师3号'

con1=consumer()
con1.username="张三"
con1.money=3000
con2=consumer()
con2.money=3000
con2.username="李四"
con3=consumer()
con3.money=3000
con3.username="王五"

c1.start()
c2.start()
c3.start()
con1.start()
con2.start()
con3.start()