# 82. 删除排序链表中的重复元素 II.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and tmp == fast.val:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and tmp == fast.val:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and fast.val == tmp:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and fast.val == tmp:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and fast.val == tmp:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and fast.val == tmp:
                    fast = fast.next
            else:
                slow.next = fast
                slow, fast = fast, fast.next
        slow.next = fast
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and fast.val == tmp:
                    fast = fast.next
            else:
                slow.next = fast
                slow, fast = fast, fast.next
        slow.next = fast
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and fast.val == tmp:
                    fast = fast.next
            else:
                slow.next = fast
                slow, fast = fast, fast.next
        slow.next = fast
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and fast.val == tmp:
                    fast = fast.next
            else:
                slow.next = fast
                slow, fast = fast, fast.next
        slow.next = fast
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and fast.val == tmp:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and fast.val == tmp:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next


def main():
    pass


if __name__ == '__main__':
    main()
