# 977. 有序数组的平方.py
import bisect
from typing import List


# 1.解法1，乘方，排序，假设乘方是O(1)的，排序是O(nlogn)的
# 2。 先找到正负分解线 logn
#     用两个指针指向正还是负
#     不停移动 O(m)
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        zero_index = bisect.bisect_left(A, 0)
        l, r = zero_index - 1, zero_index
        i = 0
        while r < n:
            if l >= 0 and -A[l] < A[r]:
                res[i] = A[l] * A[l]
                l -= 1
            else:
                res[i] = A[r] * A[r]
                r += 1
            i += 1
        while l >= 0:
            res[i] = A[l] * A[l]
            l -= 1
            i += 1
        return res


# 以下为自我练习
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        zero_index = bisect.bisect_left(A, 0)
        l, r = zero_index - 1, zero_index
        res = [0] * n
        i = 0
        while r < n:
            while l >= 0 and -A[l] <= A[r]:
                res[i] = A[l] * A[l]
                l -= 1
                i += 1
            res[i] = A[r] * A[r]
            r += 1
            i += 1
        while l >= 0:
            res[i] = A[l] * A[l]
            l -= 1
            i += 1
        return res


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        index0 = bisect.bisect_left(A, 0)
        l, r = index0 - 1, index0
        n = len(A)
        res = [0] * n
        i = 0
        while r < n:
            while l >= 0 and -A[l] < A[r]:
                res[i] = A[l] * A[l]
                i += 1
                l -= 1
            res[i] = A[r] * A[r]
            i += 1
            r += 1
        while l >= 0:
            res[i] = A[l] * A[l]
            i += 1
            l -= 1
        return res


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        ind0 = bisect.bisect_left(A, 0)
        l, r = ind0 - 1, ind0
        res = [0] * n
        i = 0
        while r < n:
            while l >= 0 and A[l] * A[l] <= A[r] * A[r]:
                res[i] = A[l] * A[l]
                i += 1
                l -= 1
            res[i] = A[r] * A[r]
            i += 1
            r += 1
        while l >= 0:
            res[i] = A[l] * A[l]
            i += 1
            l -= 1
        return res


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i0 = bisect.bisect_left(A, 0)
        l, r = i0 - 1, i0
        n = len(A)
        res = [0] * n
        i = 0
        while r < n:
            while l >= 0 and A[l] * A[l] <= A[r] * A[r]:
                res[i] = A[l] * A[l]
                i += 1
                l -= 1
            res[i] = A[r] * A[r]
            i += 1
            r += 1
        while l >= 0:
            res[i] = A[l] * A[l]
            i += 1
            l -= 1
        return res


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i0 = bisect.bisect_left(A, 0)
        l, r = i0 - 1, i0
        n = len(A)
        res = [0 for _ in range(n)]
        i = 0
        while r < n:
            while l >= 0 and A[l] * A[l] <= A[r] * A[r]:
                res[i] = A[l] * A[l]
                i += 1
                l -= 1
            res[i] = A[r] * A[r]
            i += 1
            r += 1
        while l >= 0:
            res[i] = A[l] * A[l]
            i += 1
            l -= 1
        return res


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        loc = bisect.bisect_left(A, 0)
        n = len(A)
        l, r = loc - 1, loc
        res = [0] * n
        c = 0
        while r < n:
            while l >= 0 and A[l] * A[l] < A[r] * A[r]:
                res[c] = A[l] * A[l]
                c += 1
                l -= 1
            res[c] = A[r] * A[r]
            c += 1
            r += 1
        while l >= 0:
            res[c] = A[l] * A[l]
            c += 1
            l -= 1
        return res


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        loc = bisect.bisect_left(A, 0)
        l, c = loc - 1, 0
        for r in range(loc, n):
            while l >= 0 and A[l] ** 2 <= A[r] ** 2:
                res[c] = A[l] ** 2
                c += 1
                l -= 1
            res[c] = A[r] ** 2
            c += 1
        while l >= 0:
            res[c] = A[l] ** 2
            c += 1
            l -= 1
        return res


def main():
    sol = Solution()

    nums = [-4, -1, 0, 3, 10]
    res = sol.sortedSquares(nums)
    print(res)


if __name__ == '__main__':
    main()
