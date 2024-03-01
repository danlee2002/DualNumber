from __future__ import annotations

from typing import Tuple
class Dual:
    def __init__(self, real: float, dual: float):
        self.real = real
        self.dual = dual
        self.grad =
        self._forward = lambda: None

    def __add__(self, other) -> Dual:
        def _forward():
            ...
        return Dual(self.real + other.real, self.dual + other.dual)

    def __sub__(self, other) -> Dual:
        def _forward():
            ...
        return Dual(self.real - other.real, self.dual - other.dual)

    def __mul__(self, other) -> Dual: 
        def _forward():
            ...
        return Dual(self.real * other.real, self.real * other.dual + other.real * self.dual)

    def __repr__(self) -> str:
        def _forward():
            ...
        return f'real: {self.real}, epsilon: {self.dual}'

    def __truediv__(self, other) -> Dual: 
        def _forward():
            ...
        return Dual(self.real/other.real,(self.dual *  other.real - self.real * other.dual)/(other.real**2))

    def __neg__(self) -> Dual:
        def _forward():
            ...
        return Dual(-self.real, -self.dual)
    
    def __pow__(self, pow):
        def _forward():
            ...
        return Dual(self.real**pow, pow* self.dual *  self.real **(pow-1) ) 
   

