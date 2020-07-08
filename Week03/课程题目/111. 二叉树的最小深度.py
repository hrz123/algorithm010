# 111. 二叉树的最小深度.py

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
# helper(level, node)
# 终止条件
# if not node.left or not node.right
#      return level
# level += 1
# left = helper(level, node.left)
# right = helper(level, node.right)
# reverse current level status
# return 1 + min(left, right)
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(level, node):
            if not node.left and not node.right:
                return level
            level += 1
            left = helper(level, node.left) if node.left else float('inf')
            right = helper(level, node.right) if node.right else float('inf')

            return min(left, right)

        return helper(1, root)


# 时间复杂度：O(n)，遍历了所有的点
# 空间复杂度：O(log(n))，树的高度

# dfs递归
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        min_depth = float('inf')

        def dfs(level, node):
            nonlocal min_depth
            # recursion terminator
            if not node.left and not node.right:
                if level < min_depth:
                    min_depth = level
            # process current level logic
            level += 1
            # drill down
            if node.left:
                dfs(level, node.left)
            if node.right:
                dfs(level, node.right)

        dfs(1, root)

        return min_depth


# dfs迭代
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = float("inf")
        stack = [(root, 1)]

        while stack:
            node, level = stack.pop()
            if not node.left and not node.right:
                if level < res:
                    res = level
            level += 1
            if node.right:
                stack.append((node.right, level))
            if node.left:
                stack.append((node.left, level))
        return res


# bfs迭代
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        deq = deque([(root, 1)])

        while deq:
            node, level = deq.popleft()
            if not node.left and not node.right:
                return level
            level += 1
            if node.left:
                deq.append((node.left, level))
            if node.right:
                deq.append((node.right, level))


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    res = sol.minDepth(root)
    print(res)


if __name__ == '__main__':
    main()
