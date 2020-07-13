# 198. 打家劫舍.py
from typing import List


# 子问题：偷第几家房子f(i)有重复性
# 定义状态数组： 偷到第i个房子并且偷第i个房子
# 递推方程：
# f(i) = max(f(i-2), f(i-3)) + a[i]
# f(0) = 0
# f(1) = a[0]
# f(2) = a[1]
# 最大状态为max(f(n), f(n-1))
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        dp = [0] * (n + 1)
        dp[1] = nums[0]
        dp[2] = nums[1]

        for i in range(3, n + 1):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i - 1]

        return max(dp[n - 1:])


# 改进
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        dp = [0] * 4
        dp[1] = nums[0]
        dp[2] = nums[1]

        for i in range(2, n):
            dp[3] = max(dp[:2]) + nums[i]
            dp[:3] = dp[1:]
        return max(dp[1:3])


# 时间复杂度： O(n)
# 空间复杂度： O(n)


# a[i]: 0..i 能偷到 max value: a[n-1]
# a[i][0, 1]: 0:i偷， 1：i不偷
# a[i][0] = max(a[i-1][0], a[i-1][1])
# a[i][1] = a[i-1][0] + nums
# a[0][0] = 0
# a[0][1] = nums[0]
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [[0] * 2 for _ in range(2)]

        dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            dp[1][0] = max(dp[0])
            dp[1][1] = dp[0][0] + nums[i]

            dp[0][:] = dp[1]

        return max(dp[0])


# a[i]: 0..i 能偷到 max value: a[n]
# a[i]: 0..i天，且nums[i]或者nums[i-1]必偷
# a[i] = max(a[i-2] + nums[i], a[i-1])
# a[0] = nums[0]
# a[1] = max(nums[:1])
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * 3
        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, n):
            dp[2] = max(dp[0] + nums[i], dp[1])
            dp[:2] = dp[1:]

        return dp[1]


# 改进
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)

        prev_max = nums[0]
        cur_max = max(nums[:2])

        for i in range(2, n):
            prev_max, cur_max = cur_max, max(prev_max + nums[i], cur_max)

        return cur_max


# 改进
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max = cur_max = 0
        for num in nums:
            prev_max, cur_max = cur_max, max(prev_max + num, cur_max)
        return cur_max


def main():
    nums = [2, 7, 9, 3, 1]
    # nums = [1, 2, 3, 1]
    sol = Solution()
    res = sol.rob(nums)
    print(res)


if __name__ == '__main__':
    main()
