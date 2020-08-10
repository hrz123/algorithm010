# python实现归并排序.py
from typing import List


class Solution:
    def mergeSort(self, nums: List[int]):
        self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums: List[int], l: int, r: int):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        self.merge(nums, l, mid, r)

    def merge(self, nums, l, mid, r):
        res = [0] * (r - l + 1)
        i, j, k = l, mid + 1, 0
        while i <= mid and j <= r:
            if nums[i] < nums[j]:
                res[k] = nums[i]
                i += 1
            else:
                res[k] = nums[j]
                j += 1
            k += 1
        if i <= mid:
            res[k:] = nums[i:mid + 1]
        else:
            res[k:] = nums[j:r + 1]
        nums[l:r + 1] = res

    def merge1(self, nums, l, mid, r):
        res = nums[l:r + 1]
        i, j, k = l, mid + 1, 0
        while i <= mid and j <= r:
            if nums[i] < nums[j]:
                res[k] = nums[i]
                i += 1
            else:
                res[k] = nums[j]
                j += 1
            k += 1
        if i <= mid:
            res[k:] = nums[i:mid + 1]
        nums[l:r + 1] = res


# 以下为自我练习
class Solution:
    def mergeSort(self, nums: List[int]):
        self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums: List[int], l: int, r: int):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        self.merge(nums, l, mid, r)

    def merge(self, nums, l, mid, r):
        res = [0] * (r - l + 1)
        i, j, k = l, mid + 1, 0
        while i <= mid and j <= r:
            if nums[i] < nums[j]:
                res[k] = nums[i]
                i += 1
            else:
                res[k] = nums[j]
                j += 1
            k += 1
        if i <= mid:
            res[k:] = nums[i:mid + 1]
        else:
            res[k:] = nums[j:r + 1]
        nums[l:r + 1] = res


class Solution:
    def mergeSort(self, nums: List[int]):
        self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums, l, r):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        self.merge(nums, l, mid, r)

    def merge(self, nums, l, mid, r):
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] < nums[j]:
                cache[c] = nums[i]
                i += 1
                c += 1
            cache[c] = nums[j]
            c += 1
        while i <= mid:
            cache[c] = nums[i]
            i += 1
            c += 1
        nums[l:r + 1] = cache


class Solution:
    def mergeSort(self, nums: List[int]):
        self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums, l, r):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache


class Solution:
    def mergeSort(self, nums: List[int]):
        self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums, l, r):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache


class Solution:
    def mergeSort(self, nums: List[int]):
        self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums, l, r):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache


class Solution:
    def mergeSort(self, nums: List[int]):
        self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums, l, r):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache


class Solution:
    def mergeSort(self, nums: List[int]):
        self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums: List[int], l: int, r: int):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache


class Solution:
    def mergeSort(self, nums: List[int]):
        self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums: List[int], l: int, r: int):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache


class Solution:
    def mergeSort(self, nums: List[int]):
        self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums: List[int], l: int, r: int):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache


class Solution:
    def mergeSort(self, nums: List[int]):
        self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums, l, r):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache


class Solution:
    def mergeSort(self, nums: List[int]):
        self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums, l, r):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache


class Solution:
    def mergeSort(self, nums: List[int]):
        self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums: List[int], l: int, r: int):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache


class Solution:
    def mergeSort(self, nums: List[int]):
        return self.mergeSortHelper(nums, 0, len(nums) - 1)

    def mergeSortHelper(self, nums, l, r):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        self.mergeSortHelper(nums, l, mid)
        self.mergeSortHelper(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache


def main():
    sol = Solution()

    nums = [3, 2, 4, 1, 5]
    sol.mergeSort(nums)
    print(nums)

    nums = [3, 2]
    sol.mergeSort(nums)
    print(nums)

    nums = [5]
    sol.mergeSort(nums)
    print(nums)

    nums = []
    sol.mergeSort(nums)
    print(nums)


if __name__ == '__main__':
    main()
