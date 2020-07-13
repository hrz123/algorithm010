# 53. 最大子序和.py
from typing import List


# 重复性
# 状态数组定义：dp(i)，表示到i位置且包括i的最大和数组
# 递推方程：dp(i) = max(0, dp(i-1)) + a(i)
# dp(0) = a[0]
# 返回max(dp)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[0]
        res = dp

        for i in range(1, len(nums)):
            dp = max(dp, 0) + nums[i]
            res = max(res, dp)

        return res


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    res = sol.maxSubArray(nums)
    print(res)


if __name__ == '__main__':
    main()
