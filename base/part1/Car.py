# _*_ coding:utf-8 _*_
import time


class Car:
    '我是车'

    def __init__(self):
        self.speed = 0
        self.cmdCount = 0
        self.startTime = ""
        self.stopTime = ""

    def cmdCountIncr(self):
        self.cmdCount += 1
        return self.cmdCount

    def start(self):
        self.startTime = time.asctime(time.localtime(time.time()))
        self.speed = 20
        print("start this car,speed is", self.speed)

    def diver(self):
        self.speed += 50
        print("diver the car,speed is %d" % self.speed)

    def stop(self):
        self.stopTime = time.asctime(time.localtime(time.time()))
        self.speed = 0
        print("stop!,speed is %d" % self.speed)

    def printTime(self):
        print(self.stopTime)
        print(self.startTime)

    def back(self):
        self.__init__()
        print("归还成功！")


if __name__ == '__main__':
    myCar = Car()
    print("I am car!")
    while True:
        action = input("请输入指令让车子运行:[A]Start,[D]Diver,[S]Stop,[P]PrintTime?").upper()
        if action not in "ADSP" or len(action) != 1:
            print("I don know how to do that!")
            continue
        if action == "A":
            myCar.start()
        if action == "D":
            myCar.diver()
        if action == "S":
            myCar.stop()
        if action == "P":
            myCar.printTime()

        print("发动了%d次指令了" % myCar.cmdCountIncr())

        if myCar.cmdCount == 10:
            print("使用了十次车辆，归还车辆...")
            myCar.back()
            break
