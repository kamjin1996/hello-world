class Point:
    def __init(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point()
pt2 = pt1
pt3 = pt2
print(pt1,pt2,pt3)
del pt1
del pt2
#打开注释将会0引用 生命周期完结 将会执行类的销毁函数
# del pt3
input("继续运行...")

