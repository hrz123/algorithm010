# 31. 下一个排列.py
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        firstIndex = -1
        n = len(nums)

        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                firstIndex = i
                break
        if firstIndex == -1:
            reverse(nums, 0, n - 1)
            return
        secondIndex = -1
        for i in range(n - 1, firstIndex, -1):
            if nums[i] > nums[firstIndex]:
                secondIndex = i
                break
        nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[
            firstIndex]
        reverse(nums, firstIndex + 1, n - 1)


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind1 = -1
        n = len(nums)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind1 = i
                break
        if ind1 == -1:
            reverse(0, n - 1)
            return
        ind2 = -1
        for i in range(n - 1, ind1, -1):
            if nums[i] > nums[ind1]:
                ind2 = i
                break
        nums[ind1], nums[ind2] = nums[ind2], nums[ind1]
        reverse(ind1 + 1, n - 1)


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind1 = -1
        n = len(nums)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind1 = i
                break
        if ind1 == -1:
            reverse(0, n - 1)
            return
        ind2 = -1
        for i in range(n - 1, ind1, -1):
            if nums[i] > nums[ind1]:
                ind2 = i
                break
        nums[ind1], nums[ind2] = nums[ind2], nums[ind1]
        reverse(ind1 + 1, n - 1)


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind1 = -1
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind1 = i
                break

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        if ind1 == -1:
            reverse(0, n - 1)
            return
        ind2 = -1
        for i in range(n - 1, ind1, -1):
            if nums[i] > nums[ind1]:
                ind2 = i
                break
        nums[ind1], nums[ind2] = nums[ind2], nums[ind1]
        reverse(ind1 + 1, n - 1)


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind1 = -1
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind1 = i
                break

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        if ind1 == -1:
            reverse(0, n - 1)
            return
        ind2 = -1
        for i in range(n - 1, ind1, -1):
            if nums[i] > nums[ind1]:
                ind2 = i
                break
        nums[ind1], nums[ind2] = nums[ind2], nums[ind1]
        reverse(ind1 + 1, n - 1)


def main():
    sol = Solution()
    nums = [1, 2, 3]
    sol.nextPermutation(nums)
    print(nums)


if __name__ == '__main__':
    main()
