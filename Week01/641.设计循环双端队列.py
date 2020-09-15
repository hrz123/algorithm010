# 641.设计循环双端队列.py
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the mask of the deque to be k.
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


# 以下为自我练习
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the mask of the deque to be k.
        """
        self.capacity = k + 1
        self.data = [0] * self.capacity
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        # 先更新front位置
        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        # 后更新rear位置
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.capacity
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
        return self.data[(self.rear - 1) % self.capacity]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.rear + 1) % self.capacity == self.front


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the mask of the deque to be k.
        """
        self.data = [0] * (k + 1)
        self.front = 0
        self.rear = 0
        self.size = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front = (self.front - 1) % (self.size + 1)
        self.data[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % (self.size + 1)
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % (self.size + 1)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % (self.size + 1)
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
        if self.rear == 0:
            return self.data[self.size]
        return self.data[self.rear - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.rear + 1) % (self.size + 1) == self.front


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.cap = k + 1
        self.arr = [0] * self.cap
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.cap
        self.arr[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.cap
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.cap
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.cap
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[(self.rear - 1) % self.cap]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.rear + 1) % self.cap == self.front


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = k + 1
        self.data = [0] * self.size
        self.front = 0
        self.rear = 0

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


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.cap = k + 1
        self.data = [0] * self.cap
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.cap
        self.data[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.cap
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.cap
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.cap
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
        return self.data[(self.rear - 1) % self.cap]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.rear + 1) % self.cap == self.front


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.cap = k + 1
        self.data = [0] * self.cap
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.cap
        self.data[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.cap
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.cap
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.cap
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
        return self.data[(self.rear - 1) % self.cap]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.rear + 1) % self.cap == self.front


def main():
    obj = MyCircularDeque(3)
    param = obj.insertFront(1)
    print(param)
    param = obj.insertLast(2)
    print(param)
    param = obj.deleteFront()
    print(param)
    # param = obj.deleteLast()
    # print(param)

    param = obj.getFront()
    print(param)
    param = obj.getRear()
    print(param)
    param = obj.isEmpty()
    print(param)
    param = obj.isFull()
    print(param)


if __name__ == '__main__':
    main()
