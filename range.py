# -*- coding: cp949 -*-
import sys

lst = list(range(5))
print(lst)

r = range(5)
print(r)
print(type(r))


for i in range(5):
    print(i)


a = [n for n in range(1000000)]  # �̹� ������ ���� ��� ����
b = range(1000000)  # �����ؾ� �Ѵٴ� ���Ǹ� ������
print(len(a))
print(len(b))
print(b)
print(type(a))  # <class 'list'>
print(type(b))  # <class 'range'>
print(sys.getsizeof(a))  # 8697456
print(sys.getsizeof(b))  # 48

print(type(b[1]))
