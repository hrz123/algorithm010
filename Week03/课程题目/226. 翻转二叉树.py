# 226. 翻转二叉树.py

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # recursion terminator
        if not root:
            return

        # process current level logic
        # drill down
        # 这里要同时赋值，否则要用一个tmp变量，存储中间结果
        root.left, root.right = self.invertTree(root.right), self.invertTree(
            root.left)

        return root


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(
            root.left)
        return root


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # recursion terminator
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(
            root.left)
        return root


def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    def level_print(root):
        deq = deque([root])
        while deq:
            size = len(deq)
            for _ in range(size):
                root = deq.popleft()
                print(root.val, end=" ")
                if root.left:
                    deq.append(root.left)
                if root.right:
                    deq.append(root.right)
            print()

    level_print(root)

    sol = Solution()
    root = sol.invertTree(root)
    level_print(root)


if __name__ == '__main__':
    main()
