# 77. 组合.py
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

    def __dfs(self, start, k, n, pre, res):
        # 当前已经找到的组合存储在 pre 中，需要从 start 开始搜索新的元素
        # recursion terminator
        if len(pre) == k:
            res.append(pre[:])
            return

        for i in range(start, n + 1):
            # process current level logic
            pre.append(i)
            # 因为已经把 i 加入到 pre 中，下一轮就从 i + 1 开始
            # 注意和全排列问题的区别，因为按顺序选择，因此无须使用 used 数组
            # drill down
            self.__dfs(i + 1, k, n, pre, res)
            # 回溯的时候，状态重置
            # reverse current level status if needed
            pre.pop()


# 加入剪枝
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 特判
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, pre, res):
        if len(pre) == k:
            res.append(pre[:])
            return

        # 注意：这里 i 的上限是归纳得到的
        for i in range(start, n - (k - len(pre)) + 2):
            pre.append(i)
            self.__dfs(i + 1, k, n, pre, res)
            pre.pop()


# 库函数
from itertools import combinations


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


def main():
    pass


if __name__ == '__main__':
    main()
