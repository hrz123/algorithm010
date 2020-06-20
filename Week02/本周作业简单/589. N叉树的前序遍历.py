# 589. N叉树的前序遍历.py
from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# 递归
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self._preorfer(root, res)
        return res

    def _preorfer(self, root, res):
        if not root:
            return

        res.append(root.val)
        for child in root.children:
            self._preorfer(child, res)


# 迭代
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            # if not node.children:
            #     continue
            for child in node.children[::-1]:
                stack.append(child)

        return res


def main():
    root = Node(1)
    node = Node(3)
    root.children = [node, Node(2), Node(4)]
    node.children = [Node(5), Node(6)]

    s = Solution()
    res = s.preorder(root)
    print(res)


if __name__ == '__main__':
    main()
