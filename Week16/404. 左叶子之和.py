# 404. 左叶子之和.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        isLeafNode = lambda node: not node.left and not node.right

        def dfs(node: TreeNode) -> int:
            ans = 0
            if node.left:
                ans += node.left.val if isLeafNode(node.left) else dfs(
                    node.left)
            if node.right and not isLeafNode(node.right):
                ans += dfs(node.right)
            return ans

        return dfs(root) if root else 0


def main():
    pass


if __name__ == '__main__':
    main()
