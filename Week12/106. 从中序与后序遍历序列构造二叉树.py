# 106. 从中序与后序遍历序列构造二叉树.py
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder[-1] != stop:
                root = TreeNode(postorder.pop())
                root.right = build(root.val)
                inorder.pop()
                root.left = build(stop)
                return root

        inorder.insert(0, None)
        return build(None)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder[-1] != stop:
                root = TreeNode(postorder.pop())
                root.right = build(root.val)
                inorder.pop()
                root.left = build(stop)
                return root

        inorder.insert(0, None)
        return build(None)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder[-1] != stop:
                root = TreeNode(postorder.pop())
                root.right = build(root.val)
                inorder.pop()
                root.left = build(stop)
                return root

        inorder.insert(0, None)
        return build(None)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder[-1] != stop:
                root = TreeNode(postorder.pop())
                root.right = build(root.val)
                inorder.pop()
                root.left = build(stop)
                return root

        inorder.insert(0, None)
        return build(None)


def main():
    pass


if __name__ == '__main__':
    main()
