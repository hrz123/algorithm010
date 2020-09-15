# 215. 数组中的第K个最大元素.py

import heapq
import random
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


# 第一个解法，sort，从大到小排序，取索引为k-1的，O(nlogn)
# 解法二，小顶堆容量为k，大于堆顶的放入，O（nlogn)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) == k:
                heapq.heappushpop(heap, num)
            else:
                heapq.heappush(heap, num)
        return heap[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            else:
                heapq.heappushpop(heap, n)
        return heap[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapsize = len(nums)

        def maxheap(a, i, length):
            l = 2 * i + 1
            r = 2 * i + 2
            large = i
            if l < length and a[l] > a[large]:
                large = l
            if r < length and a[r] > a[large]:
                large = r
            if large != i:
                a[large], a[i] = a[i], a[large]
                maxheap(a, large, length)

        def buildheap(a, length):
            for i in range(heapsize >> 1, -1, -1):
                maxheap(a, i, length)

        buildheap(nums, heapsize)
        for i in range(heapsize - 1, heapsize - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapsize -= 1
            maxheap(nums, 0, heapsize)

        return nums[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, l, r):
            pivot = r
            right = l
            for i in range(l, r):
                if nums[i] >= nums[pivot]:
                    nums[i], nums[right] = nums[right], nums[i]
                    right += 1
            nums[right], nums[pivot] = nums[pivot], nums[right]
            return right

        l, r = 0, len(nums) - 1
        while True:
            pivot = partition(nums, l, r)
            if pivot == k - 1:
                return nums[pivot]
            if pivot < k - 1:
                l = pivot + 1
            else:
                r = pivot - 1


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def maxheap(a, i, length):
            l = 2 * i + 1
            r = 2 * i + 2
            large = i
            if l < length and a[l] > a[large]:
                large = l
            if r < length and a[r] > a[large]:
                large = r
            if large != i:
                a[i], a[large] = a[large], a[i]
                maxheap(a, large, length)

        def buildheap(a, length):
            for i in range(length >> 1, -1, -1):
                maxheap(a, i, length)

        heapsize = len(nums)
        buildheap(nums, heapsize)
        for i in range(heapsize - 1, heapsize - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapsize -= 1
            maxheap(nums, 0, heapsize)
        return nums[0]


# 以下为自我练习
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # def partition(nums, m, r):
        #     pivot = r
        #     r = m
        #     for i in range(m, r):
        #         if nums[i] <= nums[pivot]:
        #             nums[i], nums[r] = nums[r], nums[i]
        #             r += 1
        #     nums[r], nums[pivot] = nums[pivot], nums[r]
        #     return r

        def partition(nums, l, r):
            pivot = l
            left = r
            for i in range(r, l, -1):
                if nums[i] <= nums[pivot]:
                    nums[i], nums[left] = nums[left], nums[i]
                    left -= 1
            nums[left], nums[pivot] = nums[pivot], nums[left]
            return left

        l, r = 0, len(nums) - 1
        while True:
            pivot = partition(nums, l, r)
            if pivot == k - 1:
                return nums[pivot]
            if pivot < k - 1:
                l = pivot + 1
            else:
                r = pivot - 1


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def maxheap(a, i, size):
            l = i * 2 + 1
            r = i * 2 + 2
            large = i
            if l < size and a[l] > a[large]:
                large = l
            if r < size and a[r] > a[large]:
                large = r
            if large != i:
                a[i], a[large] = a[large], a[i]
                maxheap(a, large, size)

        def buildheap(a, size):
            for i in range(size >> 1, -1, -1):
                maxheap(a, i, size)

        heapsize = len(nums)
        buildheap(nums, heapsize)
        for i in range(heapsize - 1, heapsize - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapsize -= 1
            maxheap(nums, 0, heapsize)
        return nums[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, l, r):
            pivot = r
            rand = random.randint(l, r)
            nums[pivot], nums[rand] = nums[rand], nums[pivot]
            right = l
            for i in range(l, r):
                if nums[i] <= nums[pivot]:
                    nums[i], nums[right] = nums[right], nums[i]
                    right += 1
            nums[right], nums[pivot] = nums[pivot], nums[right]
            return right

        l, r = 0, len(nums) - 1
        while True:
            pivot = partition(nums, l, r)
            if pivot == len(nums) - k:
                return nums[pivot]
            if pivot < len(nums) - k:
                l = pivot + 1
            else:
                r = pivot - 1


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def maxheap(a, i, size):
            l = i * 2 + 1
            r = i * 2 + 2
            large = i
            if l < size and a[l] > a[large]:
                large = l
            if r < size and a[r] > a[large]:
                large = r
            if large != i:
                a[i], a[large] = a[large], a[i]
                maxheap(a, large, size)

        def buildheap(a, size):
            for i in range(size >> 1, -1, -1):
                maxheap(a, i, size)

        heapsize = len(nums)
        buildheap(nums, heapsize)
        for i in range(heapsize - 1, heapsize - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapsize -= 1
            maxheap(nums, 0, heapsize)
        return nums[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def maxheap(a, i, size):
            l = i * 2 + 1
            r = i * 2 + 2
            large = i
            if l < size and a[l] > a[large]:
                large = l
            if r < size and a[r] > a[large]:
                large = r
            if large != i:
                nums[i], nums[large] = nums[large], nums[i]
                maxheap(a, large, size)

        def buildheap(a, size):
            for i in range(size >> 1, -1, -1):
                maxheap(a, i, size)

        heapsize = len(nums)
        buildheap(nums, heapsize)
        for i in range(heapsize - 1, heapsize - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapsize -= 1
            maxheap(nums, 0, heapsize)
        return nums[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, l, r):
            ran = random.randint(l, r)
            nums[r], nums[ran] = nums[ran], nums[r]
            pivot = r
            right = l
            for i in range(l, r):
                if nums[i] <= nums[pivot]:
                    nums[i], nums[right] = nums[right], nums[i]
                    right += 1
            nums[right], nums[pivot] = nums[pivot], nums[right]
            return right

        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            pivot = partition(nums, l, r)
            if pivot == n - k:
                return nums[pivot]
            if pivot < n - k:
                l = pivot + 1
            else:
                r = pivot - 1


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def maxheap(a, i, size):
            l = i * 2 + 1
            r = i * 2 + 2
            large = i
            if l < size and a[l] > a[large]:
                large = l
            if r < size and a[r] > a[large]:
                large = r
            if large != i:
                a[i], a[large] = a[large], a[i]
                maxheap(a, large, size)

        def buildheap(a, size):
            for i in range(size >> 1, -1, -1):
                maxheap(a, i, size)

        heap_size = len(nums)
        buildheap(nums, heap_size)
        for i in range(heap_size - 1, heap_size - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heap_size -= 1
            maxheap(nums, 0, heap_size)
        return nums[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            pivot = self.partition(nums, l, r)
            if pivot == n - k:
                return nums[pivot]
            if pivot < n - k:
                l = pivot + 1
            else:
                r = pivot - 1

    def partition(self, nums, l, r):
        ran = random.randint(l, r)
        nums[r], nums[ran] = nums[ran], nums[r]
        pivot = r
        right = l
        for i in range(l, r):
            if nums[i] <= nums[pivot]:
                nums[i], nums[right] = nums[right], nums[i]
                right += 1
        nums[right], nums[pivot] = nums[pivot], nums[right]
        return right


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
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
            for i in range(size >> 1, -1, -1):
                max_heap(a, i, size)

        heap_size = len(nums)
        build_heap(nums, heap_size)
        for i in range(heap_size - 1, heap_size - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heap_size -= 1
            max_heap(nums, 0, heap_size)
        return nums[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            pivot = self.partition(nums, l, r)
            if pivot == n - k:
                return nums[pivot]
            if pivot > n - k:
                r = pivot - 1
            else:
                l = pivot + 1

    def partition(self, nums, l, r):
        ran = random.randint(l, r)
        nums[ran], nums[r] = nums[r], nums[ran]
        pivot = r
        right = l
        for i in range(l, r):
            if nums[i] <= nums[pivot]:
                nums[i], nums[right] = nums[right], nums[i]
                right += 1
        nums[right], nums[pivot] = nums[pivot], nums[right]
        return right


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            pivot = self.partition(nums, l, r)
            if pivot == n - k:
                return nums[pivot]
            if pivot > n - k:
                r = pivot - 1
            else:
                l = pivot + 1

    def partition(self, nums, l, r):
        ran = random.randint(l, r)
        nums[r], nums[ran] = nums[ran], nums[r]
        pivot = r
        right = l
        for i in range(l, r):
            if nums[i] <= nums[pivot]:
                nums[i], nums[right] = nums[right], nums[i]
                right += 1
        nums[right], nums[pivot] = nums[pivot], nums[right]
        return right


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            pivot = self.partition(nums, l, r)
            if pivot == n - k:
                return nums[pivot]
            if pivot < n - k:
                l = pivot + 1
            else:
                r = pivot - 1

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
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2,
            4, 7, 8, 5, 6]
    k = 20
    res = sol.findKthLargest(nums, k)
    print(res)

    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    res = sol.findKthLargest(nums, k)
    print(res)


def partition(nums, l, r):
    rand = random.randint(l, r)
    nums[r], nums[rand] = nums[rand], nums[r]
    pivot = r
    right = l
    for i in range(l, r):
        if nums[i] <= nums[pivot]:
            nums[i], nums[right] = nums[right], nums[i]
            right += 1
    nums[right], nums[pivot] = nums[pivot], nums[right]
    return right


def partition(nums, l, r):
    # randint 是包括左右区间的
    random_index = random.randint(l, r)
    nums[random_index], nums[l] = nums[l], nums[random_index]

    pivot = nums[l]

    lt = l + 1
    rt = r

    while True:
        while lt <= rt and nums[lt] < pivot:
            lt += 1
        while lt <= rt and nums[rt] > pivot:
            rt -= 1

        if lt > rt:
            break
        nums[lt], nums[rt] = nums[rt], nums[lt]
        lt += 1
        rt -= 1

    nums[l], nums[rt] = nums[rt], nums[l]
    return rt


if __name__ == '__main__':
    main()
