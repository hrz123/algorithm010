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


def main():
    ...


if __name__ == '__main__':
    main()
