# 101. 对称二叉树.py

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归的想法
# 根据题目的描述，镜像对称，就是左右两边相等，也就是左子树和右子树是相当的，注意这里是递归定义
# 我们将根节点的左子树记做left，右子树记做right。比较left是否等于right，
# 不等的话直接返回false即可。
# 如果相等，比较left的左节点和right的右节点，再比较left的右节点和right的左节点。
# 根据上面信息可以总结出递归函数的两个条件
# 终止条件
# 1.left和right不等返回false，left和right一个为空一个不为空返回false
# r right都为空返回True
# 2.递归的比较left.r, r.right和left.r, r.r
# 可以令初始的left right都为root
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root, root)


# 队列
# 回想下递归的实现：
# 当两子树的根节点相等时，就比较左子树的left和右子树的right，再比较左子树的right和右子树的left
# 现在我们改用队列实现，思路如下
# 每次从队列中拿出两个节点比较
# 如果两个节点都是None，就继续
# 如果只有一个是None，返回False
# 如果两个节点的值相等，将左节点的left和右节点的right加入队列，再将左节点的right和右节点的left
# 加入队列
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True

        deq = deque([(root.left, root.right)])

        while deq:
            left, right = deq.popleft()
            if not left and not right:
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            deq.append((left.left, right.right))
            deq.append((left.right, right.left))
        return True


# 以下为自我练习
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            return helper(left.left, right.right) and helper(left.right,
                                                             right.left)

        return helper(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        deq = deque([(root.left, root.right)])

        while deq:
            left, right = deq.popleft()
            if not left and not right:
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            deq.append((left.left, right.right))
            deq.append((left.right, right.left))
        return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            return helper(left.left, right.right) and helper(left.right,
                                                             right.left)

        return helper(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        deq = deque([(root.left, root.right)])
        while deq:
            left, right = deq.popleft()
            if not left and not right:
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            deq.append((left.left, right.right))
            deq.append((left.right, right.left))
        return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            return helper(left.left, right.right) \
                   and helper(left.right, right.left)

        if not root:
            return True
        return helper(root.left, root.right)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            return helper(left.left, right.right) and helper(left.right,
                                                             right.left)

        if not root:
            return True
        return helper(root.left, root.right)


def main():
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    res = sol.isSymmetric(root)
    print(res)


if __name__ == '__main__':
    main()
