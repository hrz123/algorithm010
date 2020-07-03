# 108. 将有序数组转换为二叉搜索树.py
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(nums, left, right):
            if left > right:
                return
            mid = left + (right - left) // 2
            # mid = left + (right - left + 1) // 2
            root = TreeNode(nums[mid])
            root.left = helper(nums, left, mid - 1)
            root.right = helper(nums, mid + 1, right)
            return root

        return helper(nums, 0, len(nums) - 1)


def main():
    pass


if __name__ == '__main__':
    main()
