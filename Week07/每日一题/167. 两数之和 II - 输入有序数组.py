# 167. 两数之和 II - 输入有序数组.py
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 双指针夹逼
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total > target:
                right -= 1
            else:
                left += 1
        return []


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [numbers[l], numbers[r]]
            if total > target:
                r -= 1
            else:
                l += 1
        return []


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            if total > target:
                r -= 1
            else:
                l += 1
        return [-1, -1]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            if total > target:
                r -= 1
            else:
                l += 1


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            if total > target:
                r -= 1
            else:
                l += 1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                return [l + 1, r + 1]
            if total > target:
                r -= 1
            else:
                l += 1


def main():
    sol = Solution()

    nums = [2, 7, 9, 10]
    target = 9
    res = sol.twoSum(nums, target)
    print(res)


if __name__ == '__main__':
    main()
