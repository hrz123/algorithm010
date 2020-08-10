# 5486. 切棍子的最小成本.py
from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        import sys
        sys.setrecursionlimit(10000000)

        import functools
        @functools.lru_cache(None)
        def dp(i, j):
            res = float('inf')
            for c in cuts:
                if c > i and c < j:
                    res = min(res, dp(i, c) + dp(c, j) + j - i)
            if res == float('inf'):
                return 0
            return res

        return dp(0, n)


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        import sys
        sys.setrecursionlimit(10000000)

        import functools
        @functools.lru_cache(None)
        def dp(i, j):
            res = float('inf')
            for c in cuts:
                if i < c < j:
                    res = min(res, dp(i, c) + dp(c, j) + j - i)
            if res == float('inf'):
                return 0
            return res

        return dp(0, n)


# 以下为自我练习
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        import sys
        sys.setrecursionlimit(10000000)

        import functools
        @functools.lru_cache(None)
        def dp(i, j):
            res = float('inf')
            for c in cuts:
                if i < c < j:
                    res = min(res, dp(i, c) + dp(c, j) + j - i)
            if res == float('inf'):
                return 0
            return res

        return dp(0, n)


def main():
    sol = Solution()
    n = 7
    cuts = [1, 3, 4, 5]
    res = sol.minCost(n, cuts)
    print(res)

    n = 9
    cuts = [5, 6, 1, 4, 2]
    res = sol.minCost(n, cuts)
    print(res)

    n = 30
    cuts = [18, 15, 13, 7, 5, 26, 25, 29]
    res = sol.minCost(n, cuts)
    print(res)


if __name__ == '__main__':
    main()
