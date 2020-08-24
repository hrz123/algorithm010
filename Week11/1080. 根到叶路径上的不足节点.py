# 1080. 根到叶路径上的不足节点.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        root_deleted = self.dfs(root, 0, limit)
        return None if root_deleted else root

    def dfs(self, node, s, limit):
        if node.left is None and node.right is None:
            return s + node.val < limit
        l_tree_deleted = r_tree_deleted = True
        if node.left:
            l_tree_deleted = self.dfs(node.left, s + node.val, limit)
        if node.right:
            r_tree_deleted = self.dfs(node.right, s + node.val, limit)
        if l_tree_deleted:
            node.left = None
        if r_tree_deleted:
            node.right = None
        return l_tree_deleted and r_tree_deleted


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(node, limit):
            if node.left is None and node.right is None:
                return node.val >= limit
            l_tree_saved = r_tree_saved = False
            if node.left:
                l_tree_saved = dfs(node.left, limit - node.val)
            if node.right:
                r_tree_saved = dfs(node.right, limit - node.val)
            if not l_tree_saved:
                node.left = None
            if not r_tree_saved:
                node.right = None
            return l_tree_saved or r_tree_saved

        return root if dfs(root, limit) else None


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(root, limit):
            if not root.left and not root.right:
                return root.val >= limit
            l_tree_saved = dfs(root.left,
                               limit - root.val) if root.left else False
            if not l_tree_saved:
                root.left = None
            r_tree_saved = dfs(root.right,
                               limit - root.val) if root.right else False
            if not r_tree_saved:
                root.right = None
            return l_tree_saved or r_tree_saved

        return root if dfs(root, limit) else None


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def deleted(root, pre, limit):
            if not root.left and not root.right:
                return root.val + pre < limit
            pre += root.val
            l_tree_deleted = r_tree_deleted = True
            if root.left:
                l_tree_deleted = deleted(root.left, pre, limit)
            if root.right:
                r_tree_deleted = deleted(root.right, pre, limit)
            if l_tree_deleted:
                root.left = None
            if r_tree_deleted:
                root.right = None
            return l_tree_deleted and r_tree_deleted

        return None if deleted(root, 0, limit) else root


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def saved(root, pre, limit):
            if not root.left and not root.right:
                return root.val + pre >= limit
            l_tree_saved = r_tree_saved = False
            pre += root.val
            if root.left:
                l_tree_saved = saved(root.left, pre, limit)
            if root.right:
                r_tree_saved = saved(root.right, pre, limit)
            if not l_tree_saved:
                root.left = None
            if not r_tree_saved:
                root.right = None
            return l_tree_saved or r_tree_saved

        return root if saved(root, 0, limit) else None


def main():
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(-5)
    root.right = TreeNode(-3)
    root.right.left = TreeNode(4)
    node = sol.sufficientSubset(root, -1)

    def level(n):
        if not n:
            return []
        res = []
        q, nq = [n], []
        while q:
            output = []
            for n in q:
                output.append(n.val)
                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)
            res.append(output)
            q, nq = nq, []
        return res

    print(level(node))


if __name__ == '__main__':
    main()
