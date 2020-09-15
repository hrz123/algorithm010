# 组合数.py
import math


def combine(m, n):
    return math.factorial(m) // (math.factorial(n) * math.factorial(m - n))


def combine(m, n):
    return math.factorial(m) // math.factorial(n) // math.factorial(m - n)


def main():
    print(combine(0, 0))
    print(math.factorial(0))
    print(math.factorial(2))
    print(combine(3, 2))


if __name__ == '__main__':
    main()
