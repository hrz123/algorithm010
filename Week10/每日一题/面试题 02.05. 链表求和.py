# 面试题 02.05. 链表求和.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            carry, val = divmod(n1 + n2 + carry, 10)
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            cur.next = ListNode(1)
        return dummy.next


# 进阶
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1, v2 = 0, 0
        while l1:
            v1 = v1 * 10 + l1.val
            l1 = l1.next
        while l2:
            v2 = v2 * 10 + l2.val
            l2 = l2.next
        val = v1 + v2
        pre, cur = None, None
        while val:
            val, mod = divmod(val, 10)
            cur = ListNode(mod)
            cur.next = pre
            pre = cur
        return cur


def main():
    sol = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l2 = ListNode(2)
    l2.next = ListNode(8)
    l3 = sol.addTwoNumbers(l1, l2)
    while l3:
        print(l3.val)
        l3 = l3.next


if __name__ == '__main__':
    main()
