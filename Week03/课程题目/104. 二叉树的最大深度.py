# 104. 二叉树的最大深度.py


# Definition for a binary tree node.
from collections import deque


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
        # process current row logic
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


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0

        stack = [(root, 1)]

        while stack:
            root, depth = stack.pop()
            if not root.left and not root.right:
                res = max(res, depth)
            if root.left:
                stack.append((root.left, depth + 1))
            if root.right:
                stack.append((root.right, depth + 1))
        return res


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = 0

        def dfs(level, node):
            nonlocal res
            if not node:
                res = max(res, level)
                return res

            dfs(level + 1, node.left)
            dfs(level + 1, node.right)

        dfs(0, root)

        return res


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


# 递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # recursion terminator
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# bfs
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 特殊处理
        if not root:
            return 0
        deq = deque([root])
        res = 0
        while deq:
            res += 1
            size = len(deq)
            for _ in range(size):
                root = deq.popleft()
                if root.left:
                    deq.append(root.left)
                if root.right:
                    deq.append(root.right)
        return res


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# bfs
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        deq = deque([root])
        res = 0
        while deq:
            res += 1
            for _ in range(len(deq)):
                root = deq.popleft()
                if root.left:
                    deq.append(root.left)
                if root.right:
                    deq.append(root.right)
        return res


# dfs
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        res = 0
        while stack:
            root, level = stack.pop()
            res = max(res, level)
            if root.left:
                stack.append((root.left, level + 1))
            if root.right:
                stack.append((root.right, level + 1))
        return res


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, level):
            nonlocal res
            if not root:
                res = max(res, level)
                return
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return res


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, pre):
            nonlocal res
            if not root:
                res = max(pre, res)
                return
            dfs(root.left, pre + 1)
            dfs(root.right, pre + 1)

        dfs(root, 0)
        return res


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        res = 1
        while stack:
            root, level = stack.pop()
            res = max(res, level)
            if root.left:
                stack.append((root.left, level + 1))
            if root.right:
                stack.append((root.right, level + 1))
        return res


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        deq = deque([(root, 1)])
        res = 1
        while deq:
            root, level = deq.popleft()
            res = max(res, level)
            if root.left:
                deq.append((root.left, level + 1))
            if root.right:
                deq.append((root.right, level + 1))
        return res


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


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
