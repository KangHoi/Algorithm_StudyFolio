# -*- coding: utf-8 -*-
# Generator
# Iteration(������ �ݺ�) ������ ������ �� �ִ� ��ƾ ����

def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n
    return


# print(get_natural_number())
# <generator object get_natural_number at 0x102eaf430>

g = get_natural_number()
for _ in range(0, 100):
    print(next(g))  # 1~100���� ���

# ������ ������ ���� �����⸦ next() �Լ��� �����ϱ�
cube_generator = (e ** 3 for e in range(100000000))
print(next(cube_generator))  # 0
print(next(cube_generator))  # 1
print(next(cube_generator))  # 8
