# 637. 二叉树的层平均值.py


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        q, nq = [root], []
        res = []
        while q:
            size = len(q)
            total = 0
            for node in q:
                total += node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            q, nq = nq, []
            res.append(total / size)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
