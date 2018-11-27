class room():
    area = 35
    lamp_on = True

    def set_bed(self,area):
        print('房间剩余的面积为%d平方米'%area)
        return True

    def __str__(self):
        return "房间内有床"

class bed():
    area = 6

if __name__ == '__main__':
    area = room.area - bed.area
    room1 = room()
    if room1.set_bed(area):
        print(room1)