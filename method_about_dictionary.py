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

# 존재하지 않는 키
if 'key4' in a:
    print('존재하는 키')
else:
    print('존재하지 않는 키')


# 딕셔너리 내 키/값은 for 반복문으로도 조회 가능
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

b['C'] += 1  # defaultdict 객체의 default값 에러 없이 바로 +1 연산 가능
print(b)  # defaultdict(<class 'int'>, {'A': 5, 'B': 4, 'C': 1})

num = [1, 2, 3, 4, 5, 5, 5, 6, 6]
c = collections.Counter(num)
# Counter 객체(키:값) ==> 아이템 값 : 아이템 개수 | 개수를 자동으로 계산해줌
print(c)  # Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1}
print(type(c))  # <class 'collections.Counter'>
# most_common : Counter객체에서 가장 빈도 수가 높은 요소 추출 가능
print(c.most_common(2))  # [(5, 3), (6, 2), (1, 1)]
