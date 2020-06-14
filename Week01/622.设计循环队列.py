# 622.设计循环队列.py


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
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

def main():
    obj = MyCircularQueue(3)
    param_1 = obj.enQueue(1)
    param_1 = obj.enQueue(2)
    param_1 = obj.enQueue(3)
    param_2 = obj.deQueue()
    param_3 = obj.Front()
    param_4 = obj.Rear()
    param_5 = obj.isEmpty()
    param_6 = obj.isFull()


if __name__ == '__main__':
    main()
