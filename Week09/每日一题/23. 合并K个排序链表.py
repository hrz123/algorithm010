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


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        # 这里的i为了排序
        heap = [(l.val, i, l) for i, l in enumerate(lists) if l]
        heapq.heapify(heap)
        while heap:
            val, ind, l = heapq.heappop(heap)
            cur.next = l
            if l.next:
                l = l.next
                heapq.heappush(heap, (l.val, ind, l))
            cur = cur.next
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        n = len(lists)
        return self.merge(lists, 0, n - 1)

    def merge(self, lists, l, r):
        if l >= r:
            return lists[l]
        mid = l + ((r - l) >> 1)
        l1 = self.merge(lists, l, mid)
        l2 = self.merge(lists, mid + 1, r)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next


# 归并的做法
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        n = len(lists)
        return self.merge(lists, 0, n - 1)

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        mid = l + ((r - l) >> 1)
        l1 = self.merge(lists, l, mid)
        l2 = self.merge(lists, mid + 1, r)
        return self.mergeTwoList(l1, l2)

    def mergeTwoList(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        mid = l + ((r - l) >> 1)
        l1 = self.merge(lists, l, mid)
        l2 = self.merge(lists, mid + 1, r)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(l.val, i) for i, l in enumerate(lists) if l]
        heapq.heapify(heap)
        dummy = ListNode(0)
        cur = dummy
        while heap:
            _, i = heapq.heappop(heap)
            cur.next = lists[i]
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
            cur = cur.next
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        mid = l + ((r - l) >> 1)
        l1 = self.merge(lists, l, mid)
        l2 = self.merge(lists, mid + 1, r)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(l.val, i) for i, l in enumerate(lists) if l]
        heapq.heapify(heap)
        dummy = ListNode(0)
        cur = dummy
        while heap:
            _, i = heapq.heappop(heap)
            cur.next = lists[i]
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
            cur = cur.next
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        mid = l + ((r - l) >> 1)
        l1 = self.merge(lists, l, mid)
        l2 = self.merge(lists, mid + 1, r)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        mid = l + ((r - l) >> 1)
        l1 = self.merge(lists, l, mid)
        l2 = self.merge(lists, mid + 1, r)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        mid = l + ((r - l) >> 1)
        l1 = self.merge(lists, l, mid)
        l2 = self.merge(lists, mid + 1, r)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(l.val, i) for i, l in enumerate(lists) if l]
        heapq.heapify(heap)
        dummy = ListNode(0)
        cur = dummy
        while heap:
            _, i = heapq.heappop(heap)
            cur.next = lists[i]
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
            cur = cur.next
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        mid = l + ((r - l) >> 1)
        l1 = self.merge(lists, l, mid)
        l2 = self.merge(lists, mid + 1, r)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next


def main():
    pass


if __name__ == '__main__':
    main()
