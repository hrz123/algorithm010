# 894. 所有可能的满二叉树.py
# Definition for a binary tree node.
from functools import lru_cache
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @lru_cache(None)
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N == 1:
            return [TreeNode(0)]
        res = []
        for i in range(1, N, 2):
            nLeft = i
            nRight = N - 1 - i
            for left in self.allPossibleFBT(nLeft):
                for right in self.allPossibleFBT(nRight):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)

        return res


# 以下为自我练习
class Solution:
    @lru_cache(None)
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N == 1:
            return [TreeNode(0)]
        res = []
        for i in range(1, N, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N - i - 1):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res


class Solution:
    memo = {1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N in self.memo:
            return self.memo[N]
        res = []
        for i in range(1, N, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N - i - 1):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        self.memo[N] = res
        return self.memo[N]


class Solution:
    memo = {1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N in self.memo:
            return self.memo[N]
        res = []
        for i in range(1, N, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N - i - 1):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        self.memo[N] = res
        return self.memo[N]


class Solution:
    memo = {1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N in self.memo:
            return self.memo[N]
        res = []
        for i in range(1, N, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N - i - 1):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        self.memo[N] = res
        return res


class Solution:
    memo = {1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N in self.memo:
            return self.memo[N]
        res = []
        for i in range(1, N, 2):
            for l in self.allPossibleFBT(i):
                for r in self.allPossibleFBT(N - i - 1):
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    res.append(root)
        self.memo[N] = res
        return res


def main():
    s = Solution()

    res = s.allPossibleFBT(7)
    print(res)

    res = s.allPossibleFBT(6)
    print(res)


if __name__ == '__main__':
    main()
