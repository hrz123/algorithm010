# 92. 反转链表 II.py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        count = 1
        while cur:
            if count == m:
                head, tail = self._reverse(cur, m, n)
                pre.next = head
                break
            cur, pre = cur.next, cur
            count += 1
        return dummy.next

    def _reverse(self, head, m, n):
        pre = None
        cur = head
        for _ in range(n - m + 1):
            cur.next, pre, cur = pre, cur, cur.next
        head.next = cur
        return pre, head


# 以下为自我练习
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        rear = dummy
        for _ in range(m - 1):
            rear = rear.next
        cur = tail = rear.next
        pre = rear
        for _ in range(n - m + 1):
            cur.next, pre, cur = pre, cur, cur.next
        rear.next = pre
        tail.next = cur
        return dummy.next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        for _ in range(m - 1):
            pre, cur = cur, cur.next
        h, nxt = cur, cur.next
        for _ in range(n - m):
            nxt.next, h, nxt = h, nxt, nxt.next
        cur.next = nxt
        pre.next = h
        return dummy.next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        for _ in range(m - 1):
            pre, cur = cur, cur.next
        p, nxt = cur, cur.next
        for _ in range(n - m):
            nxt.next, cur, nxt = cur, nxt, nxt.next
        pre.next = cur
        p.next = nxt
        return dummy.next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, start = dummy, head
        for _ in range(m - 1):
            pre, start = start, start.next
        cur, nxt = start, start.next
        for _ in range(n - m):
            nxt.next, cur, nxt = cur, nxt, nxt.next
        pre.next = cur
        start.next = nxt
        return dummy.next


def main():
    sol = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    b = sol.reverseBetween(a, 2, 4)

    def print_all(a):
        while a:
            print(a.val, end="->")
            a = a.next

    print_all(b)


if __name__ == '__main__':
    main()
