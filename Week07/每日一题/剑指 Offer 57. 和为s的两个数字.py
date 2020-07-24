# 剑指 Offer 57. 和为s的两个数字.py
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            _sum = nums[l] + nums[r]
            if _sum == target:
                return [nums[l], nums[r]]
            if _sum > target:
                r -= 1
            else:
                l += 1
        return []


def main():
    pass


if __name__ == '__main__':
    main()
