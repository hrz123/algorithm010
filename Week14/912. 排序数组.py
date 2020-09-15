# 912. 排序数组.py
import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, l, r):
        if l >= r:
            return
        pivot = self.partition(nums, l, r)
        self.quickSort(nums, l, pivot - 1)
        self.quickSort(nums, pivot + 1, r)

    def partition(self, nums, l, r):
        ran = random.randint(l, r)
        nums[ran], nums[r] = nums[r], nums[ran]
        pivot = r
        right = l
        for i in range(l, r):
            if nums[i] < nums[pivot]:
                nums[i], nums[right] = nums[right], nums[i]
                right += 1
        nums[pivot], nums[right] = nums[right], nums[pivot]
        return right


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, l, r):
        if l >= r:
            return
        pivot = self.partition(nums, l, r)
        self.quickSort(nums, l, pivot - 1)
        self.quickSort(nums, pivot + 1, r)

    def partition(self, nums, l, r):
        ran = random.randint(l, r)
        nums[r], nums[ran] = nums[ran], nums[r]
        pivot = r
        right = l
        for i in range(l, r):
            if nums[i] < nums[pivot]:
                nums[i], nums[right] = nums[right], nums[i]
                right += 1
        nums[right], nums[pivot] = nums[pivot], nums[right]
        return right


def main():
    sol = Solution()
    nums = [5, 2, 3, 1]
    res = sol.sortArray(nums)
    print(res)


if __name__ == '__main__':
    main()
