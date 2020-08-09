# 95. 不同的二叉搜索树 II.py
from functools import lru_cache
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 思路：
# 用dfs找到所有的树
# 当没有用的数字为止
# 只要有可用的数字
# dfs()
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n)

    @lru_cache(None)
    def helper(self, start, end):
        if start > end:
            return [None]
        res = []
        for i in range(start, end + 1):
            left_list = self.helper(start, i - 1)
            right_list = self.helper(i + 1, end)
            for left in left_list:
                for right in right_list:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res


# 以下为自我练习
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        return self.helper(1, n)

    @lru_cache(None)
    def helper(self, l, r):
        if l > r:
            return [None]
        res = []
        for mid in range(l, r + 1):
            for left in self.helper(l, mid - 1):
                for right in self.helper(mid + 1, r):
                    root = TreeNode(mid)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res


def main():
    sol = Solution()
    res = sol.generateTrees(3)
    print(res)
    for t in res:
        print(t.val)


if __name__ == '__main__':
    main()
