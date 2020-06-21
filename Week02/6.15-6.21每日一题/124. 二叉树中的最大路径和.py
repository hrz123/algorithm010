# 124. 二叉树中的最大路径和.py
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1.首先想到递归
# 最大路径可能出现在左子树、右子树和经过根节点
# 一共只有三种情况。对于左子树和右子树我们可以递归求解。
# 然后取最大值。
# 这里重要的一点是递归返回的结果和更新的结果不一样。
# 返回的结果是取左右两边最大的。
# 更新使用的结果是root.val + 左边最大的 + 右边最大的
# def maxPathSUm(root):
#     max_path = float('-inf')
#
#     def get_max_gain(node):
#         nonlocal max_path
#         if not node:
#             return 0
#         left_gain = max(get_max_gain(node.left), 0)
#         right_gain = max(get_max_gain(node.right), 0)
#         cur_max_path = node.val + left_gain + right_gain
#         max_path = max(max_path, cur_max_path)
#         return node.val + max(left_gain, right_gain)
#
#     get_max_gain(root)
#     return max_path


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float("-inf")  # placeholder to be updated

        def get_max_gain(node):
            nonlocal max_path  # This tells that max_path is not a local variable
            if not node:
                return 0
            gain_on_left = max(get_max_gain(node.left),
                               0)  # Read the part important observations
            gain_on_right = max(get_max_gain(node.right),
                                0)  # Read the part important observations

            current_max_path = node.val + gain_on_left + gain_on_right  # Read first three images of going down the recursion stack
            max_path = max(max_path,
                           current_max_path)  # Read first three images of going down the recursion stack

            return node.val + max(gain_on_left,
                                  gain_on_right)  # Read the last image of going down the recursion stack

        get_max_gain(root)  # Starts the recursion chain
        return max_path


def main():
    pass


if __name__ == '__main__':
    main()
