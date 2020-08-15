# 99. 恢复二叉搜索树.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        pre = TreeNode(float('-inf'))
        head, tail = None, None
        find_head = False
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre.val > root.val and not find_head:
                head = pre
                find_head = True
            if find_head and pre.val > root.val:
                tail = root
            pre = root
            root = root.right
        head.val, tail.val = tail.val, head.val


# morris遍历，可以O(1)空间复杂度，但是要遍历树两次，时间也是O(N)的
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        x = y = pred = None
        while root:
            if root.left:
                predecessor = root.left
                # predecessor节点就是当前root节点向左走一步，然后一直向右走至无法走为止
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                # 让 predecessor 的右指针指向 root，继续遍历左子树
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:  # 说明左子树已经访问完了，我们需要断开链接
                    if pred and root.val < pred.val:
                        y = root
                        if not x:
                            x = pred
                    pred = root
                    predecessor.right = None
                    root = root.right
            # 如果没有左孩子，则直接访问右孩子
            else:
                if pred and root.val < pred.val:
                    y = root
                    if not x:
                        x = pred
                pred = root
                root = root.right
        x.val, y.val = y.val, x.val


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        p1, p2, pre = None, None, None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and pre.val >= root.val:
                if not p1:
                    p1 = pre
                if p1:
                    p2 = root
            pre = root
            root = root.right
        p1.val, p2.val = p2.val, p1.val


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        begin, end = None, None
        pre = float('-inf')
        pred = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre > root.val:
                if not begin:
                    begin = pred
                end = root
            pre = root.val
            pred = root
            root = root.right
        begin.val, end.val = end.val, begin.val


def main():
    pass


if __name__ == '__main__':
    main()
