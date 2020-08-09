# 154. 寻找旋转排序数组中的最小值 II.py
# 与 剑指 Offer 11. 旋转数组的最小数字 相同
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right = right - 1  # key
        return nums[left]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        return nums[l]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        return nums[l]


def main():
    sol = Solution()

    nums = [1, 3, 5]
    res = sol.findMin(nums)
    print(res)
    assert res == 1

    nums = [2, 2, 2, 0, 1]
    res = sol.findMin(nums)
    print(res)
    assert res == 0

    nums = [2, 2, 2, 2, 1]
    res = sol.findMin(nums)
    print(res)
    assert res == 1

    nums = [0]
    res = sol.findMin(nums)
    print(res)
    assert res == 0


if __name__ == '__main__':
    main()
