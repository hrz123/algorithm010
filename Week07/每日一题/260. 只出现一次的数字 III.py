# 260. 只出现一次的数字 III.py
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        res = [0, 0]
        mask = xor & (-xor)
        for n in nums:
            if n & mask:
                res[0] ^= n
            else:
                res[1] ^= n
        return res


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x1 = 0
        for num in nums:
            x1 ^= num
        a1 = a2 = 0
        mask = x1 & (-x1)
        for num in nums:
            if num & mask:
                a1 ^= num
            else:
                a2 ^= num
        return [a1, a2]


# 以下是自我练习
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x1 = 0
        for num in nums:
            x1 ^= num
        a1 = 0
        mask = x1 & (-x1)
        for num in nums:
            if num & mask:
                a1 ^= num
        return [a1, x1 ^ a1]


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        mask = xor & (-xor)
        x1 = 0
        for n in nums:
            if n & mask:
                x1 ^= n
        return [x1, xor ^ x1]


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        mask = xor & (-xor)
        x1 = 0
        for n in nums:
            if mask & n:
                x1 ^= n
        return [x1, xor ^ x1]


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        mask = xor & (-xor)
        x1 = 0
        for n in nums:
            if n & mask:
                x1 ^= n
        return [x1, xor ^ x1]


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        mask = xor & -xor
        x1 = 0
        for n in nums:
            if n & mask:
                x1 ^= n
        return [x1, xor ^ x1]


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        mask = xor & -xor
        x1 = 0
        for num in nums:
            if num & mask:
                x1 ^= num
        return [x1, x1 ^ xor]


def main():
    sol = Solution()

    nums = [1, 2, 1, 3, 2, 5]
    res = sol.singleNumber(nums)
    print(res)


if __name__ == '__main__':
    main()
