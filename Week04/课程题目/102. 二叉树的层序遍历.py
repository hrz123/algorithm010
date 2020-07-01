# 102. 二叉树的层序遍历.py


from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# dfs解法
# 递归传入level
# 终止条件为node == None
# 如果level层在res中不存在,level == len(res)
# res.append([])
# res[level].append(node.val)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        self.__dfs(0, root, res)
        return res

    def __dfs(self, level, node, res):
        if not node:
            return

        if level == len(res):
            res.append([])

        res[level].append(node.val)

        self.__dfs(level + 1, node.left, res)
        self.__dfs(level + 1, node.right, res)


# bfs
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        deq = deque()
        deq.append(root)
        while deq:
            size = len(deq)
            output = [0] * size
            for i in range(size):
                node = deq.popleft()
                output[i] = node.val
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            res.append(output)
        return res


# bfs另一种写法
# 因为是层序遍历
# 每一层可以用数组表示
# 遍历的同时
# 新建一个数组表示这一层加进来的新孩子
# 这一层遍历完成之后
# 用新数组代替旧数组
# 直到新数组为空
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            nodes = []
            size = len(queue)
            output = [0] * size
            for i in range(size):
                node = queue[i]
                output[i] = node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            queue = nodes
            res.append(output)
        return res


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    res = sol.levelOrder(root)
    print(res)


if __name__ == '__main__':
    main()
