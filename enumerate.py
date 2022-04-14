a = [1, 2, 3, 2, 45, 2, 5]
print(a)

print(enumerate(a))  # <enumerate object at 0x102dcda40>

print(list(enumerate(a)))  # [(0, 1), (1, 2), (2, 3), (3, 2), (4, 45), (5, 2),(6, 5)]

anum = ['a1', 'b2', 'c3']
for i in range(len(anum)):
    print(i, anum[i])  # 0 a1 | 1 b2 | 2 c3


i = 0
for v in anum:
    print(i, v)
    i += 1  # 0 a1 | 1 b2 | 2 c3


for i, v in enumerate(anum):
    print(i, v)  # 0 a1 | 1 b2 | 2 c3

print(type(enumerate(anum)))  # <class 'enumerate'>
