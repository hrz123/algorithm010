# 面试题40. 最小的k个数.py

import heapq
from typing import List


# 1.sort: O(NlogN)
# 2.heap：O(NlogK)
# 3.quick-sort: O(n)

# sort排序的方法
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]


# 使用heap
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not k:
            return []
        # heapq默认是小顶堆

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans


# 使用快排partition方法
# 时间复杂度：期望为 O(n) ，由于证明过程很繁琐，所以不再这里展开讲。
# 具体证明可以参考《算法导论》第 9 章第 2 小节。
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # partition 方法
        if not k:
            return []
        start = 0
        end = len(arr) - 1
        index = self.quickSort(arr, start, end)
        while index != k - 1:
            # print(index)
            if index > k - 1:
                end = index - 1
                index = self.quickSort(arr, start, end)
            if index < k - 1:
                start = index + 1
                index = self.quickSort(arr, start, end)
        return arr[:k]

    def quickSort(self, arr, start, end):
        low = start
        high = end
        temp = arr[start]
        while low < high:
            while low < high and arr[high] >= temp:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] < temp:
                low += 1
            arr[high] = arr[low]
        arr[low] = temp
        return low


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not k:
            return []
        heap = self.build_heap(arr[:k])

        for i in range(k, len(arr)):
            if arr[i] < heap[0]:
                heap[0] = arr[i]
                self.sink(heap, 0)
        return heap

    # 小的往下下沉
    def sink(self, array, n, k):
        left = 2 * k + 1
        right = 2 * k + 2
        if left >= n:
            return
        max_i = left
        if right < n and array[left] < array[right]:
            max_i = right
        if array[max_i] > array[k]:
            array[max_i], array[k] = array[k], array[max_i]
            self.sink(array, n, max_i)

    def build_heap(self, list_):
        n = len(list_)
        for i in range(n // 2 - 1, -1, -1):
            self.sink(list_, n, i)
        return list_

    def heapSort(self, arr):
        self.build_heap(arr)
        for i in range(len(arr) - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.sink(arr, i, 0)


# 以下为自我练习
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for num in arr:
            if len(heap) == k:
                heapq.heappushpop(heap, -num)
                continue
            heapq.heappush(heap, -num)

        return [-num for num in heap]


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l < r:
            pivot = self.partition(arr, l, r)
            if pivot > k - 1:
                r = pivot - 1
            else:
                l = pivot + 1
        return arr[:k]

    def partition(self, nums, l, r):
        pivot = r
        right = l
        for i in range(l, r):
            if nums[i] < nums[pivot]:
                nums[i], nums[right] = nums[right], nums[i]
                right += 1
        nums[pivot], nums[right] = nums[right], nums[pivot]
        return right


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for num in arr:
            if len(heap) == k:
                heapq.heappushpop(heap, -num)
            else:
                heapq.heappush(heap, -num)
        return [-num for num in heap]


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heap = [-a for a in arr[:k]]
        heapq.heapify(heap)
        for i in range(k, len(arr)):
            heapq.heappushpop(heap, -arr[i])
        return [-a for a in heap]


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return heapq.nsmallest(k, arr)


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for num in arr:
            if len(heap) < k:
                heapq.heappush(heap, -num)
            else:
                heapq.heappushpop(heap, -num)
        return [-num for num in heap]


def main():
    s = Solution()
    arr = [3, 2, 1]
    res = s.getLeastNumbers(arr, 2)
    print(res)

    arr = [0, 1, 2, 1]
    res = s.getLeastNumbers(arr, 2)
    print(res)


if __name__ == '__main__':
    main()
