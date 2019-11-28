# _*_coding:utf-8_*_
try:
    with open("D:/test.txt", "r+",encoding="utf-8") as file:
        print(file.read(10))
finally:
    file.close()
