# 爬楼梯输出所有不同的path.py
from functools import lru_cache
from typing import List


# 相邻两步可以相同，同时输出所有路径
class Solution:
    def climbStairs(self, n: int, steps: List[int]) -> List[List[int]]:
        res = []

        @lru_cache(None)
        def dfs(n, ans):
            if n == 0:
                res.append(ans)
                return
            for step in steps:
                if n >= step:
                    dfs(n - step, (step,) + ans)

        dfs(n, ())
        return [list(e) for e in res]


# 相邻两步不可以相同，同时输出所有路径
class Solution:
    def climbStairs(self, n: int, steps: List[int]) -> List[List[int]]:
        res = []

        @lru_cache(None)
        def dfs(n, ans):
            if n == 0:
                res.append(ans)
                return
            for step in steps:
                if (not ans or step != ans[0]) and n >= step:
                    dfs(n - step, (step,) + ans)

        dfs(n, ())
        return [list(e) for e in res]


# class Solution:
#     def climbStairs(self, n: int) -> List[List[int]]:
#
#         a = [[1]]
#         b = [[1, 1], [2]]
#         if n == 1:
#             return a
#         if n == 2:
#             return b
#
#         for i in range(n - 2):
#             a, b = b, [e + [2] for e in a] + [e + [1] for e in b]
#         return b


class Solution:
    def climbStairs(self, n: int, steps: List[int]) -> List[List[int]]:
        res = []
        self.__dfs(n, steps, [], res)
        return res

    def __dfs(self, n, steps, pre, res):
        if n == 0:
            res.append(pre)
            return

        for s in steps:
            if n >= s:
                self.__dfs(n - s, steps, [s] + pre, res)


class Solution:
    def climbStairs(self, n: int, steps: List[int]) -> List[List[int]]:
        res = []
        self.__dfs(n, steps, [], res)
        return res

    def __dfs(self, n, steps, pre, res):
        if n == 0:
            res.append(pre)
            return

        for s in steps:
            if n >= s and (not pre or pre[0] != s):
                self.__dfs(n - s, steps, [s] + pre, res)


def main():
    n = 3
    steps = [1, 2, 3]

    sol = Solution()
    res = sol.climbStairs(n, steps)
    print(res)

    # sol = Solution()
    # res = sol.climbStairs(4)
    # print(res)


if __name__ == '__main__':
    main()
