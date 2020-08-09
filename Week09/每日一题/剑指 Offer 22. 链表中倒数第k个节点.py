# 剑指 Offer 22. 链表中倒数第k个节点.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 拿到size后，知道正向是第几个元素，正向再遍历一遍
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        h, size = head, 0
        while h:
            h, size = h.next, size + 1
        k = size - k
        h = head
        while k:
            h, k = h.next, k - 1
        return h


# 用一个fast指针，先走k步，然后slow指针和fast指针同时走，fast到NULL的时候，
# slow指针就是我们要求的节点
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = slow = head
        for _ in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow


def main():
    pass


if __name__ == '__main__':
    main()
