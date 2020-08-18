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
            # mid = r + (r - r + 1) // 2
            root = TreeNode(nums[mid])
            root.left = helper(nums, left, mid - 1)
            root.right = helper(nums, mid + 1, right)
            return root

        return helper(nums, 0, len(nums) - 1)


# 以下为自我练习
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return
            mid = left + ((right - left) >> 1)
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node

        return helper(0, len(nums) - 1)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left <= right:
                mid = left + ((right - left) >> 1)
                root = TreeNode(nums[mid])
                root.left = helper(left, mid - 1)
                root.right = helper(mid + 1, right)
                return root

        return helper(0, len(nums) - 1)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def convertBST(l, r):
            if l > r:
                return
            mid = l + ((r - l) >> 1)
            left = convertBST(l, mid - 1)
            root = TreeNode(nums[mid])
            root.left = left
            root.right = convertBST(mid + 1, r)
            return root

        return convertBST(0, len(nums) - 1)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(l, r):
            if l > r:
                return
            mid = l + ((r - l) >> 1)
            root = TreeNode(nums[mid])
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root

        return helper(0, len(nums) - 1)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(l, r):
            if l > r:
                return
            mid = l + ((r - l) >> 1)
            root = TreeNode(nums[mid])
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root

        return helper(0, len(nums) - 1)


def main():
    pass


if __name__ == '__main__':
    main()
