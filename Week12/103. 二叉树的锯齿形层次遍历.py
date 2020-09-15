# 103. 二叉树的锯齿形层次遍历.py


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q, nq = [root], []
        res = []
        flag = True
        while q:
            output = []
            for node in q:
                output.append(node.val)
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            if flag:
                res.append(output)
            else:
                res.append(output[::-1])
            q, nq = nq, []
            flag = not flag
        return res


def main():
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    res = sol.zigzagLevelOrder(root)
    print(res)


if __name__ == '__main__':
    main()
