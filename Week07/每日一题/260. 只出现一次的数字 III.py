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


def main():
    sol = Solution()

    nums = [1, 2, 1, 3, 2, 5]
    res = sol.singleNumber(nums)
    print(res)


if __name__ == '__main__':
    main()
