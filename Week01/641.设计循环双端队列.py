# 641.设计循环双端队列.py
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._front = 0
        self._rear = 0
        self._capacity = k + 1
        self._arr = [0 for _ in range(self._capacity)]

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the _front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self._front = (self._front - 1) % self._capacity
        self._arr[self._front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the _rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self._arr[self._rear] = value
        self._rear = (self._rear + 1) % self._capacity
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the _front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self._front = (self._front + 1) % self._capacity
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the _rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self._rear = (self._rear - 1) % self._capacity
        return True

    def getFront(self) -> int:
        """
        Get the _front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self._arr[self._front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self._arr[(self._rear - 1 + self._capacity) % self._capacity]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self._front == self._rear

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self._rear + 1) % self._capacity == self._front


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

def main():
    obj = MyCircularDeque(3)
    param_1 = obj.insertFront(1)
    param_2 = obj.insertLast(2)
    param_3 = obj.deleteFront()
    param_4 = obj.deleteLast()
    param_5 = obj.getFront()
    param_6 = obj.getRear()
    param_7 = obj.isEmpty()
    param_8 = obj.isFull()
    print(param_1)


if __name__ == '__main__':
    main()
