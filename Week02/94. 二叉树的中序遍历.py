# 94. 二叉树的中序遍历.py
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归的写法
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


# 迭代的写法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []

        node = root
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right

        return res


def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    res = s.inorderTraversal(root)
    print(res)


if __name__ == '__main__':
    main()
