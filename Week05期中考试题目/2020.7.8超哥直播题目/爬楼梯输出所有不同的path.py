# 爬楼梯输出所有不同的path.py
from typing import List


# 相邻两步可以相同，同时输出所有路径
class Solution:
    def climbStairs(self, n: int, steps: List[int]) -> List[List[int]]:
        res = []

        def dfs(n, ans):
            if n < 0:
                return
            if n == 0:
                res.append(ans)
                return
            for step in steps:
                dfs(n - step, [step] + ans)

        dfs(n, [])
        return res


# 相邻两步不可以相同，同时输出所有路径
class Solution:
    def climbStairs(self, n: int, steps: List[int]) -> List[List[int]]:
        res = []

        def dfs(n, cur_step, ans):
            if n < 0:
                return
            if n == 0:
                res.append(ans)
                return
            for step in steps:
                if step != cur_step:
                    dfs(n - step, step, [step] + ans)

        dfs(n, 0, [])
        return res


def main():
    n = 4
    steps = [1, 2, 3]

    sol = Solution()
    res = sol.climbStairs(n, steps)
    print(res)


if __name__ == '__main__':
    main()
