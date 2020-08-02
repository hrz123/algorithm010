# 700. 二叉搜索树中的搜索.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        return self.searchBST(root.left, val) if val < root.val else \
            self.searchBST(root.right, val)


def main():
    pass


if __name__ == '__main__':
    main()
