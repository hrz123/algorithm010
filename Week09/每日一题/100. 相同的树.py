# 100. 相同的树.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not (p and q) or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(
            p.right, q.right)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not (p and q) or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) \
               and self.isSameTree(p.right, q.right)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not (p and q):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) \
               and self.isSameTree(p.right, q.right)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not (p and q):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)


def main():
    pass


if __name__ == '__main__':
    main()
