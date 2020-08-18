# 面试题 04.06. 后继者.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root or not p:
            return root
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        left = self.inorderSuccessor(root.left, p)
        return left if left else root


def main():
    pass


if __name__ == '__main__':
    main()
