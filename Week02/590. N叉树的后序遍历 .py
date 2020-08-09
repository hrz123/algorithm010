"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# 递归的写法
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self._helper(root, res)
        return res

    def _helper(self, root, res):
        if not root:
            return

        for node in root.children:
            self._helper(node, res)
        res.append(root.val)


# 迭代的写法

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        if not root:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            for c in root.children:
                stack.append(c)

        return output[::-1]


# 以下为自我练习
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        # 左右根，根右左
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children)

        return list(reversed(res))


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children)
        return res[::-1]


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self._helper(root, res)
        return res

    def _helper(self, root, res):
        if not root:
            return
        for child in root.children:
            self._helper(child, res)
        res.append(root.val)


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.children:
                stack.extend(root.children)
        return res[::-1]
