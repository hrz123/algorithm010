# 589. N叉树的前序遍历.py
from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# 1.递归的方法。对每一个child：children，调用这个函数。全局的数组添加这个元素。
# 时间复杂度：O(N)。所有的节点都访问一遍。
# 空间复杂度：递归栈的大小为树的高度。树的高度，平均O(logN)。最坏O(N)
# 2.迭代的方法。
# 前序遍历顺序为根->左孩子->右孩子，递归的方式，为dfs。数据结构使用栈。
# 首先将root放入栈中。
# 栈不为空。那么node为出栈元素。令result.append(node.val)。此为根。
# 然后将node.children中的元素反序加入栈中。
# 这是拿出栈顶的第一个元素。即为最左边的孩子。
# 将值加入result中。
# 并此时应该访问此节点的孩子节点。
# 继续将此节点的孩子反序加入栈中。
# 以此类推。
# 时间复杂度：O(N)。所有节点都访问一遍。
# 空间复杂度：手动维护所有的栈，不像递归时形成分支，空间复杂度更高一些。平均最坏都是O(N)。


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# 递归
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self._preorfer(root, res)
        return res

    def _preorfer(self, root, res):
        if not root:
            return

        res.append(root.val)
        for child in root.children:
            self._preorfer(child, res)


# 迭代
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            # if not node.children:
            #     continue
            for child in node.children[::-1]:
                stack.append(child)

        return res


# 以下为自我练习
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.children:
                stack.extend(reversed(root.children))

        return res


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            res.append(root.val)
            if root.children:
                for child in root.children:
                    dfs(child)

        dfs(root)
        return res


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.children:
                for child in root.children[::-1]:
                    stack.append(child)
        return res


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.children:
                for node in root.children[::-1]:
                    stack.append(node)
        return res


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.children:
                for ch in root.children[::-1]:
                    stack.append(ch)
        return res


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                for ch in node.children[::-1]:
                    stack.append(ch)
        return res


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.children:
                stack.extend(reversed(root.children))
        return res


def main():
    root = Node(1)
    node = Node(3)
    root.children = [node, Node(2), Node(4)]
    node.children = [Node(5), Node(6)]

    s = Solution()
    res = s.preorder(root)
    print(res)


if __name__ == '__main__':
    main()
