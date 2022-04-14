# -*- coding: cp949 -*-
import collections


a = dict()
a = {}  # <class 'dict'>

print(type(a))

a = {'key1':'value1', 'key2':'value2'}
print(a)  # {'key1': 'value1', 'key2': 'value2'}

a['key3'] = 'value3'
print(a)  # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

print(a['key1']) # value1

# Traceback (most recent call last):
#   File "method_about_dictionary.py", line 13, in <module>
#     print(a['key4'])
# KeyError: 'key4'
# print(a['key4'])

print('key4' in a)  # False

# �������� �ʴ� Ű
if 'key4' in a:
    print('�����ϴ� Ű')
else:
    print('�������� �ʴ� Ű')


# ��ųʸ� �� Ű/���� for �ݺ������ε� ��ȸ ����
# key1 value1
# key2 value2
# key3 value3
for k, v in a.items():
    print(k, v)

del a['key1']
print(a)  # {'key2': 'value2', 'key3': 'value3'}

## dictionary module
b = collections.defaultdict(int)
b['A'] = 5
b['B'] = 4
print(b)  # defaultdict(<class 'int'>, {'A': 5, 'B': 4})

b['C'] += 1  # defaultdict ��ü�� default�� ���� ���� �ٷ� +1 ���� ����
print(b)  # defaultdict(<class 'int'>, {'A': 5, 'B': 4, 'C': 1})

num = [1, 2, 3, 4, 5, 5, 5, 6, 6]
c = collections.Counter(num)
# Counter ��ü(Ű:��) ==> ������ �� : ������ ���� | ������ �ڵ����� �������
print(c)  # Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1}
print(type(c))  # <class 'collections.Counter'>
# most_common : Counter��ü���� ���� �� ���� ���� ��� ���� ����
print(c.most_common(2))  # [(5, 3), (6, 2), (1, 1)]
