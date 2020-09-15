# 面试题 08.03. 魔术索引.py
from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == i:
                return i
        return -1


# 官方解法
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        def binary_search(nums, l, r):
            if l > r:
                return -1
            mid = l + ((r - l) >> 1)
            left = binary_search(nums, l, mid - 1)
            if left != -1:
                return left
            if nums[mid] == mid:
                return mid
            return binary_search(nums, mid + 1, r)

        return binary_search(nums, 0, len(nums) - 1)


# 以下为自我练习
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        def binary_search(nums, l, r):
            if l > r:
                return -1
            mid = l + ((r - l) >> 1)
            left = binary_search(nums, l, mid - 1)
            if left != -1:
                return left
            if nums[mid] == mid:
                return mid
            return binary_search(nums, mid + 1, r)

        return binary_search(nums, 0, len(nums) - 1)


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        def binary_search(nums, l, r):
            if l > r:
                return -1
            mid = l + ((r - l) >> 1)
            left = binary_search(nums, l, mid - 1)
            if left != -1:
                return left
            if nums[mid] == mid:
                return mid
            return binary_search(nums, mid + 1, r)

        return binary_search(nums, 0, len(nums) - 1)


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        def binary_search(nums, l, r):
            if l > r:
                return -1
            mid = l + ((r - l) >> 1)
            left = binary_search(nums, l, mid - 1)
            if left != -1:
                return left
            if nums[mid] == mid:
                return mid
            return binary_search(nums, mid + 1, r)

        return binary_search(nums, 0, len(nums) - 1)


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == i:
                return i
        return -1


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        def binary_search(nums, l, r):
            if l > r:
                return -1
            mid = l + ((r - l) >> 1)
            left = binary_search(nums, l, mid - 1)
            if left != -1:
                return left
            if nums[mid] == mid:
                return mid
            return binary_search(nums, mid + 1, r)

        return binary_search(nums, 0, len(nums) - 1)


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        def binary_search(nums, l, r):
            if l > r:
                return -1
            mid = l + ((r - l) >> 1)
            left = binary_search(nums, l, mid - 1)
            if left != -1:
                return left
            if nums[mid] == mid:
                return mid
            return binary_search(nums, mid + 1, r)

        return binary_search(nums, 0, len(nums) - 1)


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        def binary_search(nums, l, r):
            if l > r:
                return -1
            mid = l + ((r - l) >> 1)
            left = binary_search(nums, l, mid - 1)
            if left != -1:
                return left
            if nums[mid] == mid:
                return mid
            return binary_search(nums, mid + 1, r)

        return binary_search(nums, 0, len(nums) - 1)


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i == nums[i]:
                return i
            if i < nums[i]:
                i = nums[i]
            else:
                i += 1
        return -1


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num == i:
                return i
        return -1


def main():
    sol = Solution()

    nums = [0, 2, 3, 4, 5]
    res = sol.findMagicIndex(nums)
    print(res)

    nums = [1, 1, 1]
    res = sol.findMagicIndex(nums)
    print(res)


if __name__ == '__main__':
    main()
