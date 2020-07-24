# 34. 在排序数组中查找元素的第一个和最后一个位置.py
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [0, 0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if l < len(nums) and nums[l] == target:
            res[0] = l
        else:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l < r:
            print(l, r)
            mid = l + ((r - l) >> 1) + 1
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        res[1] = l
        return res


def main():
    sol = Solution()

    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    res = sol.searchRange(nums, target)
    print(res)


if __name__ == '__main__':
    main()
