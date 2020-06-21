# 145. 二叉树的后序遍历.py
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 迭代
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        # 放入根节点
        stack = [root]

        while stack:
            root = stack.pop()
            # 放入根的值
            res.append(root.val)
            # 先压左子节点入栈
            if root.left:
                stack.append(root.left)
            # 再压右子节点入栈
            if root.right:
                stack.append(root.right)
        # 输出顺序是根右左，从上至下，后序遍历是左右根，从下至上，正好反序输出即可
        return res[::-1]


# 颜色标记法
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((GRAY, node))
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
