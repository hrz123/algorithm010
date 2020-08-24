# 979. 在二叉树中分配硬币.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        # 定义dfs求过载量
        # 我们可以用上述的方法来逐步构建我们的最终答案。
        # 定义 dfs(node) 为这个节点所在的子树中金币的 过载量，
        # 也就是这个子树中金币的数量减去这个子树中节点的数量。
        # 接着，我们可以计算出这个节点与它的子节点之间需要移动金币的数量为
        # abs(dfs(node.left)) + abs(dfs(node.right))，
        # 这个节点金币的过载量为 node.val + dfs(node.left) + dfs(node.right) - 1
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            self.res += abs(left) + abs(right)
            return node.val - 1 + left + right

        dfs(root)
        return self.res


# 以下为自我练习
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        res = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal res
            res += abs(left) + abs(right)
            return node.val - 1 + left + right

        dfs(root)
        return res


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        res = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal res
            res += abs(left) + abs(right)
            return node.val - 1 + left + right

        dfs(root)
        return res


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res
            res += abs(left) + abs(right)
            return root.val - 1 + left + right

        dfs(root)
        return res


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res
            res += abs(left) + abs(right)
            return root.val - 1 + left + right

        dfs(root)
        return res


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res
            res += abs(left) + abs(right)
            return root.val - 1 + left + right

        dfs(root)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
