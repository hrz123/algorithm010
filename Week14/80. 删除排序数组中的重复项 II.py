# 80. 删除排序数组中的重复项 II.py
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 2 or num > nums[i - 2]:
                nums[i] = num
                i += 1
        return i


def main():
    pass


if __name__ == '__main__':
    main()
