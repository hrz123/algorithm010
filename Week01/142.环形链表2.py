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


def main():
    pass


if __name__ == '__main__':
    main()
