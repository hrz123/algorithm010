# 146.LRU缓存机制.py

from typing import Dict


class DLinkedNode(object):
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity: int):
        self.cache: Dict[int, DLinkedNode] = {}
        # 使用伪头部和伪尾部节点
        self.head: DLinkedNode = DLinkedNode()
        self.tail: DLinkedNode = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity: int = capacity
        self.size: int = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果key存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def moveToHead(self, node: DLinkedNode) -> None:
        self.removeNode(node)
        self.addToHead(node)

    def removeNode(self, node: DLinkedNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node: DLinkedNode) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeTail(self) -> DLinkedNode:
        node = self.tail.prev
        self.removeNode(node)
        return node


# 以下为自我练习

# 分析
# get要实现的操作
# get要实现的操作有
# 查看key是否在hashmap中（这里因为get操作多的话，hashmap是最好的数据结构）
# 如果在hashmap中，将对应的节点放在缓存的头部（这里因为要经常改变节点在容器中的位置）
# 链表是最好的选择。
# 操作为moveToHead(node)
# 分为两个小操作是删除当前结点removeNode(node), 在头部加入addToHead(node)

# 因为是通过node的地址删除node，如果能知道node的前序节点会更快，所以链表用双向链表更好

# put要实现的操作
# 首先看put的key是否在hashmap中
# 如果在
# 将node移到链表首部，moveToHead(node)
# 将node的value更新
# 如果不在
# 在链表首部添加元素
# 在hashmpa中添加节点
# 链表的size += 1
# 如果链表的size大于了capacity，在链表尾部删除元素
# delete = removeTail()
# self.cache.pop(delete.key)
# self.size -= 1


# 下面开始coding

class DLinkedNode(object):
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.moveToHead(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)

        else:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeNode(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def main():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)
    assert lru.get(1) == -1
    assert lru.get(3) == 3


if __name__ == '__main__':
    main()
