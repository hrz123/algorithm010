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
