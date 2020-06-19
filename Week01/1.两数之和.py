# 1.两数之和.py

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []

        memo = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in memo:
                return [memo[num], i]
            memo[target - num] = i

        return []
enu

def main():
    s = Solution()
    res = s.twoSum([2, 11, 15], 9)
    print(res)


if __name__ == '__main__':
    main()
