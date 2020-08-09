# 剑指 Offer 56 - II. 数组中数字出现的次数 II.py
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x2 = x1 = 0
        for num in nums:
            x2 ^= (x1 & num)
            x1 ^= num
            mask = ~(x2 & x1)
            x2 &= mask
            x1 &= mask
        return x1


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x2 = x1 = 0
        for n in nums:
            x2 ^= (x1 & n)
            x1 ^= n
            mask = ~(x2 & x1)
            x2 &= mask
            x1 &= mask
        return x1


def main():
    sol = Solution()
    nums = [3, 4, 3, 3]
    res = sol.singleNumber(nums)
    print(res)


if __name__ == '__main__':
    main()
