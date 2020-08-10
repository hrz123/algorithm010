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
