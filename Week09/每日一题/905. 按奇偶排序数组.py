# 905. 按奇偶排序数组.py
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        l, r = 0, n - 1
        for n in A:
            if n & 1:
                res[r] = n
                r -= 1
            else:
                res[l] = n
                l += 1
        return res


# 以下为自我练习
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l = 0
        for i in range(len(A)):
            if not A[i] & 1:
                A[i], A[l] = A[l], A[i]
                l += 1
        return A


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        l, r = 0, n - 1
        for a in A:
            if a & 1:
                res[r] = a
                r -= 1
            else:
                res[l] = a
                l += 1
        return res


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        right = 0
        n = len(A)
        for i in range(n):
            if not A[i] & 1:
                A[i], A[right] = A[right], A[i]
                right += 1
        return A


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        l = n - 1
        i = 0
        while i <= l:
            if A[i] & 1:
                A[i], A[l] = A[l], A[i]
                l -= 1
            else:
                i += 1
        return A


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        l, r = 0, n - 1
        i = 0
        while i <= r:
            if A[i] & 1:
                A[i], A[r] = A[r], A[i]
                r -= 1
            else:
                A[i], A[l] = A[l], A[i]
                i += 1
                l += 1
        return A


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] & 1 and not A[r] & 1:
                A[l], A[r] = A[r], A[l]
            if not A[l] & 1:
                l += 1
            if A[r] & 1:
                r -= 1
        return A


# 排序
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x: x & 1)
        return A


# 两边扫描
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [x for x in A if not x & 1] + [x for x in A if x & 1]


# 原地算法
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] & 1 and not A[r] & 1:
                A[l], A[r] = A[r], A[l]
                l += 1
                r -= 1
            elif not A[l] & 1:
                l += 1
            elif A[r] & 1:
                r -= 1
        return A


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] & 1 and not A[r] & 1:
                A[l], A[r] = A[r], A[l]
            if not A[l] & 1:
                l += 1
            if A[r] & 1:
                r -= 1
        return A


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] & 1 and not A[r] & 1:
                A[l], A[r] = A[r], A[l]
                l += 1
                r -= 1
            elif not A[l] & 1:
                l += 1
            elif A[r] & 1:
                r -= 1
        return A


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] & 1 and not A[r] & 1:
                A[l], A[r] = A[r], A[l]
                l += 1
                r -= 1
            elif not A[l] & 1:
                l += 1
            elif A[r] & 1:
                r -= 1
        return A


def main():
    sol = Solution()
    a = [3, 1, 2, 4]
    res = sol.sortArrayByParity(a)
    print(res)


if __name__ == '__main__':
    main()
