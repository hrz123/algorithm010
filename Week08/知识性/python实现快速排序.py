# python实现快速排序.py
from typing import List


class Solution:
    def quickSort(self, nums: List[int]):
        return self.quickSortHelper(nums, 0, len(nums) - 1)

    def quickSortHelper(self, nums: List[int], l: int, r: int):
        if l >= r:
            return
        pivot = self.partition(nums, l, r)
        self.quickSortHelper(nums, l, pivot - 1)
        self.quickSortHelper(nums, pivot + 1, r)

    def partition(self, nums, l, r):
        # pivot 标杆位置， right：小于pivot的元素的最右边界
        pivot = r
        right = l
        for i in range(l, r):
            if nums[i] < nums[pivot]:
                nums[right], nums[i] = nums[i], nums[right]
                right += 1
        nums[right], nums[pivot] = nums[pivot], nums[right]
        return right

    # def partition(self, nums, l, r):
    #     pivot = l
    #     p_larger = r
    #     i = l + 1
    #     while i <= p_larger:
    #         if nums[i] >= nums[pivot]:
    #             nums[i], nums[p_larger] = nums[p_larger], nums[i]
    #             p_larger -= 1
    #         else:
    #             i += 1
    #     nums[pivot], nums[p_larger] = nums[p_larger], nums[pivot]
    #     return p_larger


# 以下为自我练习
class Solution:
    def quickSort(self, nums: List[int]):
        return self.quickSortHelper(nums, 0, len(nums) - 1)

    def quickSortHelper(self, nums: List[int], l: int, r: int):
        if l >= r:
            return
        pivot = self.partition(nums, l, r)
        self.quickSortHelper(nums, l, pivot - 1)
        self.quickSortHelper(nums, pivot + 1, r)

    def partition(self, nums, l, r):
        pivot = r
        right = l
        for i in range(l, r):
            if nums[i] < nums[pivot]:
                nums[i], nums[right] = nums[right], nums[i]
                right += 1
        nums[right], nums[pivot] = nums[pivot], nums[right]
        return right

    # def partition1(self, nums, l, r):
    #     pivot = l
    #     left = r
    #     i = l + 1
    #     while i <= left:
    #         if nums[i] > nums[pivot]:
    #             nums[i], nums[left] = nums[left], nums[i]
    #             left -= 1
    #         else:
    #             i += 1
    #     nums[left], nums[pivot] = nums[pivot], nums[left]
    #     return left


class Solution:
    def quickSort(self, nums: List[int]):
        self.quickSortHelper(nums, 0, len(nums) - 1)

    def quickSortHelper(self, nums, l, r):
        if l >= r:
            return
        pivot = self.partition(nums, l, r)
        self.quickSortHelper(nums, l, pivot - 1)
        self.quickSortHelper(nums, pivot + 1, r)

    def partition1(self, nums, l, r):
        pivot = r
        right = l
        for i in range(l, r):
            if nums[i] < nums[pivot]:
                nums[i], nums[right] = nums[right], nums[i]
                right += 1
        nums[right], nums[pivot] = nums[pivot], nums[right]
        return right

    def partition(self, nums, l, r):
        pivot = l
        left = r
        cur = l + 1
        while cur <= left:
            if nums[cur] > nums[pivot]:
                nums[left], nums[cur] = nums[cur], nums[left]
                left -= 1
            else:
                cur += 1
        nums[left], nums[pivot] = nums[pivot], nums[left]
        return left


class Solution:
    def quickSort(self, nums: List[int]):
        self.quickSortHelper(nums, 0, len(nums) - 1)

    def quickSortHelper(self, nums, l, r):
        if l >= r:
            return
        pivot = self.partition(nums, l, r)
        self.quickSortHelper(nums, l, pivot - 1)
        self.quickSortHelper(nums, pivot + 1, r)

    def partition1(self, nums, l, r):
        pivot = r
        right = l
        for i in range(l, r):
            if nums[i] < nums[pivot]:
                nums[i], nums[right] = nums[right], nums[i]
                right += 1
        nums[right], nums[pivot] = nums[pivot], nums[right]
        return right

    def partition(self, nums, l, r):
        pivot = l
        left = r
        cur = l + 1
        while cur <= left:
            if nums[cur] > nums[pivot]:
                nums[cur], nums[left] = nums[left], nums[cur]
                left -= 1
            else:
                cur += 1
        nums[left], nums[pivot] = nums[pivot], nums[left]
        return left


def main():
    sol = Solution()
    nums = [3, 2, 4, 1, 5]
    sol.quickSort(nums)
    print(nums)

    nums = [3, 2]
    sol.quickSort(nums)
    print(nums)

    nums = [1, 4, 6, 8, 2]
    sol.quickSort(nums)
    print(nums)

    nums = [5, 4, 3, 2, 1]
    sol.quickSort(nums)
    print(nums)


if __name__ == '__main__':
    main()
