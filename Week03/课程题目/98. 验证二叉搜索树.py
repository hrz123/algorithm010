# 98. 验证二叉搜索树.py

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# BST --> 中序遍历是递增的

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True


# 另一种解法 --> 递归
# 如果该二叉树的左子树不为空，
# 则左子树上所有节点的值均小于它的根节点的值；
# 若它的右子树不空，
# 则右子树上所有节点的值均大于它的根节点的值；
# 它的左右子树也为二叉搜索树。
# 这启示我们设计一个递归函数 helper(root, lower, upper)
# 来递归判断，函数表示考虑以 root 为根的子树，
# 判断子树中所有节点的值是否都在 (l,row) 的范围内
# （注意是开区间）。
# 如果 root 节点的值 val 不在 (l,row) 的范围内
# 说明不满足条件直接返回，
# 否则我们要继续递归调用检查它的左右子树是否满足，
# 如果都满足才说明这是一棵二叉搜索树。


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)


# 以下为自我练习

# 中序遍历是严格升序的
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = []
        inorder = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        inorder = float('-inf')
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            # 注意也不能等于
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False

            return helper(node.left, lower, node.val) and helper(node.right,
                                                                 node.val,
                                                                 upper)

        return helper(root)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def helper(node, low, high):
            # recursion terminator
            if not node:
                return True
            # process current row logic
            if low < node.val < high:
                return helper(node.left, low, node.val) and helper(
                    node.right, node.val, high)
            return False

        return helper(root, float('-inf'), float('inf'))


# 中序遍历是严格升序的
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        prev = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lo, hi):
            # recursion terminator
            if not node:
                return True
            # process current row logic
            if node.val >= hi or node.val <= lo:
                return False
            return helper(node.left, lo, node.val) and helper(node.right,
                                                              node.val, hi)

        return helper(root, float('-inf'), float('inf'))


# 二叉搜索树中序遍历是严格递增的
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        prev = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lo, hi = float('-inf'), float('inf')

        def helper(root, lo, hi):
            if not root:
                return True
            if root.val <= lo or root.val >= hi:
                return False
            return helper(root.left, lo, root.val) and helper(root.right,
                                                              root.val, hi)

        return helper(root, lo, hi)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pre = float('-inf')
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pre = float('-inf')
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, lo, hi):
            if not root:
                return True
            if root.val <= lo or root.val >= hi:
                return False
            return helper(root.left, lo, root.val) and helper(root.right,
                                                              root.val, hi)

        return helper(root, float('-inf'), float('inf'))


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        pre = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        pre = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right
        return True


def main():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    sol = Solution()
    res = sol.isValidBST(root)
    print(res)


if __name__ == '__main__':
    main()
