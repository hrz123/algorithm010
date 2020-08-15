# python实现堆排序（堆不需要实现）.py
import heapq
from typing import List


class Solution:
    def heapSort(self, nums: List[int]):
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
        for i in range(len(nums)):
            nums[i] = heapq.heappop(heap)


class Solution:
    def heapSort(self, nums: List[int]):
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
        for i in range(len(nums)):
            nums[i] = heapq.heappop(heap)


class Solution:
    def heapSort(self, nums: List[int]):
        heap = nums[:]
        heapq.heapify(heap)
        for i in range(len(nums)):
            nums[i] = heapq.heappop(heap)


def max_heap(a, i, size):
    l = i * 2 + 1
    r = i * 2 + 2
    large = i
    if l < size and a[l] > a[large]:
        large = l
    if r < size and a[r] > a[large]:
        large = r
    if large != i:
        a[i], a[large] = a[large], a[i]
        max_heap(a, large, size)


def build_heap(a, size):
    for i in range(size << 1, -1, -1):
        max_heap(a, i, size)


def main():
    sol = Solution()

    nums = [3, 2, 4, 1, 5]
    sol.heapSort(nums)
    print(nums)

    nums = [3, 2]
    sol.heapSort(nums)
    print(nums)


if __name__ == '__main__':
    main()
