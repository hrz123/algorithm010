# 5490. 吃掉 N 个橘子的最少天数.py
from collections import deque
from functools import lru_cache


class Solution:
    def minDays(self, n: int) -> int:
        q = deque([n])
        d = dict()
        d[n] = 0
        while 0 not in d:
            v = q.popleft()
            if v % 3 == 0 and v // 3 not in d:
                d[v // 3] = d[v] + 1
                q.append(v // 3)
            if v % 2 == 0 and v // 2 not in d:
                d[v // 2] = d[v] + 1
                q.append(v // 2)
            if v - 1 not in d:
                d[v - 1] = d[v] + 1
                q.append(v - 1)
        return d[0]


class Solution:
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return 1 + min(self.minDays(n // 2) + n % 2,
                       self.minDays(n // 3) + n % 3)


def main():
    sol = Solution()

    n = 10
    res = sol.minDays(n)
    print(res)
    n = 6
    res = sol.minDays(n)
    print(res)


if __name__ == '__main__':
    main()
