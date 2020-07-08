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


# 两数之和双指针解法
# 错误的解法
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         l, r = 0, len(nums) - 1
#         nums_copy = nums[:]
#         nums.sort()
#         res = []
#         while l < r:
#             s = nums[l] + nums[r]
#             if s == target:
#                 res.append([nums[l], nums[r]])
#                 l += 1
#                 while l < r and nums[l] == nums[l - 1]:
#                     l += 1
#             elif s < target:
#                 l += 1
#             else:
#                 r -= 1
#         return [nums_copy.index(i) for i in res[0]] if res else res


def main():
    s = Solution()
    res = s.twoSum([3, 2, 4], 6)
    print(res)


if __name__ == '__main__':
    main()
