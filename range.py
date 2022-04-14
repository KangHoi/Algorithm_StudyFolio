# -*- coding: cp949 -*-
import sys

lst = list(range(5))
print(lst)

r = range(5)
print(r)
print(type(r))


for i in range(5):
    print(i)


a = [n for n in range(1000000)]  # 이미 생성된 값이 담겨 있음
b = range(1000000)  # 생성해야 한다는 조건만 존재함
print(len(a))
print(len(b))
print(b)
print(type(a))  # <class 'list'>
print(type(b))  # <class 'range'>
print(sys.getsizeof(a))  # 8697456
print(sys.getsizeof(b))  # 48

print(type(b[1]))
