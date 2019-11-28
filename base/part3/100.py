import math
import time


# 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# 可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。


def test1():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != j) and (i != k) and (j != k):
                    print(i, j, k)


# 一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
# 在10000以内判断，将该数加上100后再开方，加上268后再开方，如果开方后的结果满足如下条件，即是结果
def test2():
    for i in range(10000):
        # 转化为整型值
        x = int(math.sqrt(i + 100))
        y = int(math.sqrt(i + 268))
        if (x * x == i + 100) and (y * y == i + 268):
            print(i)


# 输入三个整数x,y,z，请把这三个数由小到大输出。
# 使用列表的append，sort
def test3():
    nums = []
    for i in range(3):
        num = input("请输入数字")
        nums.append(num)
    nums.sort()
    print(nums)


# 将一个列表的数据复制到另一个列表中。
# 使用[:]
def test4():
    list1 = [1, 2, 3]
    list2 = list1[:]
    print(list2)


# 输出9*9乘法口诀表。
# 分行与列考虑，共9行9列，i控制行，j控制列。
def test5():
    for i in range(1, 10):
        for j in range(1, 10):
            print(str(i) + str(" * ") + str(j) + " = " + str(i * j))


# 暂停一秒输出。
def test6():
    print("暂停一秒>>")
    time.sleep(1)
    print("输出内容")


# 打印1000以内水仙花数
def test7():
    for n in range(100, 1000):
        i = n // 100
        j = n // 10 % 10
        k = n % 10
        if n == i ** 3 + j ** 3 + k ** 3:
            print(n)


# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# 学会分解出每一位数。

def test8():
    x = int(input("请输入一个数:\n"))
    a = x // 10000
    b = x % 10000 // 1000
    c = x % 1000 // 100
    d = x % 100 // 10
    e = x % 10

    if a != 0:
        print("5 位数：", e, d, c, b, a)
    elif b != 0:
        print("4 位数：", e, d, c, b)
    elif c != 0:
        print("3 位数：", e, d, c)
    elif d != 0:
        print("2 位数：", e, d)
    else:
        print("1 位数：", e)


# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
def test9():
    a = int(input("请输入一个数字:\n"))
    x = str(a)
    flag = True

    for i in range(len(x) // 2):
        if x[i] != x[-i - 1]:
            flag = False
            break
    if flag:
        print("%d 是一个回文数!" % a)
    else:
        print("%d 不是一个回文数!" % a)


# 判断下输入的字母是星期几,如果字母相同，再次输入第二个来判断星期几
def test10():
    alpha = input("please input").lower()
    if alpha == "s":
        secAlpha = input("please input second alpha").lower()
        if secAlpha == "u":
            print("Sunday")
        elif secAlpha == "a":
            print("Saturday")
        else:
            print('data error')

    elif alpha == "f":
        print("Friday")

    elif alpha == "m":
        print("monday")

    elif alpha == "t":
        secAlpha = input("please input second alpha").lower()
        if secAlpha == "u":
            print("Tuesday")
        elif secAlpha == "h":
            print("Thursday")
        else:
            print('data error')
    elif alpha == "w":
        print("Wednesday")

    else:
        print('data error')


# 按相反顺序输出列表的值
def test11():
    x = ["a", "b", "c"]
    for i in x[::-1]:
        print(i)


# 字体变色
def test12():
    class Bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    print(Bcolors.FAIL + "变色字体" + Bcolors.ENDC)


# 求输入数字的平方，如果输入数字小于 50 则退出。
def test13():
    def sq(n):
        return int(n) * int(n)

    print("如果输入数字小于 50 则退出")
    canRun = 1
    while canRun:
        n = input("请输入:")
        print(sq(n))
        if int(n) < 50:
            canRun = False
        else:
            canRun = True


# 变量值互换
def test14():
    def exchangeThenPrint(a, b):
        a, b = b, a
        print(a, b)

    exchangeThenPrint(33, 2)

