# 94. 二叉树的中序遍历.py
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self._helper(root, res)
        return res

    def _helper(self, node: TreeNode, res: List[int]) -> None:
        if not node:
            return

        self._helper(node.left, res)
        res.append(node.val)
        self._helper(node.right, res)


def main():
    pass


if __name__ == '__main__':
    main()
