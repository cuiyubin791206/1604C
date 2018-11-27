import random
import time

class Kaodigua():

    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = '生的'
        self.condiments = ''

    def cook(self):
        num = random.randrange(0,1200)//100
        time.sleep(num)
        self.cookedLevel = num
        # self.cookedLevel = 7
        if self.cookedLevel<=3:
            self.cookedString = '是生的'
        elif self.cookedLevel<=5:
            self.cookedString = '是半生不熟的'
        elif self.cookedLevel<=8:
            self.cookedString = '已经烤好了'
        else:
            self.cookedString = '已经烤成木炭了!'

    def addCondiments(self, stuff):
        self.condiments = stuff

    def __str__(self):
        return "用%s为佐料烤地瓜，地瓜%s"%(self.condiments,self.cookedString)

if __name__ == '__main__':
    kdg = Kaodigua()
    kdg.addCondiments('番茄酱')
    kdg.cook()
    print(kdg)