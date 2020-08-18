# 283.移动零.py

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = j = 0
        length = len(nums)

        while j < length:
            while j < length - 1 and nums[j] == 0:
                j += 1
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1


# 以下为自我练习
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if not nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


# 超哥直播题目，往两边挪
# 荷兰国旗算法
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right, i = 0, len(nums) - 1, 0
        flag = True
        while i <= right:
            if not nums[i]:
                if flag:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
                    i += 1
                else:
                    nums[right], nums[i] = nums[i], nums[right]
                    right -= 1
                flag = not flag
            else:
                i += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        r = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[r] = nums[r], nums[i]
                r += 1


def main():
    s = Solution()

    nums = [0, 1, 0, 5, 6, 7, 3, 0]
    s.moveZeroes(nums)
    print(nums)

    nums = [1]
    s.moveZeroes(nums)
    print(nums)


if __name__ == '__main__':
    main()
