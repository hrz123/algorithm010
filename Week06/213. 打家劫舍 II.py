# 213. 打家劫舍 II.py
from typing import List


# 子问题
# 定义状态数组
# f(i, j) 表示第i家， i:0..n-1, j, 0..1, 0表示不偷第一家，1表示偷
# 递推方程:
# f(i, j) = max(f(i-1, j), f(i-2, j) + nums[i])
# f(n-1, 1) = max(f(n-2, 1), f(n-3,j))
# 初始条件
# f(0, 0) = 0
# f(0, 1) = nums[0]
# f(1, 0) = nums[1]
# f(1, 1) = nums[0]
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [[0] * 2 for _ in range(2)]
        dp[0][1] = nums[0]
        dp[1][0] = nums[1]
        dp[1][1] = nums[0]

        for i in range(2, len(nums) - 1):
            num = nums[i]
            dp[0][0], dp[1][0] = dp[1][0], max(dp[1][0], dp[0][0] + num)
            dp[0][1], dp[1][1] = dp[1][1], max(dp[1][1], dp[0][1] + num)
        dp[0][0], dp[1][0] = dp[1][0], max(dp[1][0], dp[0][0] + nums[-1])
        dp[0][1], dp[1][1] = dp[1][1], max(dp[0][1], dp[1][1])

        return max(dp[1])


# 未完待续

def main():
    nums = [1, 2, 3, 1]
    sol = Solution()
    res = sol.rob(nums)
    print(res)


if __name__ == '__main__':
    main()
