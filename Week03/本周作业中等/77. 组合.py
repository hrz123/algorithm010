# 77. 组合.py
from itertools import combinations
from typing import List


# 和全排列问题一样，这是一道使用回溯算法解决的经典问题。
# 而分析回溯问题，我们常常需要画图来帮助我们理清思路和寻找边界条件。
# 见77.组合.png
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 先把不符合条件的情况去掉
        if n <= 0 or k <= 0 or k > n:
            return []

        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, ans, res):
        # 当前已经找到的组合存储在 ans 中，需要从 start 开始搜索新的元素
        # recursion terminator
        if len(ans) == k:
            res.append(ans[:])
            return

        for i in range(start, n + 1):
            # process current level logic
            ans.append(i)
            # 因为已经把 i 加入到 ans 中，下一轮就从 i + 1 开始
            # 注意和全排列问题的区别，因为按顺序选择，因此无须使用 used 数组
            # drill down
            self.__dfs(i + 1, k, n, ans, res)
            # 回溯的时候，状态重置
            # reverse current level status if needed
            ans.pop()


# 加入剪枝
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 特判
        if n <= 0 or k <= 0 or k > n:
            return []

        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, ans, res):
        if len(ans) == k:
            res.append(ans[:])
            return

        # 注意：这里 i 的上限是归纳得到的
        # 比如n=5,k=2,当len(ans)==0时，最大遍历到5-(2-0)+1=4，到5就凑不够两个了
        for i in range(start, n - (k - len(ans)) + 2):
            ans.append(i)
            self.__dfs(i + 1, k, n, ans, res)
            ans.pop()


# 库函数（python提供了库函数）
class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n + 1), k))


# 递归
class Solution:
    def combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n + 1) for pre in
                self.combine(i - 1, k - 1)]


# 二刷
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:
            return []

        res = []
        self.__dfs(0, 1, n, k, [], res)
        return res

    def __dfs(self, level, start, end, k, ans, res):
        if level == k:
            res.append(ans.copy())
            return
        for i in range(start, end - (k - level) + 2):
            ans.append(i)
            self.__dfs(level + 1, i + 1, end, k, ans, res)
            ans.pop()


# level可用len(ans)代替
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:
            return []

        res = []
        self.__dfs(1, n, k, [], res)
        return res

    def __dfs(self, start, end, k, ans, res):
        level = len(ans)
        if level == k:
            res.append(ans.copy())
            return
        for i in range(start, end - (k - level) + 2):
            ans.append(i)
            self.__dfs(i + 1, end, k, ans, res)
            ans.pop()


# 以下为自我练习
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(start, ans):
            if len(ans) == k:
                res.append(ans)
                return
            for i in range(start + 1, n + 1):
                dfs(i, ans + [i])

        dfs(0, [])

        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n + 1) for pre in
                self.combine(i - 1, k - 1)]


def main():
    n = 4
    k = 2
    sol = Solution()
    res = sol.combine(n, k)
    print(res)


if __name__ == '__main__':
    main()
