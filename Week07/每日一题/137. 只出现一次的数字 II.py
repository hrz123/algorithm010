# 137. 只出现一次的数字 II.py
from typing import List


# 思路详见：https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 因为k是3
        x2 = x1 = 0
        for num in nums:
            x2 ^= (x1 & num)
            x1 ^= num
            mask = ~(x2 & x1)  # 因为k是3
            x2 &= mask
            x1 &= mask
        return x1  # 因为p是1


# 以下为自我练习
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1 = x2 = 0
        for n in nums:
            x2 ^= (x1 & n)
            x1 ^= n
            mask = ~(x1 & x2)
            print(mask)
            x2 &= mask
            x1 &= mask
        return x1


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1 = x2 = 0
        for n in nums:
            x2 ^= x1 & n
            x1 ^= n
            mask = ~(x2 & x1)
            x2 &= mask
            x1 &= mask
        return x1


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1 = x2 = 0
        for n in nums:
            x2 ^= (x1 & n)
            x1 ^= n
            mask = ~(x1 & x2)
            x2 &= mask
            x1 &= mask
        return x1


def main():
    sol = Solution()

    nums = [2, 2, 3, 2]
    res = sol.singleNumber(nums)
    print(res)

    nums = [0, 1, 0, 1, 0, 1, 99]
    res = sol.singleNumber(nums)
    print(res)


if __name__ == '__main__':
    main()
