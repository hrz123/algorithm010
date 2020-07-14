# 94. 二叉树的中序遍历.py
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1.递归。
# 二叉树的中序遍历是左根右。自下而上。dfs。
# 递归时需要，函数先作用在节点的左子节点上。添加根节点的值至结果数组。
# 再作用函数到右子节点上。退出条件是node == null。
# 比较简单。不赘述。
# 2.迭代。
# 需要同时记录node和stack。
# 首先不停的将node放入stack，node = node.left
# 直到node = null后
# 取node = stack.pop()
# 将node.val放入结果数组（此为最左节点）
# 令node = node.right (node可能为根节点，其右子节点的迭代方法一样)
# 迭代将node放入stack，node = node.left，与前面过程一样
# 这样即可得到中序遍历。
# 3.适合于前序中序后序三种遍历代码几乎一样的颜色标记法。见二叉树前序遍历。


# 递归的写法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self._helper(root, res)
        return res

    def _helper(self, node: TreeNode, res: List[int]) -> None:
        if not node:
            return

        self._helper(node.left, res)
        res.append(node.val)
        self._helper(node.right, res)


# 迭代的写法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []

        while root or stack:
            # 先把最左的节点都放进去
            while root:
                stack.append(root)
                root = root.left
            # 直到 root = None，此时拿出栈顶元素，将值放入列表
            root = stack.pop()
            res.append(root.val)
            # 令node指向其右子节点
            root = root.right

        return res


# 颜色标记法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res


# 以下为自我练习
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    res = s.inorderTraversal(root)
    print(res)


if __name__ == '__main__':
    main()
