# -*- coding: utf-8 -*-

# 리스트 출력 시, join()으로 묶어서 처리
a = ['A', 'B']
print(' '.join(a))  # A B

idx = 1
fruit = "APPLE"
print('{0}: {1}'.format(idx + 1, fruit))  # 2: APPLE
print(f'{idx + 1}: {fruit}')  # 2: APPLE
