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


# 对于每一个子树
# 返回是否为二叉搜索树，最小值，最大值，子树和
# 如果不是返回 False , 0, 0, 0
# 递推
# 1.left为二叉搜索树，right为二叉搜索树，且root.val>left的最大值<right的最小值
# 2.最小值为left的最小值如果root.left存在，否则为root.val
# 3.最大值同理
# 4.子树和等于left+right+root.val
# 初始化
# True, float('inf'), float('-inf'), 0
# 用后续遍历递推
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        res = 0

        def post_order(root):
            if not root:
                return True, float('inf'), float('-inf'), 0
            left = post_order(root.left)
            right = post_order(root.right)
            if not left[0] or not right[0] \
                    or root.val <= left[2] or root.val >= right[1]:
                return False, 0, 0, 0
            _min = left[1] if root.left else root.val
            _max = right[2] if root.right else root.val
            _sum = left[3] + right[3] + root.val
            nonlocal res
            res = max(res, _sum)
            return True, _min, _max, _sum

        post_order(root)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
