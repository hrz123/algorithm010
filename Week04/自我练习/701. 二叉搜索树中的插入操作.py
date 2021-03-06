# 701. 二叉搜索树中的插入操作.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 迭代的写法
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        prev, cur = None, root

        while cur:
            prev = cur
            if val > cur.val:
                cur = cur.right
            else:
                cur = cur.left

        if val > prev.val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)

        return root


# 递归的写法
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val > root.val:
            # insert into the r subtree
            root.right = self.insertIntoBST(root.right, val)
        else:
            # insert into the r subtree
            root.left = self.insertIntoBST(root.left, val)
        return root


# 迭代的写法
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            # insert into the r subtree
            if val > node.val:
                # insert r now
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            # insert into the r subtree
            else:
                # insert r now
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return TreeNode(val)


# 以下为自我练习
# 递归更简洁
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return TreeNode(val)


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                node = node.left
        return TreeNode(val)


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if not root.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return TreeNode(val)


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        cur = root
        while cur:
            if cur.val < val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    break
                else:
                    cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    break
                else:
                    cur = cur.left


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        cur = root
        while cur:
            if val > cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    return root
            else:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    return root


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        node = root
        while node:
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                node = node.left


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


def main():
    pass


if __name__ == '__main__':
    main()
