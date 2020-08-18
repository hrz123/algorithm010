# 113. 路径总和 II.py

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            if sum == root.val:
                return [[sum]]
        left = self.pathSum(root.left, sum - root.val)
        right = self.pathSum(root.right, sum - root.val)
        return [[root.val] + path for path in left + right]


# 以下为自我练习
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[sum]] if root.val == sum else []
        left = self.pathSum(root.left, sum - root.val)
        right = self.pathSum(root.right, sum - root.val)
        return [[root.val] + ans for ans in left + right]


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[sum]] if root.val == sum else []
        left = self.pathSum(root.left, sum - root.val)
        right = self.pathSum(root.right, sum - root.val)
        return [[root.val] + ans for ans in left + right]


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[sum]] if sum == root.val else []
        left = self.pathSum(root.left, sum - root.val)
        right = self.pathSum(root.right, sum - root.val)
        return [[root.val] + ans for ans in left + right]


def main():
    pass


if __name__ == '__main__':
    main()
