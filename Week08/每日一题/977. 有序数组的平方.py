# 977. 有序数组的平方.py
import bisect
from typing import List


# 1.解法1，乘方，排序，假设乘方是O(1)的，排序是O(nlogn)的
# 2。 先找到正负分解线 logn
#     用两个指针指向正还是负
#     不停移动 O(n)
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


def main():
    sol = Solution()

    nums = [-4, -1, 0, 3, 10]
    res = sol.sortedSquares(nums)
    print(res)


if __name__ == '__main__':
    main()
