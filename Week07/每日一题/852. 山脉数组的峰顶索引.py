# 852. 山脉数组的峰顶索引.py
from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if A[mid] > A[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


def main():
    sol = Solution()

    nums = [0, 1, 0]
    res = sol.peakIndexInMountainArray(nums)
    print(res)

    nums = [0, 2, 1, 0]
    res = sol.peakIndexInMountainArray(nums)
    print(res)


if __name__ == '__main__':
    main()
