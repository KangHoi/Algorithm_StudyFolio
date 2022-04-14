# -*- coding: utf-8 -*-
# Generator
# Iteration(루프의 반복) 동작을 제어할 수 있는 루틴 형태

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
    print(next(g))  # 1~100까지 출력

# 생성기 식으로 만든 생성기를 next() 함수로 실행하기
cube_generator = (e ** 3 for e in range(100000000))
print(next(cube_generator))  # 0
print(next(cube_generator))  # 1
print(next(cube_generator))  # 8
