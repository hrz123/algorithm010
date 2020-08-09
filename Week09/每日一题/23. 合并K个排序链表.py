# 23. 合并K个排序链表.py


# Definition for singly-linked list.
import heapq
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        heap = [(l.val, i) for i, l in enumerate(lists) if l]
        heapq.heapify(heap)
        while heap:
            _, i = heapq.heappop(heap)
            cur.next = lists[i]
            cur = cur.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        return dummy.next


def main():
    pass


if __name__ == '__main__':
    main()
