# 33. 搜索旋转排序数组.py
from typing import List


# 国际站解法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    sol = Solution()
    res = sol.search(nums, target)
    print(res)


if __name__ == '__main__':
    main()
