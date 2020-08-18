# 83. 删除排序链表中的重复元素.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        visited = set()
        cur = head
        prev = None
        while cur:
            if cur.val in visited:
                prev.next = cur.next
            else:
                visited.add(cur.val)
                prev = cur
            cur = cur.next
        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = head
        while pre:
            cur = pre.next
            while cur and cur.val == pre.val:
                pre.next = pre.next.next
                cur = cur.next
            pre = pre.next
        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = head
        while pre.next:
            if pre.next.val == pre.val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = head
        while pre:
            cur = pre.next
            while cur and cur.val == pre.val:
                pre.next = pre.next.next
                cur = cur.next
            pre = pre.next
        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = head
        while pre.next:
            if pre.next.val == pre.val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = head
        while pre.next:
            if pre.next.val == pre.val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = head
        while pre and pre.next:
            if pre.next.val == pre.val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, cur = head, head.next
        while pre and cur:
            if cur.val == pre.val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return head


def main():
    sol = Solution()

    a = ListNode(1)
    a.next = ListNode(1)
    a.next.next = ListNode(2)

    res = sol.deleteDuplicates(a)
    print(res.val)
    print(res.next.val)
    print(res.next.next)


if __name__ == '__main__':
    main()
