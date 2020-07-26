# 124. 二叉树中的最大路径和.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float("-inf")

        def helper(root):
            nonlocal res
            # recursion terminator
            if not root:
                return 0
            # process current row logic
            # drill down
            # 左边最大值
            left = helper(root.left)
            # 右边最大值
            right = helper(root.right)
            # 和全局变量比较
            res = max(res, left + right + root.val)
            # >0 说明都能使路径变大
            # merge
            return max(0, max(left, right) + root.val)

        helper(root)
        return res


# 以下为自我练习
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')

        def helper(root):
            nonlocal res
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            res = max(res, left + right + root.val)
            return max(0, max(left, right) + root.val)

        helper(root)
        return res


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = root.val

        def helper(root: TreeNode):
            nonlocal res
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            res = max(res, left + right + root.val)
            return max(0, max(left, right) + root.val)

        helper(root)
        return res


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        _max = root.val

        def dfs(root):
            nonlocal _max
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            _max = max(_max, left + right + root.val)
            return max(0, max(left, right) + root.val)

        dfs(root)
        return _max


def main():
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    res = sol.maxPathSum(root)
    print(res)


if __name__ == '__main__':
    main()
