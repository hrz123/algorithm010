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
        # process current row logic
        if level == len(res):
            res.append(node.val)
        else:
            res[level] = max(res[level], node.val)
        # drill down
        self.__dfs(level + 1, node.left, res)
        self.__dfs(level + 1, node.right, res)
        # reverse current row status if needed


# 以下为自我练习
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # bfs
        if not root:
            return []

        q, nq = [root], []
        res = []

        while q:
            level_max = float('-inf')
            for root in q:
                level_max = max(level_max, root.val)
                if root.left:
                    nq.append(root.left)
                if root.right:
                    nq.append(root.right)
            q, nq = nq, []
            res.append(level_max)

        return res


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        deq = deque([root])
        res = []
        while deq:
            size = len(deq)
            _max = float('-inf')
            for _ in range(size):
                root = deq.popleft()
                _max = max(_max, root.val)
                if root.left:
                    deq.append(root.left)
                if root.right:
                    deq.append(root.right)
            res.append(_max)
        return res


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q, nq = [root], []
        res = []
        while q:
            _max_value = float('-inf')
            for root in q:
                _max_value = max(_max_value, root.val)
                if root.left:
                    nq.append(root.left)
                if root.right:
                    nq.append(root.right)
            res.append(_max_value)
            q, nq = nq, []
        return res


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        deq = deque([root])
        res = []
        while deq:
            t = float('-inf')
            for _ in range(len(deq)):
                node = deq.popleft()
                t = max(t, node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            res.append(t)
        return res


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q, nq = [root], []
        res = []
        while q:
            max_value = float('-inf')
            for node in q:
                max_value = max(max_value, node.val)
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            res.append(max_value)
            q, nq = nq, []
        return res


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
