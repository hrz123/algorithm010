# 147. 对链表进行插入排序.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            p = head.next
            pre, cur = dummy, dummy.next
            while cur.val < p.val:
                pre, cur = cur, cur.next
            if cur == p:
                head = head.next
            else:
                head.next = p.next
                p.next = cur
                pre.next = p
        return dummy.next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            p = head.next
            pre, cur = dummy, dummy.next
            while cur.val < p.val:
                pre, cur = cur, cur.next
            if cur == p:
                head = head.next
            else:
                head.next = p.next
                p.next = cur
                pre.next = p
        return dummy.next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            p = head.next
            pre, cur = dummy, dummy.next
            while cur.val < p.val:
                pre, cur = cur, cur.next
            if cur == p:
                head = head.next
            else:
                head.next = p.next
                p.next = cur
                pre.next = p
        return dummy.next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            p = head.next
            pre, cur = dummy, dummy.next
            while cur.val < p.val:
                pre, cur = cur, cur.next
            if cur == p:
                head = head.next
            else:
                head.next = p.next
                p.next = cur
                pre.next = p
        return dummy.next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            p = head.next
            # 测试样例中，很多都是排序好的，增加这一步判断，可用于提速
            if p.val >= head.val:
                head = head.next
                continue
            pre, cur = dummy, dummy.next
            while cur.val < p.val:
                pre, cur = cur, cur.next
            if cur == p:
                head = head.next
            else:
                head.next = p.next
                p.next = cur
                pre.next = p
        return dummy.next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            p = head.next
            # 防止测试样例中，很多都是排好序的，增加这一步判断，可用于提速
            if p.val >= head.val:
                head = head.next
                continue
            pre, cur = dummy, dummy.next
            while cur.val < p.val:
                pre, cur = cur, cur.next
            head.next = p.next
            p.next = cur
            pre.next = p
        return dummy.next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = head
        while p and p.next:
            c = p.next
            if c.val >= p.val:
                p = p.next
            else:
                pre, cur = dummy, dummy.next
                while cur.val < c.val:
                    pre, cur = cur, cur.next
                p.next = c.next
                c.next = cur
                pre.next = c
        return dummy.next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = head
        while p and p.next:
            c = p.next
            if c.val >= p.val:
                p = c
            else:
                pre, cur = dummy, dummy.next
                while cur.val < c.val:
                    pre, cur = cur, cur.next
                p.next = c.next
                c.next = cur
                pre.next = c
        return dummy.next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = head
        while p and p.next:
            c = p.next
            if c.val >= p.val:
                p = c
            else:
                pre, cur = dummy, dummy.next
                while cur.val < c.val:
                    pre, cur = cur, cur.next
                p.next = c.next
                c.next = cur
                pre.next = c
        return dummy.next


def main():
    sol = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(5)

    h = sol.insertionSortList(head)

    def print_all(node):
        while node:
            print(node.val, end=' ')
            node = node.next

    print_all(h)


if __name__ == '__main__':
    main()
