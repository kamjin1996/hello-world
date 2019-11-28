
# 字符串
s = "i am str!"
n = 5
# s[:n]+s[n:]=s总是成立的
print(s[:n] + s[n:])

print("%(name)s,%(age)d,%(id)d" % {"name": "小李", "age": 10, "id": 111111})


tran = "".maketrans("abc","023")

print("abcd".translate(tran))