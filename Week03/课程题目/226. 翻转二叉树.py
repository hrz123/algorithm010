# 226. 翻转二叉树.py

# Definition for a binary tree node.
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


def main():
    pass


if __name__ == '__main__':
    main()
