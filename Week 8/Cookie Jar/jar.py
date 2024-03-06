import sys

class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Invalid number.")
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return '🍪' * self.cookies

    def deposit(self, n):
        if self.cookies + n > self._capacity:
            raise ValueError("Deposit exceeds jar capacity.")
        else:
            self.cookies += n


    def withdraw(self, n):
        if self.cookies < n:
            raise ValueError('Invalid Number')
        else:
            self.cookies -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
