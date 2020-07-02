# 查找旋转数组起始位置.py
from typing import List


class Solution:
    def findArrayHead(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid - 1
            else:
                return left
        # 最终left==right，返回哪个都行
        return left


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    sol = Solution()
    res = sol.findArrayHead(nums)
    print(res)
    assert res == 4


if __name__ == '__main__':
    main()
