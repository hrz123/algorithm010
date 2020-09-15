# 5502. 将子数组重新排序得到同一个二叉查找树的方案数 .py
import math
from typing import List


class Solution:
    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 1

        pivot = nums[0]
        nums_left = [num for num in nums if num < pivot]
        nums_right = [num for num in nums if num > pivot]
        return self.combine(len(nums) - 1, len(nums_left)) * self.helper(
            nums_left) * self.helper(nums_right) % (10 ** 9 + 7)

    def combine(self, n, m):
        return math.factorial(n) // (
                math.factorial(m) * math.factorial(n - m))

    def numOfWays(self, nums: List[int]) -> int:
        return self.helper(nums) - 1


def main():
    sol = Solution()

    nums = [2, 1, 3]
    res = sol.numOfWays(nums)
    print(res)
    assert res == 1

    nums = [3, 4, 5, 1, 2]
    res = sol.numOfWays(nums)
    print(res)
    assert res == 5

    nums = [1, 2, 3]
    res = sol.numOfWays(nums)
    print(res)
    assert res == 0

    nums = [3, 1, 2, 5, 4, 6]
    res = sol.numOfWays(nums)
    print(res)
    assert res == 19

    nums = [9, 4, 2, 1, 3, 6, 5, 7, 8, 14, 11, 10, 12, 13, 16, 15, 17, 18]
    res = sol.numOfWays(nums)
    print(res)
    assert res == 216212978


if __name__ == '__main__':
    main()
