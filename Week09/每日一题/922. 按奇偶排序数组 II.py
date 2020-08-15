# 922. 按奇偶排序数组 II.py
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        o, e = 1, 0
        for n in A:
            if n & 1:
                res[o] = n
                o += 2
            else:
                res[e] = n
                e += 2
        return res


# 以下为自我练习
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        o, e = 1, 0
        for a in A:
            if a & 1:
                res[o] = a
                o += 2
            else:
                res[e] = a
                e += 2
        return res


# 以下为自我练习
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i, j = 0, 1
        n = len(A)
        while i < n and j < n:
            while i < n and not A[i] & 1:
                i += 2
            while j < n and A[j] & 1:
                j += 2
            if i < n and j < n:
                A[i], A[j] = A[j], A[i]
            i += 2
            j += 2
        return A


class Solution(object):
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] & 1:
                while A[j] & 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


class Solution(object):
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] & 1:
                while A[j] & 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


class Solution(object):
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] & 1:
                while A[j] & 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


def main():
    sol = Solution()
    a = [4, 2, 5, 7]
    res = sol.sortArrayByParityII(a)
    print(res)
    a = [2, 3]
    res = sol.sortArrayByParityII(a)
    print(res)


if __name__ == '__main__':
    main()
