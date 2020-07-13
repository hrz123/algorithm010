# 152. 乘积最大子数组.py
from typing import List


# 重复性
# 状态数组定义 dp(i)为包括i位置的最大乘积
# 递推方程：dp(i) = max(dp(i-1) * a[i], a[i]) 如果a[i]大于等于0
#         dp(i) = max(dp(i-1)[最小的值] * a[i], a[i]) 如果a[i]小于0
#         dp(i)[最小的值] = min(dp(i-1)[最小的值] * a[i], a[i]) 如果a[i]大于等于0
#         dp(i)[最小的值] = min(dp(i-1) * a[i], a[i]) 如果a[i]小于0
# 最大值是max(dp[0])

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [nums[0], nums[0]]
        res = dp[0]

        for i in range(1, len(nums)):
            nums_i = nums[i]
            if nums_i >= 0:
                dp[0] = max(dp[0] * nums_i, nums_i)
                dp[1] = min(dp[1] * nums_i, nums_i)
            else:
                dp[0], dp[1] = max(dp[1] * nums_i, nums_i), min(dp[0] * nums_i,
                                                                nums_i)
            res = max(res, dp[0])

        return res


def main():
    nums = [2, 3, -2, 4]
    sol = Solution()
    res = sol.maxProduct(nums)
    print(res)


if __name__ == '__main__':
    main()
