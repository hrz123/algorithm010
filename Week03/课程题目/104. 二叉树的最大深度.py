# 104. 二叉树的最大深度.py


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # recursion terminator
        if not root:
            return 0
        # process current level logic
        # drill down
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# 迭代
# dfs迭代
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        res = 1

        while stack:
            node, level = stack.pop()
            res = max(res, level)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        return res


# bfs迭代
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        q, nq = [root], []

        while q:
            res += 1
            for node in q:
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)

            q, nq = nq, []

        return res


# dfs递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0

        def dfs(level, node):
            nonlocal max_depth
            if not node:
                if level > max_depth:
                    max_depth = level
                return max_depth

            dfs(level + 1, node.left)
            dfs(level + 1, node.right)

        dfs(0, root)

        return max_depth


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    res = sol.maxDepth(root)
    print(res)


if __name__ == '__main__':
    main()
