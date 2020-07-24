# 55. 跳跃游戏.py
from functools import reduce
from typing import List


# 暴力搜索，穷举


# 贪心:O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        size = len(nums)
        end_reachable = size - 1
        for i in range(size - 1, -1, -1):
            if nums[i] + i >= end_reachable:
                end_reachable = i
        return end_reachable == 0


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        for i in range(len(nums)):
            if i > start:
                return False
            start = max(start, i + nums[i])
        return True


# on-liner version
class Solution:
    def canJump(self, nums):
        return reduce(lambda m, tup: max(m, tup[0] + tup[1]) * (tup[0] <= m),
                      enumerate(nums, 1), 1) > 0


# 以下为自我练习遍数
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        for i in range(len(nums)):
            if i > start:
                return False
            start = max(start, i + nums[i])
        return True


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        for i in range(len(nums)):
            if i > start:
                return False
            start = max(start, nums[i] + i)
        return True


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        for i in range(len(nums)):
            if i > start:
                return False
            start = max(start, nums[i] + i)
        return True


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        for i in range(len(nums)):
            if i > start:
                return False
            start = max(start, i + nums[i])
        return True


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        for i in range(len(nums)):
            if i > start:
                return False
            start = max(start, i + nums[i])
        return True


def main():
    nums = [2, 3, 1, 1, 4]
    sol = Solution()
    res = sol.canJump(nums)
    print(res)


if __name__ == '__main__':
    main()
