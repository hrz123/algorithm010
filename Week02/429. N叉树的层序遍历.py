# 429. N叉树的层序遍历.py
from collections import deque
from typing import List

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        deq = deque()

        deq.append(root)

        while deq:
            size = len(deq)
            output = []
            for _ in range(size):
                node = deq.popleft()
                output.append(node.val)
                for child in node.children:
                    deq.append(child)

            res.append(output)

        return res


def main():
    pass


if __name__ == '__main__':
    main()
