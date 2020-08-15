# 35. 搜索插入位置.py
import bisect
from typing import List


# 使用库函数
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


# 手动二分
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        l, r = 0, len(nums)
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        l, r = 0, len(nums)
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return r


# 以下为自我练习
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l


# 1.使用库函数
# 2.遍历
# 3.二分查找
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + ((r - l) >> 1)
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        return l


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


def main():
    sol = Solution()

    nums = [1, 3, 5, 6]
    target = 5
    res = sol.searchInsert(nums, target)
    print(res)

    nums = [1, 3, 5, 6]
    target = 2
    res = sol.searchInsert(nums, target)
    print(res)

    nums = [1, 3, 5, 6]
    target = 7
    res = sol.searchInsert(nums, target)
    print(res)

    nums = [1, 3, 5, 6]
    target = 0
    res = sol.searchInsert(nums, target)
    print(res)


if __name__ == '__main__':
    main()
