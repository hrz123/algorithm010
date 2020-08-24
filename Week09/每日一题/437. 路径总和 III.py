# 437. 路径总和 III.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        prefix_sum_count = {0: 1}
        return self.recursion_path_sum(root, prefix_sum_count, sum, 0)

    def recursion_path_sum(self, node, prefix_sum_count, target, cur_sum):
        if not node:
            return 0
        res = 0
        cur_sum += node.val
        res += prefix_sum_count.get(cur_sum - target, 0)
        prefix_sum_count[cur_sum] = prefix_sum_count.get(cur_sum, 0) + 1

        res += self.recursion_path_sum(node.left, prefix_sum_count, target,
                                       cur_sum)
        res += self.recursion_path_sum(node.right, prefix_sum_count, target,
                                       cur_sum)
        prefix_sum_count[cur_sum] -= 1
        return res


# 以下为自我练习
class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        pre_sum_count = {0: 1}
        return self.findPathSum(root, pre_sum_count, 0, sum)

    def findPathSum(self, node, pre_sum_count, pre, target):
        if not node:
            return 0
        res = 0
        pre += node.val
        if pre - target in pre_sum_count:
            res += pre_sum_count[pre - target]
        pre_sum_count[pre] = pre_sum_count.get(pre, 0) + 1
        res += self.findPathSum(node.left, pre_sum_count, pre, target)
        res += self.findPathSum(node.right, pre_sum_count, pre, target)
        pre_sum_count[pre] -= 1
        return res


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        pathSum = {0: 1}
        return self.findPathSum(root, 0, sum, pathSum)

    def findPathSum(self, root, pre, target, pathSum):
        if not root:
            return 0
        pre += root.val
        res = 0
        if pre - target in pathSum:
            res += pathSum[pre - target]
        pathSum[pre] = pathSum.get(pre, 0) + 1
        res += self.findPathSum(root.left, pre, target, pathSum)
        res += self.findPathSum(root.right, pre, target, pathSum)
        pathSum[pre] -= 1
        return res


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        pre_sum = {0: 1}
        return self.dfs(root, 0, sum, pre_sum)

    def dfs(self, root, pre, target, pre_sum):
        if not root:
            return 0
        res = 0
        pre += root.val
        if pre - target in pre_sum:
            res += pre_sum[pre - target]
        pre_sum[pre] = pre_sum.get(pre, 0) + 1
        res += self.dfs(root.left, pre, target, pre_sum)
        res += self.dfs(root.right, pre, target, pre_sum)
        pre_sum[pre] -= 1
        return res


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        pre_sums = {0: 1}
        return self.findSum(root, 0, pre_sums, sum)

    def findSum(self, root, pre, pre_sums, target):
        if not root:
            return 0
        pre += root.val
        res = 0
        if pre - target in pre_sums:
            res += pre_sums[pre - target]
        pre_sums[pre] = pre_sums.get(pre, 0) + 1
        res += self.findSum(root.left, pre, pre_sums, target)
        res += self.findSum(root.right, pre, pre_sums, target)
        pre_sums[pre] -= 1
        return res


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        pre_sums = {0: 1}
        return self.dfs(root, 0, pre_sums, sum)

    def dfs(self, root, pre, pre_sums, target):
        if not root:
            return 0
        pre += root.val
        res = 0
        if pre - target in pre_sums:
            res += pre_sums[pre - target]
        pre_sums[pre] = pre_sums.get(pre, 0) + 1
        res += self.dfs(root.left, pre, pre_sums, target)
        res += self.dfs(root.right, pre, pre_sums, target)
        pre_sums[pre] -= 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
