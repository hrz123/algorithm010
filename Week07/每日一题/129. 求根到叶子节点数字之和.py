# 129. 求根到叶子节点数字之和.py
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [str(root.val)]
            left = dfs(root.left)
            right = dfs(root.right)
            return [str(root.val) + i for i in left + right]

        return sum(int(i) for i in dfs(root))


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # 计算前面路径为多少时的总和
        def helper(root, i):
            if not root:
                return 0
            res = i * 10 + root.val
            if not root.left and not root.right:
                return res
            return helper(root.left, res) + helper(root.right, res)

        return helper(root, 0)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(root, pre):
            if not root:
                return 0
            res = pre * 10 + root.val
            # 算出该节点的最终表示结果
            if not root.left and not root.right:
                return res
            return helper(root.left, res) + helper(root.right, res)

        return helper(root, 0)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, pre):
            if not root:
                return 0
            res = pre * 10 + root.val
            if not root.left and not root.right:
                return res
            return dfs(root.left, res) + dfs(root.right, res)

        return dfs(root, 0)


class Solution:
    def sumNumbers(selfself, root: TreeNode) -> int:
        def dfs(root, pre):
            if not root:
                return 0
            res = pre * 10 + root.val
            if not root.left and not root.right:
                return res
            return dfs(root.left, res) + dfs(root.right, res)

        return dfs(root, 0)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, pre):
            if not root:
                return 0
            res = pre * 10 + root.val
            if not root.left and not root.right:
                return res
            return dfs(root.left, res) + dfs(root.right, res)

        return dfs(root, 0)


class Solution:
    def sumNumbers(selfself, root: TreeNode) -> int:
        def dfs(root, pre):
            if not root:
                return 0
            res = pre * 10 + root.val
            if not root.left and not root.right:
                return res
            return dfs(root.left, res) + dfs(root.right, res)

        return dfs(root, 0)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, pre):
            if not node:
                return 0
            res = pre * 10 + node.val
            if not node.left and not node.right:
                return res
            return dfs(node.left, res) + dfs(node.right, res)

        return dfs(root, 0)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, pre):
            if not root:
                return 0
            res = pre * 10 + root.val
            if not root.left and not root.right:
                return res
            return dfs(root.left, res) + dfs(root.right, res)

        return dfs(root, 0)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, pre):
            if not root:
                return 0
            res = pre * 10 + root.val
            if not root.left and not root.right:
                return res
            return dfs(root.left, res) + dfs(root.right, res)

        return dfs(root, 0)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, pre):
            if not root:
                return 0
            res = pre * 10 + root.val
            if not root.left and not root.right:
                return res
            return dfs(root.left, res) + dfs(root.right, res)

        return dfs(root, 0)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, pre):
            if not root:
                return 0
            res = pre * 10 + root.val
            if not root.left and not root.right:
                return res
            return dfs(root.left, res) + dfs(root.right, res)

        return dfs(root, 0)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, pre):
            if not root:
                return 0
            res = pre * 10 + root.val
            if not root.left and not root.right:
                return res
            return dfs(root.left, res) + dfs(root.right, res)

        return dfs(root, 0)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, pre):
            if not root:
                return 0
            res = pre * 10 + root.val
            if not root.left and not root.right:
                return res
            return dfs(root.left, res) + dfs(root.right, res)

        return dfs(root, 0)


def main():
    sol = Solution()
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    res = sol.sumNumbers(a)
    print(res)


if __name__ == '__main__':
    main()
