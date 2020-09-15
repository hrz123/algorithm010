# 剑指 Offer 36. 二叉搜索树与双向链表.py


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        head = node = stack.pop()
        pre = node
        node = node.right
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            pre.right = node
            node.left = pre
            pre = node
            node = node.right
        pre.right = head
        head.left = pre
        return head


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        stack = []
        while root:
            stack.append(root)
            root = root.left
        head = root = stack.pop()
        pre = root
        root = root.right
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            root.left = pre
            pre.right = root
            pre = root
            root = root.right
        pre.right = head
        head.left = pre
        return head


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = []
        while root:
            stack.append(root)
            root = root.left
        head = pre = root = stack.pop()
        root = root.right
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            pre.right = root
            root.left = pre
            pre = root
            root = root.right
        pre.right = head
        head.left = pre
        return head


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = []
        while root:
            stack.append(root)
            root = root.left
        head = pre = stack.pop()
        root = pre.right
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            pre.right = root
            root.left = pre
            pre = root
            root = root.right
        pre.right = head
        head.left = pre
        return head


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = []
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        head = pre = root
        root = root.right
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            pre.right = root
            root.left = pre
            pre = root
            root = root.right
        head.left = pre
        pre.right = head
        return head


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = []
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        head = pre = root
        root = root.right
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            pre.right = root
            root.left = pre
            pre = root
            root = root.right
        head.left = pre
        pre.right = head
        return head


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = []
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        head = pre = root
        root = root.right
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            pre.right = root
            root.left = pre
            pre = root
            root = root.right
        head.left = pre
        pre.right = head
        return head


# 本文解法基于性质：二叉搜索树的中序遍历为递增序列
# 将二查搜索树转换成一个"排序的循环双向链表"，其中包含三个要素：
# 1.排序链表：节点应从小到大排列，因此应使用 中序遍历 "从小到大"访问树的节点。
# 2.双向链表：在构建相邻节点（设前驱节点pre，当前节点cur）关系时，不仅应pre.right = cur
# 也应该cur.left = pre
# 3.循环链表：设链表头节点head和尾节点tail，则应该构建head.left=tail和tail.right=head

# 中序遍历为"左、根、右"顺序，递归实现代码如下：
# def dfs(root):
#     if not root:
#         return
#     print(root.left)
#     print(root.val)
#     print(root.right)

# 根据以上分析，考虑使用中序遍历访问树的各节点cur；并在访问每个节点时构建cur和前驱节点pre
# 的引用指向；中序遍历完成后，最后构建头节点和尾节点的引用指向即可。
# 算法流程：
# dfs(cur):递归法中序遍历
# 1.终止条件：当节点cur为空，代表越过叶节点，直接返回；
# 2.递归左子树，即dfs(cur.left)
# 3.构建链表：
#   1.当pre为空时：代表正在访问链表头节点，记为head
#   2.当pre不为空时：修改双向节点引用是，即pre.right = cur, cur.left = pre;
#   3.保存cur：更新pre = cur，即节点cur是后继节点的pre
# 3.递归右子树，即dfs(cur.right)
# treeToDoublyList(root):
# 1.特例处理：若节点root为空，则直接返回；
# 2.初始化：空节点为pre；
# 3.转化为双向链表：调用dfs(root)
# 4.构建循环链表：中序遍历完成后，head指向头节点，pre指向尾节点，因此修改head和pre
#   的双向节点引用即可。
# 5.返回值：返回链表的头节点head即可
# 复杂度分析
#   时间复杂度O(n)：N为二叉树的节点数，中序遍历需要访问所有节点
#   空间复杂度O(n)：最差情况下，即树退化为链表时，递归深度达到N，系统使用O(n)栈空间
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            nonlocal pre, head
            if pre:
                pre.right = cur
                cur.left = pre
            else:
                head = cur
            pre = cur
            dfs(cur.right)

        pre, head = None, None
        dfs(root)
        head.left = pre
        pre.right = head
        return head


def main():
    pass


if __name__ == '__main__':
    main()
