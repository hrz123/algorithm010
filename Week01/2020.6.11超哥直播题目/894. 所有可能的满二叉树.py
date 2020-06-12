# 894. 所有可能的满二叉树.py
# Definition for a binary tree node.


from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N == 1:
            return [TreeNode(0)]
        res = []
        for i in range(1, N, 2):
            nLeft = i
            nRight = N - 1 - i
            for left in self.allPossibleFBT(nLeft):
                for right in self.allPossibleFBT(nRight):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)

        return res


def main():
    s = Solution()
    res = s.allPossibleFBT(5)
    print(res)


if __name__ == '__main__':
    main()
