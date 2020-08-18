# 153. 寻找旋转排序数组中的最小值.py

from typing import List


# 第一遍解法
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                return nums[left]


# 答案解法
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        # 最终left==r，返回哪个都行
        return nums[left]


# 以下为自我练习
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            # 比右边大就一定不是最小的
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


def main():
    sol = Solution()

    nums = [3, 4, 5, 1, 2]
    res = sol.findMin(nums)
    print(res)

    nums = [4, 5, 6, 7, 0, 1, 2]
    res = sol.findMin(nums)
    print(res)

    nums = [3, 1, 2]
    res = sol.findMin(nums)
    print(res)


if __name__ == '__main__':
    main()
