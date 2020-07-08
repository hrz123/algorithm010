# 70. 爬楼梯.py
from functools import lru_cache


# 递归
class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# 递归，手动维护缓存
class Solution:
    def __init__(self):
        self.memo = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.memo[n]


# 循环
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        x, y = 1, 2

        for _ in range(n - 2):
            x, y = y, x + y

        return y


def main():
    sol = Solution()
    res = sol.climbStairs(3)
    print(res)


if __name__ == '__main__':
    main()
