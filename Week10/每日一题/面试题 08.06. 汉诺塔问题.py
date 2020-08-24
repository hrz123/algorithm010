# 面试题 08.06. 汉诺塔问题.py
from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        self.move(n, A, B, C)

    def move(self, n, A, B, C):
        if n == 1:
            C.append(A.pop())
            return
        self.move(n - 1, A, C, B)
        C.append(A.pop())
        self.move(n - 1, B, A, C)


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        return self.helper(n, A, B, C)

    def helper(self, n, A, B, C):
        if n == 1:
            C.append(A.pop())
            return
        self.helper(n - 1, A, C, B)
        C.append(A.pop())
        self.helper(n - 1, B, A, C)


def main():
    sol = Solution()
    A = list(range(10, -1, -1))
    B = []
    C = []
    sol.hanota(A, B, C)
    print(C)


if __name__ == '__main__':
    main()
