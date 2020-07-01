# 515. 在每个树行中找最大值.py
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# bfs
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []

        deq = deque()
        deq.append(root)

        while deq:
            size = len(deq)
            largest = float('-inf')
            for _ in range(size):
                node = deq.popleft()
                largest = max(largest, node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            res.append(largest)

        return res


# dfs
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        self.__dfs(0, root, res)
        return res

    def __dfs(self, level, node, res):
        # recursion terminator
        if not node:
            return
        # process current level logic
        if level == len(res):
            res.append(node.val)
        else:
            res[level] = max(res[level], node.val)
        # drill down
        self.__dfs(level + 1, node.left, res)
        self.__dfs(level + 1, node.right, res)
        # reverse current level status if needed


def main():
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(9)

    sol = Solution()
    res = sol.largestValues(root)
    print(res)


if __name__ == '__main__':
    main()
