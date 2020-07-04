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
        # 最终left==right，返回哪个都行
        return nums[left]


def main():
    nums = [3, 4, 5, 1, 2]
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [3, 1, 2]
    sol = Solution()
    res = sol.findMin(nums)
    print(res)


if __name__ == '__main__':
    main()
