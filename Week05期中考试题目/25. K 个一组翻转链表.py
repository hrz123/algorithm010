# 25. K 个一组翻转链表.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于k
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nxt = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nxt  # 重复
            pre = tail
            head = nxt
        return dummy.next

    def reverse(self, head, tail):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head


# 以下为自我练习
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        while head:
            tail = pre
            # 查看剩余部分长度是否大于k
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nxt = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新串联起来
            pre.next = head
            tail.next = nxt
            pre = tail
            head = nxt
        return dummy.next

    def reverse(self, head, tail):
        prev = tail.next
        cur = head
        while prev != tail:
            cur.next, cur, prev = prev, cur.next, cur
        return tail, head


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nxt = tail.next
            head, tail = self._reverse(head, tail)
            pre.next = head
            pre = tail
            head = nxt
        return dummy.next

    def _reverse(self, head, tail):
        prev = tail.next
        cur = head
        while prev != tail:
            cur.next, prev, cur = prev, cur, cur.next
        return tail, head


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nxt = tail.next
            head, tail = self._reverse(head, tail)
            pre.next = head
            pre = tail
            head = nxt
        return dummy.next

    def _reverse(self, head, tail):
        pre = tail.next
        cur = head
        while pre != tail:
            cur.next, pre, cur = pre, cur, cur.next
        return tail, head


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nxt = tail.next
            head, tail = self._reverse(head, tail)
            pre.next = head
            pre = tail
            head = nxt
        return dummy.next

    def _reverse(self, head, tail):
        pre = tail.next
        cur = head
        while pre != tail:
            cur.next, pre, cur = pre, cur, cur.next
        return tail, head


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nxt = tail.next
            head, tail = self._reverse(head, tail)
            pre.next = head
            pre = tail
            head = nxt
        return dummy.next

    def _reverse(self, head, tail):
        pre = tail.next
        cur = head
        while pre != tail:
            cur.next, pre, cur = pre, cur, cur.next
        return tail, head


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nxt = tail.next
            head, tail = self._reverse(head, tail)
            pre.next = head
            pre = tail
            head = nxt
        return dummy.next

    def _reverse(self, head, tail):
        pre = tail.next
        cur = head
        while pre != tail:
            cur.next, pre, cur = pre, cur, cur.next
        return tail, head


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nxt = tail.next
            head, tail = self._reverse(head, tail)
            pre.next = head
            pre = tail
            head = nxt
        return dummy.next

    def _reverse(self, head, tail):
        pre = tail.next
        cur = head
        while pre != tail:
            cur.next, pre, cur = pre, cur, cur.next
        return tail, head


def main():
    def print_all(head: ListNode):
        if not head:
            print(str(None))
        elif not head.next:
            print(str(head.val))
        else:
            print(str(head.val) + '->', end='')
            print_all(head.next)

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sol = Solution()
    res = sol.reverseKGroup(head, 2)
    print_all(res)


if __name__ == '__main__':
    main()
