# 面试题 02.01. 移除重复节点.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 解法1：使用临时缓冲区。思路比较简单不说了。
# 解法2：不使用临时缓冲区。两种循环。一重循环遍历链表，另一重循环去掉于第一重循环相同值的节点。

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        occurred = {head.val}
        pos = head
        # 枚举前驱节点
        while pos.next:
            # 当前待删除节点
            cur = pos.next
            if cur.val not in occurred:
                occurred.add(cur.val)
                pos = pos.next
            else:
                pos.next = pos.next.next
        return head


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        ob = head
        while ob:
            oc = ob
            while oc.next:
                if oc.next.val == ob.val:
                    oc.next = oc.next.next
                else:
                    oc = oc.next
            ob = ob.next
        return head


def main():
    pass


if __name__ == '__main__':
    main()
