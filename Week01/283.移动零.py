# 283.移动零.py

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
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
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


def main():
    nums = [1]
    nums = [0, 1, 0, 3, 12]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)


if __name__ == '__main__':
    main()
