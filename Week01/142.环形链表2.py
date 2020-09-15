# 142.环形链表2.py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow = head.next
            fast = head.next.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return

        fast = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return slow


# 以下为自我练习
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow = head.next
            fast = head.next.next

            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return

        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow = fast = head
            slow = slow.next
            fast = fast.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        slow = head.next
        fast = head.next.next
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        if slow != fast:
            return
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow = fast = head
            slow = slow.next
            fast = fast.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow = head.next
            fast = head.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow = head.next
            fast = head.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        slow = head.next
        fast = head.next.next
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        if slow != fast:
            return
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        slow = head.next
        fast = head.next.next
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        if slow != fast:
            return
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow = head.next
            fast = head.next.next
            while fast != slow:
                slow = slow.next
                fast = fast.next.next
        except:
            return
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        slow = head.next
        fast = head.next.next
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        if slow != fast:
            return
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        slow = head.next
        fast = slow.next
        while fast and fast.next:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next
        if slow != fast:
            return
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow, fast = head.next, head.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow, fast = head.next, head.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        slow, fast = head.next, head.next.next
        while fast and fast.next:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next
        if slow != fast:
            return
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow


def main():
    pass


if __name__ == '__main__':
    main()
