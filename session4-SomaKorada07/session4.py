import math
import random
import decimal
from decimal import Decimal


class Qualean():
    def __init__(self, real):
        if real not in [-1, 0, 1, 1.0, 0.0, -1.0]:
            raise ValueError('Invalid real number. Should be -1, 0 or 1')
        self.number = round(real * random.uniform(-1, 1), 10)

    def __repr__(self):
        return str(self.number)

    def __str__(self):
        return str(self.number)

    def __eq__(self, other):
        if isinstance(other, Qualean):
            return self.number == other.number
        return self.number == Decimal(other)

    def __ge__(self, other):
        if isinstance(other, Qualean):
            return self.number >= other.number
        return self.number >= Decimal(other)

    def __gt__(self, other):
        if isinstance(other, Qualean):
            return self.number > other.number
        return self.number > Decimal(other)

    def __le__(self, other):
        if isinstance(other, Qualean):
            return self.number <= other.number
        return self.number <= Decimal(other)

    def __lt__(self, other):
        if isinstance(other, Qualean):
            return self.number < other.number
        return self.number < Decimal(other)

    def __add__(self, other):
        if isinstance(other, Qualean):
            return self.number + other.number
        return self.number + Decimal(other)

    def __mul__(self, other):
        if isinstance(other, Qualean):
            return self.number * other.number
        return self.number * Decimal(other)

    def __sqrt__(self):
        decimal.getcontext().prec = 10
        if self.number >= 0:
            return Decimal(self.number).sqrt()
        return '{}i'.format(Decimal(-self.number).sqrt())

    def __bool__(self):
        return bool(self.number)

    def __and__(self, other):
        if not bool(self.number):
            return self.number
        if not isinstance(other, Qualean):
            raise TypeError("Expected type Qualean.")
        return (self.number) and (other.number)

    def __or__(self, other):
        if bool(self.number):
            return self.number
        if not isinstance(other, Qualean):
            raise TypeError("Expected type Qualean.")
        return (self.number) or (other.number)

    def __float__(self):
        return float(self.number)

    def __invertsign__(self):
        self.number = -self.number
        return self
