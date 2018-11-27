
class Fang():
    def __init__(self):
        self.area = 35
        self.lamp_on = True

    def set_chuang(self,c_a):
        print("房间剩余面积%d" % c_a)
        return True

    def __str__(self):
        return "房间内有个床"


class Chuang():
    def __init__(self):
        self.area = 6

if __name__ == '__main__':
    fang1 = Fang()
    chuang1 = Chuang()
    c_a = fang1.area - chuang1.area
    if fang1.set_chuang(c_a):
        print(fang1)