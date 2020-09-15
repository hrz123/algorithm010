# 1014. 最佳观光组合.py
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        pre, cur = 0, 0
        for i in range(len(A)):
            cur = max(A[i] - i + pre, cur)
            pre = max(pre, A[i] + i)
        return cur


# 以下为自我练习
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        pre, res = 0, 0
        for i in range(len(A)):
            res = max(res, A[i] - i + pre)
            pre = max(pre, A[i] + i)
        return res


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res, pre = 0, 0
        for i in range(len(A)):
            res = max(res, A[i] - i + pre)
            pre = max(pre, A[i] + i)
        return res


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        pre, cur = 0, 0
        for i in range(len(A)):
            cur = max(cur, A[i] - i + pre)
            pre = max(pre, A[i] + i)
        return cur


#
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        pre, res = 0, 0
        for i, a in enumerate(A):
            res = max(res, a - i + pre)
            pre = max(pre, a + i)
        return res


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        pre, cur = 0, 0
        for i, a in enumerate(A):
            cur = max(cur, pre + a - i)
            pre = max(pre, a + i)
        return cur


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        pre, cur = 0, 0
        for i, num in enumerate(A):
            cur = max(cur, num - i + pre)
            pre = max(pre, num + i)
        return cur


def main():
    sol = Solution()
    nums = [8, 1, 5, 2, 6]
    res = sol.maxScoreSightseeingPair(nums)
    print(res)


if __name__ == '__main__':
    main()
