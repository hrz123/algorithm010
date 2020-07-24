# 540. 有序数组中的单一元素.py
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if mid & 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]


def main():
    sol = Solution()

    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    res = sol.singleNonDuplicate(nums)
    print(res)

    nums = [3, 3, 7, 7, 10, 11, 11]
    res = sol.singleNonDuplicate(nums)
    print(res)


if __name__ == '__main__':
    main()
