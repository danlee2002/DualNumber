from __future__ import annotations
from typing import Tuple
class Dual:

    def __init__(self, real: float, dual: float):
        self.real = real
        self.dual = dual

    def __add__(self, other):
        return Dual(self.real + other.real, self.dual + other.dual)
    
    def __sub__(self, other):
        return Dual(self.real - other.real, self.dual - other.dual)
    
    def __mul__(self, other):
        return Dual(self.real * other.real, self.real * other.dual + other.real * self.dual)
    

