# 剑指 Offer 36. 二叉搜索树与双向链表.py


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        head = node = stack.pop()
        pre = node
        node = node.right
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            pre.right = node
            node.left = pre
            pre = node
            node = node.right
        pre.right = head
        head.left = pre
        return head


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        stack = []
        while root:
            stack.append(root)
            root = root.left
        head = root = stack.pop()
        pre = root
        root = root.right
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            root.left = pre
            pre.right = root
            pre = root
            root = root.right
        pre.right = head
        head.left = pre
        return head


def main():
    pass


if __name__ == '__main__':
    main()
