# 53. 最大子序和.py
from typing import List


# 重复性
# 状态数组定义：dp(i)，表示到i位置且包括i的最大和数组
# 递推方程：dp(i) = max(0, dp(i-1)) + a(i)
# dp(0) = a[0]
# 返回max(dp)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = 0
        res = nums[0]

        for num in nums:
            dp = max(dp, 0) + num
            res = max(res, dp)

        return res


# 以下为自我练习
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[0]
        res = dp
        for i in range(1, len(nums)):
            dp = max(dp, 0) + nums[i]
            res = max(res, dp)
        return res


# 子问题
# 定义到i位置，且必须包含i位置的连续数组最大和为dp(i)
# 最终返回max(dp(i)), i 0..n-1
# 定义状态数组
# dp(i)
# 递推方程
# dp(i) = max(dp(i-1), 0) + nums[i]
# 初始化dp(0) = nums[0]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = nums[0]
        global_max = local_max
        for i in range(1, len(nums)):
            local_max = max(0, local_max) + nums[i]
            global_max = max(global_max, local_max)
        return global_max


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _sum, res = 0, float('-inf')
        for num in nums:
            _sum = max(_sum + num, num)
            res = max(res, _sum)
        return res


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    res = sol.maxSubArray(nums)
    print(res)


if __name__ == '__main__':
    main()
