# 141.环形链表.py
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


# 以下为自我练习
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            slow = head
            fast = head.next

            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


def main():
    pass


if __name__ == '__main__':
    main()
