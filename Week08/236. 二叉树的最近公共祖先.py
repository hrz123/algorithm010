# 236. 二叉树的最近公共祖先.py

# 1. parent node --> 往上走，common node
# 2. 遍历：Path1(root-->p), Path2(root-->q), 找分叉点
# 3. DFS


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 算法：
# 递归
# 当我们用递归取桌这个题时不要被题目误导，应该要明确一点
# 这个函数的功能有三个：给定两个节点p和q
# 1.如果p和q都存在，则返回它们的公共祖先；
# 2.如果只存在一个，则返回存在的一个；
# 3.如果p和q都不存在，则返回NULL
# 本题说给定的两个节点都存在，那自然还是能用上面的函数来解决

# 具体思路
# 1.如果当前节点root等于NULL，则直接返回NULL
# 2.如果root等于p或者q，则这棵树一定返回p或者q
# 3.然后递归左右子树，因为是递归，使用函数后可认为左右子树已经算出结果，用 r 和 r 表示
# 4.此时若left为空，那最终结果只要看right；若right为空，那最终结果只要看left
# 5.如果left和right都非空，因为只给了p和q两个结点，都非空，说明一边一个
#   因此root是它们的最近公共祖先
# 6.如果left和right都为空，则返回空（其实已经包含在前面的情况中了）

# 时间复杂度：O(n)，每个节点最多遍历一次
# 空间复杂度：O(n)，递归需要使用栈空间


class Solution:
    def lowestCommonAncestor(
            self,
            root: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode'
    ) -> 'TreeNode':
        if not root:
            return

        if root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        if not right:
            return left

        return root


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        if not right:
            return left

        return root


# 以下为自我练习
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        if not right:
            return left
        return root


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left if left else right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left if left else right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left if left else right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left if left else right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left if left else right


# 想法：如果p和q可以不在二叉树中呢？
# 要写一个函数

def main():
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 1

    def deserialize(arr):
        if not arr:
            return

        def helper(i):
            if i >= len(arr):
                return
            if arr[i] is None:
                return
            root = TreeNode(arr[i])
            root.left = helper(2 * i + 1)
            root.right = helper(2 * i + 2)
            return root

        return helper(0)

    root = deserialize(root)

    def print_tree(root):
        if not root:
            print('#', end=" ")
            return
        print(root.val, end=" ")
        print_tree(root.left)
        print_tree(root.right)

    print_tree(root)
    print()

    sol = Solution()
    res = sol.lowestCommonAncestor(root, root.left, root.right)
    print_tree(res)


if __name__ == '__main__':
    main()
