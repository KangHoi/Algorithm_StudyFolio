# -*- coding: cp949 -*-
from dataclasses import dataclass


@dataclass  # @: ���ڷ��̼�
class Product:
    weight: int = None
    price: float = None


apple = Product()
apple.price = 10
print(apple)  # Product(weight=None, price=10)
