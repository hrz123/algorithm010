# 543. 二叉树的直径.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 直径等于
# max(左边的最大直径，右边的最大直径，root.val + 左侧的深度 + 右侧的深度)
# 我们要构造的函数是
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def _max_depth(root):
            nonlocal res
            if not root:
                return 0
            left = _max_depth(root.left)
            right = _max_depth(root.right)
            res = max(res, left + right)
            return max(left, right) + 1

        _max_depth(root)
        return res


# 以下为自我练习
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return max(left, right) + 1

        dfs(root)
        return res


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0
            nonlocal res
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return max(left, right) + 1

        dfs(root)
        return res


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            nonlocal res
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return max(left, right) + 1

        res = 0
        dfs(root)
        return res


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def dfs(node):
            if not node:
                return 0
            nonlocal res
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right)
            return max(left, right) + 1

        dfs(root)
        return res


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res
            res = max(res, left + right)
            return max(left, right) + 1

        dfs(root)
        return res


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res
            res = max(res, left + right)
            return max(left, right) + 1

        dfs(root)
        return res


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res
            res = max(res, left + right)
            return max(left, right) + 1

        dfs(root)
        return res


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res
            res = max(res, left + right)
            return max(left, right) + 1

        dfs(root)
        return res


def main():
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    res = sol.diameterOfBinaryTree(root)
    print(res)


if __name__ == '__main__':
    main()
