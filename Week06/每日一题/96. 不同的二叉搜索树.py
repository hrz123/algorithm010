# 96. 不同的二叉搜索树.py
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        # recursion terminator
        if n <= 1:
            return 1
        # process data
        res = 0
        # conquer
        for i in range(n):
            res += self.numTrees(i) * self.numTrees(n - i - 1)
        # generate final result
        return res


class Solution:
    def __init__(self):
        self.memo = {0: 1, 1: 1}

    def numTrees(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        res = 0
        # conquer
        for i in range(n):
            res += self.numTrees(i) * self.numTrees(n - i - 1)
        self.memo[n] = res
        return self.memo[n]


class Solution:
    def __init__(self):
        self.memo = {0: 1, 1: 1}

    def numTrees(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        res = 0
        # conquer
        for i in range(n // 2):
            res += 2 * self.numTrees(i) * self.numTrees(n - i - 1)
        if n & 1:
            res += self.numTrees(n // 2) * self.numTrees(n // 2)
        self.memo[n] = res
        return self.memo[n]


def main():
    n = 4
    sol = Solution()
    res = sol.numTrees(n)
    print(res)


if __name__ == '__main__':
    main()
