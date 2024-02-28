from __future__ import annotations
from typing import Tuple
class Dual:

    def __init__(self, real: float, dual: float):
        self.real = real
        self.dual = dual
    def __add__(self, other) -> Dual:
        return Dual(self.real + other.real, self.dual + other.dual)

    def __sub__(self, other) -> Dual:
        return Dual(self.real - other.real, self.dual - other.dual)

    def __mul__(self, other) -> type[Dual]:
        return Dual(self.real * other.real, self.real * other.dual + other.real * self.dual)

    def __repr__(self) -> str:
        return f'real: {self.real}, epsilon: {self.dual}'

    def __truediv__(self, other) -> Dual: 
        return Dual(self.real/other.real,(self.dual *  other.real - self.real * other.dual)/(other.real**2))

    def __neg__(self) -> Dual:
        return Dual(-self.real, -self.dual)
    
    def __pow__(self, pow):
        return Dual(self.real**pow, pow* self.dual *  self.real **(pow-1) ) 
    
