# 900. RLE 迭代器.py
from typing import List


class RLEIterator:

    def __init__(self, A: List[int]):
        self.arr = A
        self.start = 0
        self.size = len(A)

    def next(self, n: int) -> int:
        if not self.arr or self.start >= self.size:
            return -1
        if n <= self.arr[self.start]:
            self.arr[self.start] -= n
            return self.arr[self.start + 1]
        while n > self.arr[self.start]:
            n -= self.arr[self.start]
            self.arr[self.start] = 0
            self.start += 2
            if self.start >= self.size:
                return -1
        self.arr[self.start] -= n
        return self.arr[self.start + 1]


class RLEIterator:

    def __init__(self, A: List[int]):
        self.arr = A
        self.start = 0
        self.size = len(A)

    def next(self, n: int) -> int:
        while self.start < self.size and n > self.arr[self.start]:
            n -= self.arr[self.start]
            self.arr[self.start] = 0
            self.start += 2
        if self.start >= self.size:
            return -1
        self.arr[self.start] -= n
        return self.arr[self.start + 1]


class RLEIterator:
    def __init__(self, A: List[int]):
        self.arr = A
        self.start = 0
        self.size = len(A)

    def next(self, n: int) -> int:
        while self.start < self.size and self.arr[self.start] < n:
            n -= self.arr[self.start]
            self.arr[self.start] = 0
            self.start += 2
        if self.start == self.size:
            return -1
        self.arr[self.start] -= n
        return self.arr[self.start + 1]


def main():
    pass


if __name__ == '__main__':
    main()
