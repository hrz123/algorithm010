# 1339. 分裂二叉树的最大乘积.py


# Definition for a binary tree node.
import bisect


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        sum_list = []

        def dfs(root):
            if not root:
                return 0
            res = root.val + dfs(root.left) + dfs(root.right)
            sum_list.append(res)
            return res

        mod = 10 ** 9 + 7
        total = dfs(root)
        sum_list.sort()
        loc = bisect.bisect_left(sum_list, total >> 1)
        ans = max(sum_list[loc] * (total - sum_list[loc]), sum_list[loc - 1] *
                  (total - sum_list[loc - 1]))
        return ans % mod


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        totals = []

        def dfs(root):
            if not root:
                return 0
            ans = root.val + dfs(root.left) + dfs(root.right)
            totals.append(ans)
            return ans

        total = dfs(root)
        totals.sort()
        loc = bisect.bisect_left(totals, total >> 1)
        c1, c2 = totals[loc - 1], totals[loc]
        return max(c1 * (total - c1), c2 * (total - c2)) % (10 ** 9 + 7)


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        totals = []

        def dfs(root):
            if not root:
                return 0
            ans = dfs(root.left) + dfs(root.right) + root.val
            totals.append(ans)
            return ans

        total = dfs(root)
        totals.sort()
        loc = bisect.bisect_left(totals, total >> 1)
        c1, c2 = totals[loc - 1], totals[loc]
        return max(c1 * (total - c1), c2 * (total - c2)) % (10 ** 9 + 7)


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        sums_lists = []

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            ans = left + right + root.val
            sums_lists.append(ans)
            return ans

        total = dfs(root)
        sums_lists.sort()
        loc = bisect.bisect_left(total >> 1)
        l, r = sums_lists[loc - 1], sums_lists[loc]
        return max(l * (total - l), r * (total - r)) % (10 ** 9 + 7)


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        sums_list = []

        def dfs(root):
            if not root:
                return 0
            res = dfs(root.left) + dfs(root.right) + root.val
            sums_list.append(res)
            return res

        total = dfs(root)
        sums_list.sort()
        loc = bisect.bisect_left(sums_list, total >> 1)
        l, r = sums_list[loc - 1], sums_list[loc]
        return max(l * (total - l), r * (total - r)) % (10 ** 9 + 7)


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        sums_list = []

        def post_order(root):
            if not root:
                return 0
            left = post_order(root.left)
            right = post_order(root.right)
            res = left + right + root.val
            sums_list.append(res)
            return res

        total = post_order(root)
        sums_list.sort()
        loc = bisect.bisect_left(sums_list, total >> 1)
        l, r = sums_list[loc - 1], sums_list[loc]
        return max(l * (total - l), r * (total - r)) % (10 ** 9 + 7)


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        sums_list = []

        def post_order(root):
            if not root:
                return 0
            res = post_order(root.left) + post_order(root.right) + root.val
            sums_list.append(res)
            return res

        total = post_order(root)
        sums_list.sort()
        loc = bisect.bisect_left(sums_list, total >> 1)
        l, r = sums_list[loc - 1], sums_list[loc]
        return max(l * (total - l), r * (total - r)) % (10 ** 9 + 7)


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        sum_lists = []

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = left + right + root.val
            sum_lists.append(res)
            return res

        total = dfs(root)
        sum_lists.sort()
        loc = bisect.bisect_left(sum_lists, total >> 1)
        l, r = sum_lists[loc - 1], sum_lists[loc]
        return max(l * (total - l), r * (total - r)) % (10 ** 9 + 7)


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            res = dfs(root.left) + dfs(root.right) + root.val
            sums_list.append(res)
            return res

        sums_list = []
        total = dfs(root)
        sums_list.sort()
        loc = bisect.bisect_left(sums_list, total >> 1)
        l, r = sums_list[loc - 1], sums_list[loc]
        return max(l * (total - l), r * (total - r)) % (10 ** 9 + 7)


def main():
    ...


if __name__ == '__main__':
    main()
