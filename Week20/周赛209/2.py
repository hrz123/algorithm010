# 2.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q, nq = [root], []
        flag = True
        while q:
            if flag:
                pre = float('-inf')
                for node in q:
                    if node.val & 1 == 0 or node.val <= pre:
                        return False
                    pre = node.val
                    if node.left:
                        nq.append(node.left)
                    if node.right:
                        nq.append(node.right)
            else:
                pre = float('inf')
                for node in q:
                    if node.val & 1 == 1 or node.val >= pre:
                        return False
                    pre = node.val
                    if node.left:
                        nq.append(node.left)
                    if node.right:
                        nq.append(node.right)
            q, nq = nq, []
            flag = not flag
        return True


def main():
    pass


if __name__ == '__main__':
    main()
