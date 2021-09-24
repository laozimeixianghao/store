class cook:
    __name=""
    __age=0
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age
    def c(self):
        print(self.__age,'的',self.__name)

    def cooking(self):
        print("蒸饭")

class cehf(cook):
    def fry(self):
        print("炒菜")

class cook1(cehf):
    c=cook()
    c.setname('陈枭')
    c.setage(20)
    c.cooking()
    c.c()



