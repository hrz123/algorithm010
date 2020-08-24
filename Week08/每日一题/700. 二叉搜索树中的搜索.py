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


# 以下为自我练习
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        return self.searchBST(root.left, val) if val < root.val else \
            self.searchBST(root.right, val)


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        return self.searchBST(root.left, val) if val < root.val else \
            self.searchBST(root.right, val)


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left
            else:
                return root
        return root


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return root


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            if root.val < val:
                root = root.right
            else:
                root = root.left
        return root


def main():
    pass


if __name__ == '__main__':
    main()
