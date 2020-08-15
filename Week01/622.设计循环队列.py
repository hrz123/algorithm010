# 622.设计循环队列.py


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the mask of the queue to be k.
        """
        self.front = 0
        self.rear = 0
        self.capacity = k + 1
        self.data = [0] * self.capacity

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.data[self.rear - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.rear + 1) % self.capacity == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


# 以下为自我练习
# 底层用数组实现
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the mask of the queue to be k.
        """
        self.size = k + 1
        self.array = [0] * self.size
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.array[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.array[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.array[self.rear - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.rear + 1) % self.size == self.front


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the mask of the queue to be k.
        """
        self.cap = k
        self.front = 0
        self.rear = 0
        self.data = [0] * (k + 1)
        self.size = k + 1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.data[(self.rear - 1) % self.size]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.rear + 1) % self.size == self.front


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the mask of the deque to be k.
        """
        self.front = 0
        self.rear = 0
        self.cap = k
        self.size = k + 1
        self.data = [0] * self.size

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.size
        self.data[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.size
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.data[(self.rear - 1) % self.size]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.rear + 1) % self.size == self.front


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.cap = k + 1
        self.arr = [0] * self.cap
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.cap
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.cap
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.arr[(self.rear - 1) % self.cap]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.rear + 1) % self.cap == self.front


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k + 1
        self.data = [0] * self.size
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.data[(self.rear - 1) % self.size]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.rear + 1) % self.size == self.front


def main():
    obj = MyCircularQueue(3)
    param_1 = obj.enQueue(1)
    print(param_1)
    param_1 = obj.enQueue(2)
    print(param_1)
    param_1 = obj.enQueue(3)
    print(param_1)
    param_2 = obj.deQueue()
    print(param_2)
    param_3 = obj.Front()
    print(param_3)
    param_4 = obj.Rear()
    print(param_4)
    param_5 = obj.isEmpty()
    print(param_5)
    param_6 = obj.isFull()
    print(param_6)


if __name__ == '__main__':
    main()
