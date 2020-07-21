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


# 以下为自我练习
# 子问题
# 到i位置，且子数组一定包含nums[i]的数组，乘积最大的值
# res为这些最大值的最大数
# 定义状态数组
# f(i, j),我们还要记录最小，j=0记录最大，j=1时记录最小
# 递推方程
# f(i, 0) = f(i-1, 0) * nums[i] if nums[i] > 0
# f(i, 1) = f(i-1, 1) * nums[i]
# f(i, 0) = f(i-1, 1) * nums[i] if nums[i] < 0
# f(i, 1) = f(i-1, 0) * nums[i]
# 初始化
# f(0,0) = f(0, 1) = nums[0]
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_value = min_value = nums[0]
        res = max_value

        for i in range(1, len(nums)):
            nums_i = nums[i]
            if nums_i >= 0:
                max_value, min_value = max_value * nums_i, min_value * nums_i
            else:
                max_value, min_value = min_value * nums_i, max_value * nums_i
            max_value = max(max_value, nums_i)
            min_value = min(min_value, nums_i)
            res = max(res, max_value)
        return res


def main():
    nums = [2, 3, -2, 4]
    sol = Solution()
    res = sol.maxProduct(nums)
    print(res)


if __name__ == '__main__':
    main()
