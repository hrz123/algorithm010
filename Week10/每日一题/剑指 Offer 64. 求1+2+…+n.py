# 剑指 Offer 64. 求1+2+…+m.py
from functools import reduce


class Solution:
    def sumNums(self, n: int) -> int:
        return (n ** 2 + n) >> 1


class Solution:
    def sumNums(self, n: int) -> int:
        return reduce(
            lambda acc, x: acc + x,
            range(1, n + 1)
        )


def main():
    sol = Solution()
    n = 3
    res = sol.sumNums(n)
    print(res)


if __name__ == '__main__':
    main()
