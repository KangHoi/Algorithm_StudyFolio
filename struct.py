# -*- coding: cp949 -*-
from dataclasses import dataclass


@dataclass  # @: 데코레이션
class Product:
    weight: int = None
    price: float = None


apple = Product()
apple.price = 10
print(apple)  # Product(weight=None, price=10)
