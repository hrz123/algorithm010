# 剑指 Offer 33. 二叉搜索树的后序遍历序列.py


class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        stack, root = [], float("inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root:
                return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()
            stack.append(postorder[i])
        return True


def main():
    pass


if __name__ == '__main__':
    main()
