# 剑指 Offer 59 - II. 队列的最大值.py
import queue
from collections import deque


class MaxQueue:

    def __init__(self):
        self.deque = deque()
        self.queue = queue.Queue()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans


class MaxQueue:

    def __init__(self):
        from queue import Queue
        self.queue = Queue()
        self.deq = deque()

    def max_value(self) -> int:
        return self.deq[0] if self.deq else -1

    def push_back(self, value: int) -> None:
        while self.deq and self.deq[-1] < value:
            self.deq.pop()
        self.deq.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deq:
            return -1
        value = self.queue.get()
        if value == self.deq[0]:
            self.deq.popleft()
        return value


class MaxQueue:

    def __init__(self):
        self.queue = deque()
        self.deq = deque()

    def max_value(self) -> int:
        return self.deq[0] if self.deq else -1

    def push_back(self, value: int) -> None:
        while self.deq and self.deq[-1] < value:
            self.deq.pop()
        self.deq.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.deq:
            return -1
        value = self.queue.popleft()
        if value == self.deq[0]:
            self.deq.popleft()
        return value


class MaxQueue:

    def __init__(self):
        self.queue = deque()
        self.deq = deque()

    def max_value(self) -> int:
        return self.deq[0] if self.deq else -1

    def push_back(self, value: int) -> None:
        while self.deq and self.deq[-1] < value:
            self.deq.pop()
        self.deq.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.deq:
            return -1
        value = self.queue.popleft()
        if value == self.deq[0]:
            self.deq.popleft()
        return value


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

def main():
    pass


if __name__ == '__main__':
    main()
