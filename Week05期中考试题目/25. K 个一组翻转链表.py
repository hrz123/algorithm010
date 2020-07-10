# 25. K 个一组翻转链表.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于k
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex  # 重复
            pre = tail
            head = nex
        return dummy.next

    def reverse(self, head, tail):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head


def print_all(head: ListNode):
    if not head:
        print(str(None))
    elif not head.next:
        print(str(head.val))
    else:
        print(str(head.val) + '->', end='')
        print_all(head.next)


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sol = Solution()
    res = sol.reverseKGroup(head, 2)
    print_all(res)


if __name__ == '__main__':
    main()
