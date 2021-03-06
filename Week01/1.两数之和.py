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
#     def twoSum(self, arr: List[int], target: int) -> List[int]:
#         m, row = 0, len(arr) - 1
#         nums_copy = arr[:]
#         arr.sort()
#         res = []
#         while m < row:
#             s = arr[m] + arr[row]
#             if s == target:
#                 res.append([arr[m], arr[row]])
#                 m += 1
#                 while m < row and arr[m] == arr[m - 1]:
#                     m += 1
#             elif s < target:
#                 m += 1
#             else:
#                 row -= 1
#         return [nums_copy.index(start) for start in res[0]] if res else res

# 以下为自我练习
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in memo:
                return [memo[num], i]
            memo[target - num] = i

        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in memo:
                return [memo[num], i]
            else:
                memo[target - num] = i
        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            if nums[i] in mem:
                return [mem[nums[i]], i]
            else:
                mem[target - nums[i]] = i
        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, n in enumerate(nums):
            if n in memo:
                return [memo[n], i]
            else:
                memo[target - n] = i
        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, n in enumerate(nums):
            if n in mem:
                return [mem[n], i]
            mem[target - n] = i
        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, num in enumerate(nums):
            if num in mem:
                return [mem[num], i]
            mem[target - num] = i
        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, num in enumerate(nums):
            if num in mem:
                return [mem[num], i]
            mem[target - num] = i
        return []


def main():
    s = Solution()
    res = s.twoSum([3, 2, 4], 6)
    print(res)


if __name__ == '__main__':
    main()
