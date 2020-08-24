# 1558. 得到目标数组的最少函数调用次数 .py
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        while not all(num == 0 for num in nums):
            res += 1
            for i, num in enumerate(nums):
                if num & 1:
                    res += 1
                    nums[i] -= 1
                nums[i] >>= 1
        return res - 1


def main():
    pass


if __name__ == '__main__':
    main()
