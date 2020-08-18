# 1373. 二叉搜索子树的最大键值和.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            if not root:
                return True, float('inf'), float('-inf'), 0
            left = dfs(root.left)
            right = dfs(root.right)
            if not left[0] or not right[0] or \
                    root.val >= right[1] or root.val <= left[2]:
                return False, 0, 0, 0
            cur_min = left[1] if root.left else root.val
            cur_max = right[2] if root.right else root.val
            total = root.val + left[3] + right[3]
            nonlocal res
            res = max(res, total)
            return True, cur_min, cur_max, total

        dfs(root)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
