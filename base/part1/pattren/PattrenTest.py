import re

value = "A12BZ2X546CMK678678S9AM";


# 匹配到数字则数字*2，返回新的字符串
def regNumMultiply2(value):
    reg = re.compile("[0-9]", re.I | re.M)
    newValue = ""
    for i in value:
        m = reg.match(i)
        if m:
            newValue += str(int(i) * 2)
        else:
            newValue += i
    return newValue


print(regNumMultiply2(value))
