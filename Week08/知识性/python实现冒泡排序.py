# python实现冒泡排序.py
from typing import List


class Solution:
    def bubbleSort(self, nums: List[int]):
        n = len(nums)
        for i in range(n - 1, 0, -1):
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


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
