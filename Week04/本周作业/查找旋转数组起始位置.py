# 查找旋转数组起始位置.py
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid - 1
            else:
                return nums[left]
        # 最终left==r，返回哪个都行
        return nums[left]


# 改进，类似题目leetcode153题
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


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    sol = Solution()
    res = sol.findMin(nums)
    print(res)
    assert res == 0


if __name__ == '__main__':
    main()
