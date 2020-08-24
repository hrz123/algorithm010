# 1262. 可被三整除的最大和.py
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for num in nums:
            mod = num % 3
            a, b, c = dp[-mod % 3], dp[(1 - mod) % 3], dp[(2 - mod) % 3]
            if a or mod == 0:
                dp[0] = max(dp[0], a + num)
            if b or mod == 1:
                dp[1] = max(dp[1], b + num)
            if c or mod == 2:
                dp[2] = max(dp[2], c + num)
        return dp[0]


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for num in nums:
            mod = num % 3
            a, b, c = dp[-mod % 3], dp[(1 - mod) % 3], dp[(2 - mod) % 3]
            if a or mod == 0:
                dp[0] = max(dp[0], a + num)
            if b or mod == 1:
                dp[1] = max(dp[1], b + num)
            if c or mod == 2:
                dp[2] = max(dp[2], c + num)
        return dp[0]


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for num in nums:
            mod = num % 3
            a, b, c = dp[-mod % 3], dp[(1 - mod) % 3], dp[(2 - mod) % 3]
            if a or mod == 0:
                dp[0] = max(dp[0], a + num)
            if b or mod == 1:
                dp[1] = max(dp[1], b + num)
            if c or mod == 2:
                dp[2] = max(dp[2], c + num)
        return dp[0]


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for num in nums:
            mod = num % 3
            a, b, c = dp[-mod % 3], dp[(1 - mod) % 3], dp[(2 - mod) % 3]
            if a or mod == 0:
                dp[0] = max(dp[0], a + num)
            if b or mod == 1:
                dp[1] = max(dp[1], b + num)
            if c or mod == 2:
                dp[2] = max(dp[2], c + num)
        return dp[0]


def main():
    sol = Solution()
    nums = [3, 6, 5, 1, 8]
    res = sol.maxSumDivThree(nums)
    print(res)


if __name__ == '__main__':
    main()
