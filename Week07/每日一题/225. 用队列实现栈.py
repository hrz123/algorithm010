# 225. 用队列实现栈.py
from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return self.q2.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        val = self.q1.popleft()
        self.q2.append(val)
        self.q1, self.q2 = self.q2, self.q1
        return val

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0 and len(self.q2) == 0


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return -1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return self.q2.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return -1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        res = self.q2.popleft()
        self.q1.append(res)
        return res

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
def main():
    pass


if __name__ == '__main__':
    main()
