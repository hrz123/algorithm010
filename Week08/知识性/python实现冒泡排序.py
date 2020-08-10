# python实现冒泡排序.py
from typing import List


class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    t = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = t
        return arr


# 以下为自我练习
class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    t = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = t
        return arr


class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    t = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = t
        return arr


class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    t = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = t
        return arr


class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    t = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = t
        return arr


class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j - 1]:
                    t = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = t
        return arr


class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    t = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = t
        return arr


class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    t = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = t
        return arr


class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    t = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = t
        return arr


class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class Solution:
    def bubbleSort(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


def main():
    sol = Solution()

    nums = [3, 2, 4, 1, 5]
    sol.bubbleSort(nums)
    print(nums)

    nums = [3, 2]
    sol.bubbleSort(nums)
    print(nums)

    nums = [5, 4, 3, 2, 1]
    sol.bubbleSort(nums)
    print(nums)


if __name__ == '__main__':
    main()
