# 679. 24 点游戏.py
from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums: return False

        def helper(nums):
            if len(nums) == 1: return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        newnums = [nums[k] for k in range(len(nums)) if
                                   i != k != j]
                        if helper(newnums + [nums[i] + nums[j]]): return True
                        if helper(newnums + [nums[i] - nums[j]]): return True
                        if helper(newnums + [nums[i] * nums[j]]): return True
                        if nums[j] != 0 and helper(
                                newnums + [nums[i] / nums[j]]): return True
            return False

        return helper(nums)


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False

        def helper(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        rest = [nums[k] for k in range(len(nums)) if
                                i != k != j]
                        if helper(rest + [nums[i] + nums[j]]):
                            return True
                        if helper(rest + [nums[i] - nums[j]]):
                            return True
                        if helper(rest + [nums[i] * nums[j]]):
                            return True
                        if nums[j] != 0 and helper(rest + [nums[i] / nums[j]]):
                            return True
            return False

        return helper(nums)


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False

        def helper(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        rest = [nums[k] for k in range(len(nums)) if i != k
                                != j]
                        if helper(rest + [nums[i] + nums[j]]):
                            return True
                        if helper(rest + [nums[i] - nums[j]]):
                            return True
                        if helper(rest + [nums[i] * nums[j]]):
                            return True
                        if nums[j] != 0 and helper(rest + [nums[i] / nums[j]]):
                            return True
            return False

        return helper(nums)


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False

        def helper(nums):
            if len(nums) == 1:
                if abs(nums[0] - 24) < 1e-6:
                    return True
                return False
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        rest = [nums[k] for k in range(len(nums)) if i != k
                                != j]
                        if helper(rest + [nums[i] + nums[j]]) \
                                or helper(rest + [nums[i] - nums[j]]) \
                                or helper(rest + [nums[i] * nums[j]]) \
                                or (nums[j] != 0
                                    and helper(rest + [nums[i] / nums[j]])):
                            return True
            return False

        return helper(nums)


def main():
    sol = Solution()
    nums = [4, 1, 8, 7]
    res = sol.judgePoint24(nums)
    print(res)


if __name__ == '__main__':
    main()
