# 面试题 02.01. 移除重复节点.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 解法1：使用临时缓冲区。思路比较简单不说了。
# 解法2：不使用临时缓冲区。两次循环。一重循环遍历链表，另一重循环去掉于第一重循环相同值的节点。

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


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return
        occurred = {head.val}
        pre = head
        while pre.next:
            cur = pre.next
            if cur.val in occurred:
                pre.next = pre.next.next
            else:
                occurred.add(cur.val)
                pre = pre.next
        return head


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        pre = head
        while pre:
            cur = pre
            while cur.next:
                if cur.next.val == pre.val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            pre = pre.next
        return head


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        occurred = {head.val}
        pre = head
        while pre.next:
            cur = pre.next
            if cur.val in occurred:
                pre.next = pre.next.next
            else:
                occurred.add(cur.val)
                pre = pre.next
        return head


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        pre = head
        while pre:
            cur = pre
            while cur.next:
                if cur.next.val == pre.val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            pre = pre.next
        return head


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = head
        visited = {head.val}
        while pre.next:
            if pre.next.val in visited:
                pre.next = pre.next.next
            else:
                pre = pre.next
                visited.add(pre.val)
        return head


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        pre = head
        while pre:
            cur = pre
            while cur.next:
                if cur.next.val == pre.val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            pre = pre.next
        return head


# 以下为自我练习
# 1. 使用hashmap
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        occurred = {head.val}
        pre = head
        while pre.next:
            cur = pre.next
            if cur.val in occurred:
                pre.next = pre.next.next
            else:
                occurred.add(cur.val)
                pre = pre.next
        return head


# 2.暴力删除
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        pre = head
        while pre:
            cur = pre
            while cur.next:
                if cur.next.val == pre.val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            pre = pre.next
        return head


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        visited = {head.val}
        cur = head
        while cur.next:
            if cur.next.val in visited:
                cur.next = cur.next.next
            else:
                visited.add(cur.next.val)
                cur = cur.next
        return head


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        pre = head
        while pre:
            cur = pre
            while cur.next:
                if cur.next.val == pre.val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            pre = pre.next
        return head


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        mem = set()
        while pre and pre.next:
            if pre.next.val in mem:
                pre.next = pre.next.next
            else:
                mem.add(pre.next.val)
                pre = pre.next
        return dummy.next


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        mem = set()
        pre = dummy
        while pre and pre.next:
            if pre.next.val in mem:
                pre.next = pre.next.next
            else:
                mem.add(pre.next.val)
                pre = pre.next
        return dummy.next


def main():
    sol = Solution()

    a = ListNode(1)
    a.next = ListNode(1)
    a.next.next = ListNode(2)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(2)

    b = sol.removeDuplicateNodes(a)

    def print_all(a):
        while a:
            print(a.val, end=' ')
            a = a.next

    print_all(b)


if __name__ == '__main__':
    main()
