# 109. 有序链表转换二叉搜索树.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def findmid(head, tail):
            slow = head
            fast = head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            return slow

        def helper(head, tail):
            if head == tail:
                return
            node = findmid(head, tail)
            root = TreeNode(node.val)
            root.left = helper(head, node)
            root.right = helper(node.next, tail)
            return root

        return helper(head, None)


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def find_mid(head, tail):
            slow = fast = head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            return slow

        def helper(head, tail):
            if head == tail:
                return
            node = find_mid(head, tail)
            root = TreeNode(node.val)
            root.left = helper(head, node)
            root.right = helper(node.next, tail)
            return root

        return helper(head, None)


class Solution:
    def sortedListToBST(self, head):
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        # here we get the middle point,
        # even case, like '1234', slow points to '2',
        # '3' is root, '12' belongs to m, '4' is r
        # odd case, like '12345', slow points to '2', '12'
        # belongs to m, '3' is root, '45' belongs to r
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # tmp points to root
        tmp = slow.next
        # cut down the m child
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root


# 时间复杂度：O(nlogn)
# 空间复杂度：O(logn)

class Solution:
    def sortedListToBST(self, head):
        vals = self.mapListToValues(head)

        def convertToBST(l, r):
            if l > r:
                return
            mid = l + ((r - l) >> 1)
            root = TreeNode(vals[mid])
            root.left = convertToBST(l, mid - 1)
            root.right = convertToBST(mid + 1, r)
            return root

        return convertToBST(0, len(vals) - 1)

    def mapListToValues(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals


# 时间复杂度：O(N)
# 空间复杂度：O(N)


# 中序遍历模拟
class Solution:
    def sortedListToBST(self, head):
        size = self.findSize(head)

        def convert(l, r):
            if l > r:
                return
            nonlocal head
            mid = l + ((r - l) >> 1)
            left = convert(l, mid - 1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            node.right = convert(mid + 1, r)
            return node

        return convert(0, size - 1)

    def findSize(self, head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        return c


# 时间复杂度：O(N)
# 空间复杂度：O(logN)


# 以下为自我练习
class Solution:
    def sortedListToBST(self, head):
        size = self.get_size(head)

        def convertBST(l, r):
            if l > r:
                return
            nonlocal head
            mid = l + ((r - l) >> 1)
            left = convertBST(l, mid - 1)
            node = TreeNode(head.val)
            head = head.next
            node.left = left
            node.right = convertBST(mid + 1, r)
            return node

        return convertBST(0, size - 1)

    def get_size(self, head):
        c = 0
        while head:
            c += 1
            head = head.next
        return c


class Solution:
    def sortedListToBST(self, head):
        size = self.get_size(head)

        def convertBST(l, r):
            if l > r:
                return
            nonlocal head
            mid = l + ((r - l) >> 1)
            left = convertBST(l, mid - 1)
            node = TreeNode(head.val)
            head = head.next
            node.left = left
            node.right = convertBST(mid + 1, r)
            return node

        return convertBST(0, size - 1)

    def get_size(self, head):
        c = 0
        while head:
            c += 1
            head = head.next
        return c


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def convertBST(l, r):
            if l > r:
                return
            nonlocal head
            mid = l + ((r - l) >> 1)
            left = convertBST(l, mid - 1)
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = convertBST(mid + 1, r)
            return root

        size = self.get_size(head)
        return convertBST(0, size - 1)

    def get_size(self, head):
        c = 0
        while head:
            c += 1
            head = head.next
        return c


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        h, size = head, 0
        while h:
            h, size = h.next, size + 1

        def conertBST(l, r):
            if l > r:
                return
            mid = l + ((r - l) >> 1)
            left = conertBST(l, mid - 1)
            nonlocal head
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = conertBST(mid + 1, r)
            return root

        return conertBST(0, size - 1)


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        h, length = head, 0
        while h:
            h, length = h.next, length + 1

        def convertBST(l, r):
            if l > r:
                return
            mid = l + ((r - l) >> 1)
            left = convertBST(l, mid - 1)
            nonlocal head
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = convertBST(mid + 1, r)
            return root

        return convertBST(0, length - 1)


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        h, length = head, 0
        while h:
            h, length = h.next, length + 1

        def convertBST(l, r):
            if l > r:
                return
            mid = l + ((r - l) >> 1)
            left = convertBST(l, mid - 1)
            nonlocal head
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = convertBST(mid + 1, r)
            return root

        return convertBST(0, length - 1)


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        h, size = head, 0
        while h:
            h, size = h.next, size + 1

        def convertBST(l, r):
            if l > r:
                return
            mid = l + (r - l >> 1)
            left = convertBST(l, mid - 1)
            nonlocal head
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = convertBST(mid + 1, r)
            return root

        return convertBST(0, size - 1)


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def convertBST(l, r):
            if l > r:
                return
            mid = l + (r - l >> 1)
            left = convertBST(l, mid - 1)
            nonlocal head
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = convertBST(mid + 1, r)
            return root

        h, size = head, 0
        while h:
            h, size = h.next, size + 1
        return convertBST(0, size - 1)


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)

        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid, slow.next = slow.next, None
        root = TreeNode(mid.val)
        root.left, root.right = self.sortedListToBST(
            head), self.sortedListToBST(mid.next)
        return root


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def convertBST(l, r):
            if l > r:
                return
            mid = l + (r - l >> 1)
            left = convertBST(l, mid - 1)
            nonlocal head
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = convertBST(mid + 1, r)
            return root

        h, size = head, 0
        while h:
            h, size = h.next, size + 1
        return convertBST(0, size - 1)


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def convertBST(l, r):
            if l > r:
                return
            mid = l + (r - l >> 1)
            left = convertBST(l, mid - 1)
            nonlocal head
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = convertBST(mid + 1, r)
            return root

        h, size = head, 0
        while h:
            h, size = h.next, size + 1
        return convertBST(0, size - 1)


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def convertBST(l, r):
            if l > r:
                return
            mid = l + (r - l >> 1)
            left = convertBST(l, mid - 1)
            nonlocal head
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = convertBST(mid + 1, r)
            return root

        h, size = head, 0
        while h:
            h, size = h.next, size + 1
        return convertBST(0, size - 1)


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def convertBST(l, r):
            if l > r:
                return
            mid = l + (r - l >> 1)
            left = convertBST(l, mid - 1)
            nonlocal head
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = convertBST(mid + 1, r)
            return root

        h, size = head, 0
        while h:
            h, size = h.next, size + 1
        return convertBST(0, size - 1)


def main():
    pass


if __name__ == '__main__':
    main()
