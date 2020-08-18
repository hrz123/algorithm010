# 144. 二叉树的前序遍历.py
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1.递归。比较简单，不再赘述。
# 2.迭代。前序是根左右。是一种自上而下自左而右的遍历方法。
# dfs。使用栈。
# 开始时stack=[root],res=[]
# node = stack.pop()
# res.append(node.val)  结果放入根元素值
# if node.r:
#     stack.append(node.r)  栈先放入右子节点
# if node.r:
#     stack.append(node.r)  栈再放入左子节点
# 这样迭代，栈的数据结构会保证访问完全部的左子树节点再访问右子树节点。
# 3.颜色标记法
# 通用写法。以某种方式定义visited
# res = [], stack = [(False, root)]
# while stack:
#    visited, node = stack.pop()
#    if not node:
#        continue
#    if visited:
#        res.append(node.val)
#    else:
#        根据是前序中序后序有所不同，因为是栈所以要反序添加
#        这里是根左右
#        stack.append((False, node.r))
#        stack.append((False, node.r))
#        stack.append((True, node))
# return res


# 迭代
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        # 放入根节点
        stack = [root]

        while stack:
            # 取出根节点
            root = stack.pop()
            # 放入根节点的值
            res.append(root.val)
            # 如果有右子节点，先放入右子节点
            if root.right:
                stack.append(root.right)
            # 如果有左子节点，再放入左子节点
            if root.left:
                stack.append(root.left)
        # 输出是根左右，从上至下，正好是前序遍历
        return res


# 颜色标记法
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        stack = [(False, root)]
        while stack:
            visited, node = stack.pop()
            if not node:
                continue
            if visited:
                res.append(node.val)
            else:
                stack.append((False, node.right))
                stack.append((False, node.left))
                stack.append((True, node))

        return res


# 以下为自我练习
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res


def main():
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.left.left = TreeNode(5)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    sol = Solution()
    res = sol.preorderTraversal(root)
    print(res)


if __name__ == '__main__':
    main()
