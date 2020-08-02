# 632. 最小区间.py
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        counter = [set() for _ in range(10 ** 5 << 1 | 1)]
        all_num = sorted(list(set(a for num in nums for a in num)))
        for i in range(len(nums)):
            for n in nums[i]:
                counter[n + 10 ** 5].add(i)
        l, r = 0, 0
        _min = len(counter)
        res = [0, 0]
        size = len(nums)
        target = 0
        lookup = defaultdict(int)
        while r < len(all_num):
            r_idx = all_num[r] + 10 ** 5
            for idx in counter[r_idx]:
                lookup[idx] += 1
                if lookup[idx] == 1:
                    target += 1
            while target == size:
                l_idx = all_num[l] + 10 ** 5
                if r_idx - l_idx < _min:
                    _min = r_idx - l_idx
                    res[:] = [l_idx, r_idx]
                for idx in counter[l_idx]:
                    lookup[idx] -= 1
                    if lookup[idx] == 0:
                        target -= 1
                l += 1
            r += 1
        return [res[0] - 10 ** 5, res[1] - 10 ** 5]


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        indices = defaultdict(list)
        xMin, xMax = 10 ** 9, -10 ** 9
        for i, vec in enumerate(nums):
            for x in vec:
                indices[x].append(i)
            xMin = min(xMin, *vec)
            xMax = max(xMax, *vec)

        freq = [0] * n
        inside = 0
        left, right = xMin, xMin - 1
        bestLeft, bestRight = xMin, xMax

        while right < xMax:
            right += 1
            if right in indices:
                for x in indices[right]:
                    freq[x] += 1
                    if freq[x] == 1:
                        inside += 1
                while inside == n:
                    if right - left < bestRight - bestLeft:
                        bestLeft, bestRight = left, right
                    if left in indices:
                        for x in indices[left]:
                            freq[x] -= 1
                            if freq[x] == 0:
                                inside -= 1
                    left += 1

        return [bestLeft, bestRight]


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        rangeLeft, rangeRight = -10 ** 9, 10 ** 9
        maxValue = max(vec[0] for vec in nums)
        priorityQueue = [(vec[0], i, 0) for i, vec in enumerate(nums)]
        heapq.heapify(priorityQueue)

        while True:
            minValue, row, idx = heapq.heappop(priorityQueue)
            if maxValue - minValue < rangeRight - rangeLeft:
                rangeLeft, rangeRight = minValue, maxValue
            if idx == len(nums[row]) - 1:
                break
            maxValue = max(maxValue, nums[row][idx + 1])
            heapq.heappush(priorityQueue, (nums[row][idx + 1], row, idx + 1))

        return [rangeLeft, rangeRight]


def main():
    sol = Solution()

    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    res = sol.smallestRange(nums)
    print(res)

    nums = [[-5, -4, -3, -2, -1], [1, 2, 3, 4, 5]]
    res = sol.smallestRange(nums)
    print(res)


if __name__ == '__main__':
    main()
