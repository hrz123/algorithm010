# python实现选择排序.py
from typing import List


class Solution:
    def selectionSort(self, nums: List[int]):
        n = len(nums)
        for i in range(n - 1):
            smallest = i
            for j in range(i + 1, n):
                if nums[j] < nums[smallest]:
                    smallest = j
            nums[i], nums[smallest] = nums[smallest], nums[i]


def main():
    sol = Solution()

    nums = [3, 2, 4, 1, 5]
    sol.selectionSort(nums)
    print(nums)

    nums = [3, 2]
    sol.selectionSort(nums)
    print(nums)


if __name__ == '__main__':
    main()
