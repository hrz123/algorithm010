# 382. 链表随机节点.py


# Definition for singly-linked list.
import random


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        count = 0
        reserve = 0
        cur = self.head
        while cur:
            count += 1
            if random.randint(1, count) == count:
                reserve = cur.val
            cur = cur.next
        return reserve


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        count = 0
        cur = self.head
        res = 0
        while cur:
            count += 1
            if random.randint(1, count) == count:
                res = cur.val
            cur = cur.next
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

def main():
    head = ListNode(10)
    head.next = ListNode(1)
    head.next.next = ListNode(10)
    head.next.next.next = ListNode(20)
    head.next.next.next.next = ListNode(100)
    sol = Solution(head)
    res = sol.getRandom()
    print(res)


if __name__ == '__main__':
    main()
