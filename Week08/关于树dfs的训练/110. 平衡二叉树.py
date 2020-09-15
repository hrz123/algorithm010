# 110. 平衡二叉树.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 暴力法
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)


# 递归返回值：
# 1. 当节点root左右子树的高度差<2：返回以节点root为根节点的子树的最大高度，即节点root的左右
# 子树中最大高度加1（max(left, right) + 1)'
# 2. 当节点root左右子树的高度差>=2:则返回-1，代表此子树不是平衡树。
# 递归终止条件：
# 1.当越过叶子节点时，返回高度0；
# 2.当左右子树高度left==-1时，代表此子树的左右子树不是平衡树，因此直接返回-1.
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            if left == -1:
                return -1
            right = height(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) < 2 else -1

        return height(root) != -1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            if left == -1:
                return -1
            right = height(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) < 2 else -1

        return height(root) != -1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            if left == -1:
                return -1
            right = height(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) < 2 else -1

        return height(root) != -1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            if left == -1:
                return -1
            right = height(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) < 2 else -1

        return height(root) != -1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            if left == -1:
                return -1
            right = height(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) < 2 else -1

        return height(root) != -1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            if left == -1:
                return -1
            right = height(root.right)
            if right == -1:
                return -1
            return -1 if abs(left - right) > 1 else max(left, right) + 1

        return height(root) != -1


def main():
    pass


if __name__ == '__main__':
    main()
