# 215. 数组中的第K个最大元素.py

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            num = nums[i]
            if num >= heap[0]:
                heapq.heappushpop(heap, num)
        return heap[0]


def main():
    sol = Solution()
    res = sol.findKthLargest(
        [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4,
         7, 8, 5, 6]
        , 20)
    print(res)


if __name__ == '__main__':
    main()
