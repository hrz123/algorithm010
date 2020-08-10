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


def main():
    pass


if __name__ == '__main__':
    main()
