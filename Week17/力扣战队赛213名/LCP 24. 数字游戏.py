# 5504. 使数组和能被 P 整除.py
import heapq
from typing import List


class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        nums = [nums[i] - i for i in range(len(nums))]
        left_heap = []  # 左侧为大根堆
        right_heap = []  # 右侧为小根堆
        median = nums[0]
        sl = 0
        sr = 0
        ret = [0] * len(nums)
        for i in range(1, len(nums)):
            if i % 2 == 0:
                # 左右堆大小相等，现要再加入一元素
                left_root = -left_heap[0]
                right_root = right_heap[0]
                if nums[i] < left_root:
                    median = left_root
                    heapq.heapreplace(left_heap,
                                      -nums[i])  # 由于heaqp是小根堆，存相反数来实现大根堆
                    sl = sl - left_root + nums[i]
                elif nums[i] > right_root:
                    median = right_root
                    heapq.heapreplace(right_heap, nums[i])
                    sr = sr - right_root + nums[i]
                else:
                    median = nums[i]

            else:
                if nums[i] > median:
                    heapq.heappush(right_heap, nums[i])
                    heapq.heappush(left_heap, -median)
                    sl += median
                    sr += nums[i]
                else:
                    heapq.heappush(left_heap, -nums[i])
                    heapq.heappush(right_heap, median)
                    sl += nums[i]
                    sr += median
            ret[i] = (sr - sl) % 1000000007
        return ret


def main():
    sol = Solution()
    nums = [1, 1, 1, 2, 3, 4]
    res = sol.numsGame(nums)
    print(res)

    nums = [*range(1, 100001)]
    res = sol.numsGame(nums)
    print(res)
    print(all(i == 0 for i in res))
    print(res.count(0))


if __name__ == '__main__':
    main()
