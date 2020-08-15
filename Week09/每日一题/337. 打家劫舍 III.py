# 337. 打家劫舍 III.py
from functools import lru_cache


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @lru_cache(None)
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.rob(root.left)
        right = self.rob(root.right)
        ll = lr = rl = rr = 0
        # 保证根左右子节点不偷
        if root.left:
            ll, lr = self.rob(root.left.left), self.rob(root.left.right)
        if root.right:
            rl, rr = self.rob(root.right.left), self.rob(root.right.right)
        return max(left + right, ll + lr + rl + rr + root.val)


class Solution:
    memo = {}

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]
        left = self.rob(root.left)
        right = self.rob(root.right)
        ll = lr = rl = rr = 0
        # 保证根左右子节点不偷
        if root.left:
            ll, lr = self.rob(root.left.left), self.rob(root.left.right)
        if root.right:
            rl, rr = self.rob(root.right.left), self.rob(root.right.right)
        self.memo[root] = max(left + right, ll + lr + rl + rr + root.val)
        return self.memo[root]


# 每个节点返回两个值，List，0表示不偷这个节点时的最大收益，1表示投这个节点的最大收益
# root[0] = Math.max(rob(root.l)[0], rob(root.l)[1]) +
# Math.max(rob(root.r)[0], rob(root.r)[1])
# root[1] = rob(root.l)[0] + rob(root.r)[0] + root.val;
class Solution:

    def rob(self, root: TreeNode) -> int:
        return max(self.robHelper(root))

    def robHelper(self, root):
        if not root:
            return [0, 0]
        left = self.robHelper(root.left)
        right = self.robHelper(root.right)
        res = [0, 0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = left[0] + right[0] + root.val
        return res


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.rob_helper(root))

    def rob_helper(self, root):
        if not root:
            return [0, 0]
        left = self.rob_helper(root.left)
        right = self.rob_helper(root.right)
        res = [0, 0]
        res[0] = max(left) + max(right)
        res[1] = left[0] + right[0] + root.val
        return res


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.helper(root))

    def helper(self, root):
        if not root:
            return [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        res = [0, 0]
        res[0] = max(left) + max(right)
        res[1] = left[0] + right[0] + root.val
        return res


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.helper(root))

    def helper(self, root):
        if not root:
            return [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        res = [0, 0]
        res[0] = max(left) + max(right)
        res[1] = root.val + left[0] + right[0]
        return res


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.helper(root))

    def helper(self, root):
        if not root:
            return [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        return [max(left) + max(right), root.val + left[0] + right[0]]


def main():
    sol = Solution()

    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(1)
    root.left.right = TreeNode(3)

    res = sol.rob(root)
    print(res)

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    res = sol.rob(root)
    print(res)


if __name__ == '__main__':
    main()
