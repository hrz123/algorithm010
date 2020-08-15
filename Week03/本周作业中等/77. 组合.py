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
        # 当前已经找到的组合存储在 pre 中，需要从 start 开始搜索新的元素
        # recursion terminator
        if len(ans) == k:
            res.append(ans[:])
            return

        for i in range(start, n + 1):
            # process current row logic
            ans.append(i)
            # 因为已经把 start 加入到 pre 中，下一轮就从 start + 1 开始
            # 注意和全排列问题的区别，因为按顺序选择，因此无须使用 used 数组
            # drill down
            self.__dfs(i + 1, k, n, ans, res)
            # 回溯的时候，状态重置
            # reverse current row status if needed
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

        # 注意：这里 start 的上限是归纳得到的
        # 比如n=5,k=2,当len(pre)==0时，最大遍历到5-(2-0)+1=4，到5就凑不够两个了
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


# level可用len(pre)代替
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
            res.append(ans)
            return
        for i in range(start, end - (k - level) + 2):
            self.__dfs(i + 1, end, k, ans + [i], res)


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


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n + 1)
                for pre in self.combine(i - 1, k - 1)]


# dfs
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(level, pre):
            if level == k:
                res.append(list(pre))
                return
            start = pre[-1] if pre else 0
            for i in range(start + 1, n + 1):
                if i not in pre:
                    dfs(level + 1, pre + [i])

        dfs(0, [])
        return res


class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n + 1), k))


class Solution:
    def combine(self, n, k):
        if n <= 0 or k <= 0 or k > n:
            return [[]]
        res = []
        self._dfs(1, n, k, [], res)
        return res

    def _dfs(self, start, end, k, ans, res):
        if len(ans) == k:
            res.append(ans)
            return
        for i in range(start, end - (k - len(ans)) + 2):
            self._dfs(i + 1, end, k, ans + [i], res)


# 库函数
# 递归，相当于从t-1个数里选k-1个数再加上这个数，t k..n
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:
            return []
        return list(combinations(range(1, n + 1), k))


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:
            return [[]]

        return [pre + [i] for i in range(k, n + 1) for pre in
                self.combine(i - 1, k - 1)]


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []

        def dfs(level, start, pre):
            if level == k:
                res.append(pre)
                return
            for i in range(start, n - (k - level) + 2):
                dfs(level + 1, i + 1, pre + [i])

        dfs(0, 1, [])
        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:
            return [[]]
        return [pre + [i] for i in range(k, n + 1) for pre in
                self.combine(i - 1, k - 1)]


class Solution:
    def combine(self, n, k):
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in
                     range(1, c[0] if c else n + 1)]
        return combs


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        return [ans + [i] for i in range(k, n + 1)
                for ans in self.combine(i - 1, k - 1)]


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(level, start, pre):
            if level == k:
                res.append(pre)
                return
            for i in range(start, n - k + len(pre) + 2):
                dfs(level + 1, i + 1, pre + [i])

        dfs(0, 1, [])
        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(level, start, pre):
            if level == k:
                res.append(pre)
                return
            for i in range(start, n - k + level + 2):
                dfs(level + 1, i + 1, pre + [i])

        dfs(0, 1, [])
        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        return [ans + [i] for i in range(k, n + 1) for ans in
                self.combine(i - 1, k - 1)]


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(level, start, pre):
            if level == k:
                res.append(pre)
                return
            for i in range(start + 1, n - k + level + 2):
                dfs(level + 1, i, pre + [i])

        dfs(0, 0, [])
        return res


def main():
    n = 4
    k = 2
    sol = Solution()
    res = sol.combine(n, k)
    print(res)


if __name__ == '__main__':
    main()
