# 112. 路径总和.py
from collections import deque


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。


# 这道题一眼看上去就是dfs解法


# 递归
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # recursion terminator
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum

        # process current row logic
        sum -= root.val

        # drill down
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right,
                                                                  sum)


# dfs stack迭代
# dfs和bfs中如果加入状态，相当于函数中增加了一个参数
# 先序遍历
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                if val == sum:
                    return True
            if curr.right:
                stack.append((curr.right, val + curr.right.val))
            if curr.left:
                stack.append((curr.left, val + curr.left.val))
        return False


# bfs
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue = deque([(root, sum - root.val)])
        while queue:
            curr, val = queue.popleft()
            if not curr.left and not curr.right:
                if val == 0:
                    return True
            if curr.left:
                queue.append((curr.left, val - curr.left.val))
            if curr.right:
                queue.append((curr.right, val - curr.right.val))
        return False


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == sum

        return self.hasPathSum(root.left, sum - root.val) or \
               self.hasPathSum(root.right, sum - root.val)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == sum

        return self.hasPathSum(root.left, sum - root.val) or \
               self.hasPathSum(root.right, sum - root.val) or \
               self.hasPathSum(root.left, sum) or \
               self.hasPathSum(root.right, sum)


# 以下为自我练习
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(
            root.right, sum - root.val)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(
            root.right, sum - root.val)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        deq = deque([(root, sum - root.val)])
        while deq:
            node, target = deq.popleft()
            if not node.left and not node.right and target == 0:
                return True
            if node.left:
                deq.append((node.left, target - node.left.val))
            if node.right:
                deq.append((node.right, target - node.right.val))
        return False


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, sum - root.val)]
        while stack:
            node, target = stack.pop()
            if not node.left and not node.right and target == 0:
                return True
            if node.left:
                stack.append((node.left, target - node.left.val))
            if node.right:
                stack.append((node.right, target - node.right.val))
        return False


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(
            root.right, sum - root.val)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(
            root.right, sum - root.val)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(
            root.right, sum - root.val)


def main():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    sol = Solution()
    res = sol.hasPathSum(root, 22)
    print(res)


if __name__ == '__main__':
    main()
