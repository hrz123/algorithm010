# python实现插入排序.py

from typing import List


class Solution:
    def insertionSort(self, nums: List[int]):
        n = len(nums)
        for i in range(1, n):
            for j in range(i):
                if nums[i] < nums[j]:
                    tmp = nums[i]
                    nums[j + 1:i + 1] = nums[j:i]
                    nums[j] = tmp


def main():
    sol = Solution()

    nums = [3, 2, 4, 1, 5]
    sol.insertionSort(nums)
    print(nums)

    nums = [3, 2]
    sol.insertionSort(nums)
    print(nums)


if __name__ == '__main__':
    main()
