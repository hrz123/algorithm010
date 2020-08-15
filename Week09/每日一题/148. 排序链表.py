# 148. 排序链表.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None
        left, right = self.sortList(head), self.sortList(mid)
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, size = head, 0, 1
        while h:
            h, length = h.next, length + 1
        dummy = ListNode(0)
        dummy.next = head
        while size < length:
            pre, h = dummy, dummy.next
            while h:
                h1, i = h, size
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, size
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = size, size - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            size *= 2
        return dummy.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, size = head, 0, 1
        while h:
            h, length = h.next, length + 1
        dummy = ListNode(0)
        dummy.next = head
        while size < length:
            pre, h = dummy, dummy.next
            while h:
                h1, i = h, size
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, size
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = size, size - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            size <<= 1
        return dummy.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, size = head, 0, 1
        while h:
            h, length = h.next, length + 1
        dummy = ListNode(0)
        dummy.next = head
        while size < length:
            pre, h = dummy, dummy.next
            while h:
                h1, i = h, size
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, size
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = size, size - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            size <<= 1
        return dummy.next


# 以下为自我练习
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, size = head, 0, 1
        while h:
            h, length = h.next, length + 1
        dummy = ListNode(0)
        dummy.next = head
        while size < length:
            pre, h = dummy, dummy.next
            while h:
                h1, i = h, size
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, size
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = size, size - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            size <<= 1
        return dummy.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, size = head, 0, 1
        while h:
            h, length = h.next, length + 1
        dummy = ListNode(0)
        dummy.next = head
        while size < length:
            pre, h = dummy, dummy.next
            while h:
                h1, i = h, size
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, size
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = size, size - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            size <<= 1
        return dummy.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, size = head, 0, 1
        while h:
            h, length = h.next, length + 1
        dummy = ListNode(0)
        dummy.next = head
        while size < length:
            pre, h = dummy, dummy.next
            while h:
                h1, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                c1, c2 = size, size - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, c1, h1 = h1, c1 - 1, h1.next
                    else:
                        pre.next, c2, h2 = h2, c2 - 1, h2.next
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            size <<= 1
        return dummy.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, size = head, 0, 1
        while h:
            h, length = h.next, length + 1
        dummy = ListNode(0)
        dummy.next = head
        while size < length:
            pre, h = dummy, dummy.next
            while h:
                h1, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                c1, c2 = size, size - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            size <<= 1
        return dummy.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, size = head, 0, 1
        while h:
            h, length = h.next, length + 1
        dummy = ListNode(0)
        dummy.next = head
        while size < length:
            pre, h = dummy, dummy.next
            while h:
                h1, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                c1, c2 = size, size - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            size <<= 1
        return dummy.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, size = head, 0, 1
        while h:
            h, length = h.next, length + 1
        dummy = ListNode(0)
        dummy.next = head
        while size < length:
            pre, h = dummy, dummy.next
            while h:
                h1, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                c1, c2 = size, size - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            size <<= 1
        return dummy.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, size = head, 0, 1
        while h:
            h, length = h.next, length + 1
        dummy = ListNode(0)
        dummy.next = head
        while size < length:
            pre, h = dummy, dummy.next
            while h:
                h1, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                c1, c2 = size, size - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            size <<= 1
        return dummy.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, size = head, 0, 1
        while h:
            h, length = h.next, length + 1
        dummy = ListNode(0)
        dummy.next = head
        while size < length:
            pre, h = dummy, dummy.next
            while h:
                h1, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                c1, c2 = size, size - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            size <<= 1
        return dummy.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, size = head, 0, 1
        while h:
            h, length = h.next, length + 1
        dummy = ListNode(0)
        dummy.next = head
        while size < length:
            pre, h = dummy, dummy.next
            while h:
                h1, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, size
                while h and i:
                    h, i = h.next, i - 1
                c1, c2 = size, size - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            size <<= 1
        return dummy.next


def main():
    pass


if __name__ == '__main__':
    main()
