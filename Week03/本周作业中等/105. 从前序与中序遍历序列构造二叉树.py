# 105. 从前序与中序遍历序列构造二叉树.py

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 先来了解以下前序遍历和中序遍历是什么。
# - 前序遍历：遍历顺序为 父节点 -> 左子节点 -> 右子节点
# - 中序遍历：遍历顺序为 左子节点 -> 父节点 -> 右子节点

# 我们可以发现：前序遍历的第一个元素为根节点，而在中序遍历中，该根节点所在位置的左侧为左子树，
# 右侧为右子树。

# 例如在例题中：
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# preorder的第一个元素3是整棵树的根节点。
# inorder中3的左侧[9]是树的左子树，
# 右侧 [15,20,7]构成了树的右子树。
# 所以构建二叉树的问题本质上就是：
# 1.找到各个子树的根节点root
# 2.构建该根节点的左子树
# 3.构建该根节点的右子树
# 整个过程可以用递归来完成

# 第一遍做法

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.r = None
#         self.r = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # 前序遍历第一个值为根节点
            root = TreeNode(preorder[0])
            # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
            mid = inorder.index(preorder[0])
            # 构建左子树
            root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
            # 构建右子树
            root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

            return root


# 第二遍改进
# 对输入preorder有影响
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # 前序遍历的第一个值为根节点
            root = TreeNode(preorder.pop(0))
            # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
            mid = inorder.index(root.val)
            # 构建左子树
            root.left = self.buildTree(preorder, inorder[:mid])
            # 构建右子树
            root.right = self.buildTree(preorder, inorder[mid + 1:])

            return root


# 这样每次都会形成新的数组
# 如果只用索引的话可以更省空间
# 更好的解法，用hashmap代替数组查找索引，并用指针指向节点，而非创建数组
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(
                preorder_left: int,
                preorder_right: int,
                inorder_left: int,
                inorder_right: int
        ) -> TreeNode or None:
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中
            # 「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1,
                                    preorder_left + size_left_subtree,
                                    inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中
            # 「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1,
                                     preorder_right, inorder_root + 1,
                                     inorder_right)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)


# 终极的做法，省去了用hashmap寻找索引
# 思路
# 考虑输入
# preorder: [1, 2, 4, 5, 3, 6]
# inorder: [4, 2, 5, 1, 6, 3]
# 明显的构造树的方式是
# 1.使用preorder的第一个元素，也就是1，作为根
# 2.在inorder中查找它
# 3.用它分隔inorder，这里是[4,2,5], [6,3]
# 4.分隔剩余的preorder为两个部分，都和inorder的部分一样大，这里是[2,4,5]和[3,6]
# 5.使用preorder=[2,4,5] inorder=[4,2,5]添加为左子树
# 6.使用preorder=[3,6] inorder=[6,3]添加为右子树

# 但是考虑到最坏的情况，一个不平衡的树，并且是向左的一条线。
# 那么inorder是preorder的反序，那么在inorder中查找，就是O(n^2)的总共的时间复杂度
# 另外，取决于你怎么分隔数组，有可能你的空间复杂度也是O(n^2)
# 可以使用一个hashmap使查询的总时间将为O(n)。
# 但是这样使用了O(n)的额外空间。
# 并且同样也有分隔时的空间问题。
# 为了解决这个，你可以在preorder和inorder中使用指针。
# 并且使用指针，你同样也可以不使用value_to_index的map。

# 再考虑一下这个例子。不从inorder中查询1，不把数组分隔成部分并在它们上面递归。
# 就在整体的剩余数组上递归并且在你在inorder上遇到1时停止。
# 思路就是这样。
# 每一个递归都被告知停止点，它也告诉它的子调用停止点。
# 它给它的左子调用它自己的root value作为停止点，
# 给它的右子调用它父亲的停止点作为停止点

# 对preorder, inorder有改动(reverse)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.append(None)
        inorder.reverse()

        return build(None)


# 同样解法的javascript写法
# var buildTree = function(preorder, inorder) {
#     p = start = 0
#     build = function(stop) {
#         if (inorder[start] != stop) {
#             var root = new TreeNode(preorder[p++])
#             root.r = build(root.val)
#             start++
#             root.r = build(stop)
#             return root
#         }
#         return null
#     }
#     return build()
# };

# 以下为自我练习
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        def helper(pl, pr, il, ir):
            if pl == pr:
                return
            root = TreeNode(preorder[pl])
            idx = inorder.index(root.val)

            root.left = helper(pl + 1, pl + idx - il + 1, il, idx)
            root.right = helper(pl + idx - il + 1, pr, idx + 1, ir)
            return root

        size = len(preorder)
        return helper(0, size, 0, size)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.append(None)
        inorder.reverse()

        return build(None)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def dfs(pl, pr, il, ir):
            if pl > pr:
                return
            root = TreeNode(preorder[pl])
            mid = 0
            for i in range(il, ir + 1):
                if inorder[i] == root.val:
                    mid = i
                    break
            root.left = dfs(pl + 1, pl + mid - il, il, mid - 1)
            root.right = dfs(pl + mid - il + 1, pr, mid + 1, ir)
            return root

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)


# 非常棒的写法
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.append(None)
        inorder.reverse()

        return build(None)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.append(None)
        inorder.reverse()
        return build(None)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.append(None)
        inorder.reverse()

        return build(None)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(l1, r1, l2, r2):
            if l1 > r1:
                return
            root = TreeNode(preorder[l1])
            mid = l2
            while mid <= r2:
                if inorder[mid] == root.val:
                    break
                mid += 1
            root.left = helper(l1 + 1, l1 + mid - l2, l2, mid - 1)
            root.right = helper(l1 + mid - l2 + 1, r1, mid + 1, r2)
            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        ind = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:ind + 1], inorder[:ind])
        root.right = self.buildTree(preorder[ind + 1:], inorder[ind + 1:])
        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.append(None)
        inorder.reverse()
        return build(None)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.append(None)
        inorder.reverse()
        return build(None)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        ind = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:ind + 1], inorder[:ind])
        root.right = self.buildTree(preorder[ind + 1:], inorder[ind + 1:])
        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.append(None)
        inorder.reverse()
        return build(None)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.append(None)
        inorder.reverse()
        return build(None)


def main():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    sol = Solution()
    res = sol.buildTree(preorder, inorder)

    def print_tree(root):
        if not root:
            print('#', end=' ')
            return
        print(root.val, end=" ")
        print_tree(root.left)
        print_tree(root.right)

    print_tree(res)


if __name__ == '__main__':
    main()
