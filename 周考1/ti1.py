import time
import random
class kaodigua():

    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = '地瓜是生的'
        self.condiments = ''

    def cook(self):
        t1 = random.randrange(0,1000)//100
        print("烤地瓜的时间%d"%t1)
        time.sleep(t1)
        self.cookedLevel = t1
        # self.cookedLevel = 1

    def addCondiments(self,stuff):
        self.condiments = stuff

    def __str__(self):

        if self.cookedLevel<=3:
            return "用%s做为配料，烤的地瓜还是生的"%self.condiments
        elif self.cookedLevel<=5:
            return "用%s做为配料，烤的地瓜半生不熟"%self.condiments
        elif self.cookedLevel <= 8:
            return "用%s做为配料，烤的地瓜已经烤好了"%self.condiments
        else:
            return "用%s做为配料，烤的地瓜已经烤成木炭了"%self.condiments

if __name__ == '__main__':
    kdg = kaodigua()
    kdg.addCondiments("芥末酱")
    kdg.cook()
    print(kdg)