# 429. N叉树的层序遍历.py
from collections import deque
from typing import List

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# 1.迭代。bfs，使用队列。
# if not root:
#     return []
# data = [root], res = []
# while data:
#     output = []
#     mask = len(data)
#     for _ in range(mask):
#         node = data.popleft()
#         output.append(node.val)  # 这里访问了node.val，那么要做node为null的处理
#         for child in node.children:
#             data.append(child)
#     res.append(output)
# return res
# 2.bfs的简化
# 使用prev_layer数组存储前一层的节点。cur_layer存储当前层的节点。
# prev_layer = cur_layer
# 直到perv_layer为空
# if not root:
#     return []
# res = []
# prev_layer = [root]
# while prev_layer:
#     cur_layer = []
#     res.append([])
#     for node in prev_layer:
#         res[-1].append(node.val)
#         cur_layer.extend(node.children)
#     prev_layer = cur_layer
# return res
# 3.递归。
# 层序遍历也可以用递归实现。
# 传入一个level，代表属于第几层。向相应的层添加值。
# def traverse_node(node, row):
#     if len(res) == row:
#         res.append([])
#     res[row].append(node.val)
#     for child in node.children:
#         traverse_node(child, row + 1)
# res = []
# if not root: # traverse_node需要访问node.val，所以要判断root是否为null
#     traverse_node(root, 0)
# return res
# 递归因为不停有进栈出栈，所以空间复杂度平均为O(logN)，最坏为O(N)。树的高度。
# 而前两种使用队列都是O(N)的空间复杂度。
# 时间复杂度所有方法都是O(N)。


# 使用队列实现广度优先搜索
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        deq = deque([root])

        while deq:
            output = []
            for _ in range(len(deq)):
                node = deq.popleft()
                output.append(node.val)
                for child in node.children:
                    deq.append(child)

            res.append(output)

        return res


# 时间复杂度：O(N)。每个节点都访问一遍。
# 空间复杂度：deque最大会装下一层全部的节点，最大在n/2这个级别。O(N)


# 简化广度优先搜索
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        res = []
        prev_layer = [root]

        while prev_layer:
            cur_layer = []
            res.append([])
            for node in prev_layer:
                res[-1].append(node.val)
                cur_layer.extend(node.children)
            prev_layer = cur_layer
        return res


# 时间复杂度：O(N)
# 空间复杂度：O(N)


# 递归
# 算法：
# 我们可以使用递归来解决这个问题，
# 通常我们不能使用递归进行广度优先搜索。
# 这是因为广度优先搜索基于队列，而递归运行时使用堆栈，
# 适合深度优先搜索。但是在本题中，
# 我们可以以不同的顺序添加到最终列表中，
# 只要我们知道节点在哪一层并确保在那一层的列表顺序正确就可以了。
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def traverse_node(node: 'Node', level: int):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        result = []

        if not root:
            traverse_node(root, 0)
        return result


# 时间复杂度：每个节点访问一遍O(N)
# 空间复杂度为树的高度。平均为O(logN)。最坏为O(N)


# 以下为自我练习

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        deq = deque([root])
        result = []
        while deq:
            size = len(deq)
            level = []
            for _ in range(size):
                root = deq.popleft()
                level.append(root.val)
                if root.children:
                    deq.extend(root.children)
            result.append(level)
        return result


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q, nq = [root], []
        res = []

        while q:
            level = []
            for node in q:
                if node.children:
                    nq.extend(node.children)
                level.append(node.val)
            res.append(level)
            q, nq = nq, []
        return res


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q, nq = [root], []
        res = []
        while q:
            output = []
            for node in q:
                output.append(node.val)
                if node.children:
                    nq.extend(node.children)
            res.append(output)
            q, nq = nq, []
        return res


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q, nq = [root], []
        res = []
        while q:
            output = []
            for node in q:
                output.append(node.val)
                if node.children:
                    nq.extend(node.children)
            res.append(output)
            q, nq = nq, []
        return res


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q, nq = [root], []
        res = []
        while q:
            output = []
            for node in q:
                output.append(node.val)
                if node.children:
                    nq.extend(node.children)
            res.append(output)
            q, nq = nq, []
        return res


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q, nq = [root], []
        res = []
        while q:
            output = []
            for node in q:
                output.append(node.val)
                if node.children:
                    nq.extend(node.children)
            res.append(output)
            q, nq = nq, []
        return res


def main():
    pass


if __name__ == '__main__':
    main()
