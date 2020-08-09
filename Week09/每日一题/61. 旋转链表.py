# 61. 旋转链表.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        size = self.get_size(head)
        k %= size
        dummy = ListNode(0)
        dummy.next = head
        new_tail = dummy
        for _ in range(size - k):
            new_tail = new_tail.next
        tail = new_tail
        while tail.next:
            tail = tail.next
        tail.next = dummy.next
        dummy.next = new_tail.next
        new_tail.next = None
        return dummy.next

    def get_size(self, head):
        s = 0
        while head:
            s += 1
            head = head.next
        return s


def main():
    sol = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    b = sol.rotateRight(a, 2)

    def print_all(a):
        while a:
            print(a.val, end="->")
            a = a.next

    print_all(b)


if __name__ == '__main__':
    main()
