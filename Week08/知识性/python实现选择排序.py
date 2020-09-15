# python实现选择排序.py
from typing import List


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            t = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = t
        return arr


# 以下为自我练习
class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            t = arr[i]
            arr[i] = arr[_min_index]
            arr[_min_index] = t
        return arr


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            t = arr[i]
            arr[i] = arr[_min_index]
            arr[_min_index] = t
        return arr


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            t = arr[_min_index]
            arr[_min_index] = arr[i]
            arr[i] = t
        return arr


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            t = arr[i]
            arr[i] = arr[_min_index]
            arr[_min_index] = t
        return arr


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            t = arr[i]
            arr[i] = arr[_min_index]
            arr[_min_index] = t
        return arr


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            t = arr[i]
            arr[i] = arr[_min_index]
            arr[_min_index] = t
        return arr


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            t = arr[i]
            arr[i] = arr[_min_index]
            arr[_min_index] = t
        return arr


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            arr[i], arr[_min_index] = arr[_min_index], arr[i]
        return arr


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            arr[_min_index], arr[i] = arr[i], arr[_min_index]
        return arr


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            arr[i], arr[_min_index] = arr[_min_index], arr[i]
        return arr


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            arr[_min_index], arr[i] = arr[i], arr[_min_index]
        return arr


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            arr[_min_index], arr[i] = arr[i], arr[_min_index]
        return arr


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            arr[i], arr[_min_index] = arr[_min_index], arr[i]
        return arr


class Solution:
    def selectionSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[_min_index]:
                    _min_index = j
            arr[i], arr[_min_index] = arr[_min_index], arr[i]
        return arr


class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n - 1):
            _min_index = i
            for j in range(i + 1, n):
                if nums[j] < nums[_min_index]:
                    _min_index = j
            nums[i], nums[_min_index] = nums[_min_index], nums[i]
        return nums


def main():
    sol = Solution()

    nums = [3, 2, 4, 1, 5]
    sol.selectionSort(nums)
    print(nums)

    nums = [3, 2]
    sol.selectionSort(nums)
    print(nums)


if __name__ == '__main__':
    main()
