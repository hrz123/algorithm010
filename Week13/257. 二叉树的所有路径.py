# 257. 二叉树的所有路径.py


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        return [str(root.val) + "->" + ans
                for ans in self.binaryTreePaths(root.left) +
                self.binaryTreePaths(root.right)]


def main():
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    res = sol.binaryTreePaths(root)
    print(res)


if __name__ == '__main__':
    main()
