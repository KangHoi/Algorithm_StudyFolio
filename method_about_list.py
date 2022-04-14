# -*- coding: cp949 -*-
a = []  # <class 'list'>
a = list()  # <class 'list'>

print(type(a))

a = [1, 2, 3]
print(a)  # [1, 2, 3]

a.append(4)
print(a)  # [1, 2, 3, 4]

a.insert(3, 6)
print(a)  # [1, 2, 3, 6, 4]

a.append('�ȳ�')
a.append(True)
print(a)  # [1, 2, 3, 6, 4, '�ȳ�', True]
print(a[6])  # True
print(type(a[6]))  # <class 'bool'>

print(a[1:3])  # [2, 3]
print(a[:6])  # [1, 2, 3, 6, 4, '�ȳ�']
print(a[4:])  # [4, '�ȳ�', True]

# print(a[9])
# Traceback (most recent call last):
# File "method_about_list.py", line 26, in <module>
#    print(a[9])
#IndexError: list index out of range


try:
    print(a[9])
except IndexError:
    print('�������� �ʴ� �ε���')  # �������� �ʴ� �ε���


print(a)  # [1, 2, 3, 6, 4, '�ȳ�', True]
del a[1]
print(a)  # [1, 2, 3, 6, 4, '�ȳ�', True]
a.remove(3)
print(a)  # [1, 6, 4, '�ȳ�', True]
print(a.pop(3))  # �ȳ�
a.reverse()
print(a)  # [True, 4, 6, 1]