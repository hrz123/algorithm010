# 152. 乘积最大子数组.py
from typing import List


# 重复性
# 状态数组定义 dp(start)为包括i位置的最大乘积
# 递推方程：dp(start) = max(dp(start-1) * a[start], a[start]) 如果a[start]大于等于0
#         dp(start) = max(dp(start-1)[最小的值] * a[start], a[start]) 如果a[start]小于0
#         dp(start)[最小的值] = min(dp(start-1)[最小的值] * a[start], a[start]) 如果a[start]大于等于0
#         dp(start)[最小的值] = min(dp(start-1) * a[start], a[start]) 如果a[start]小于0
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
# 到i位置，且子数组一定包含nums[start]的数组，乘积最大的值
# res为这些最大值的最大数
# 定义状态数组
# f(start, j),我们还要记录最小，j=0记录最大，j=1时记录最小
# 递推方程
# f(start, 0) = f(start-1, 0) * arr[start] if arr[start] > 0
# f(start, 1) = f(start-1, 1) * arr[start]
# f(start, 0) = f(start-1, 1) * arr[start] if arr[start] < 0
# f(start, 1) = f(start-1, 0) * arr[start]
# 初始化
# f(0,0) = f(0, 1) = arr[0]
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


# 定义子问题
# 数组[0..start]的成绩连续最大子数组是多少，连续最小子数组是多少，且一定包含a[start]
# 定义状态数组
# f(start, 0) f(start, 1)
# 递推方程
# 如果a[start]是正的
# f(start, 0) = max(f(start-1, 0)*a[start] , a[start])
# f(start, 1) = min(f(start-1, 1)*a[start], a[start])
# 如果a[start]是负的
# f(start, 0) = max(f(start-1, 1)*a[start] , a[start])
# f(start, 1) = min(f(start-1, 0)*a[start],  a[start])
# 初始化
# f(0, 0) = f(0, 1) = a[0]
# 利用哨兵初始化可以为f(0, 0) = f(0, 1) = 1
# 返回值
# 返回这些最大连续子数组乘积的最大值
# 优化状态空间
# 只需要这次和上一次，可以优化只用两个值
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f0 = f1 = 1
        res = float('-inf')
        for n in nums:
            if n > 0:
                f0, f1 = max(f0 * n, n), min(f1 * n, n)
            else:
                f0, f1 = max(f1 * n, n), min(f0 * n, n)
            res = max(res, f0)
        return res


# f(i)为s[：i]数组的连续乘积最大值，且一定包含i
# 因为有负数，我们还要记录f(i)中连续数组的最小值
# f(i) a[i]为正数时，f(i)[0] = f(i-1)[0] * a[i]
#            否则   f(i)[1] = f(i-1)[1] * a[i]
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        dp0, dp1 = 1, 1
        for n in nums:
            if n > 0:
                dp0, dp1 = max(dp0 * n, n), min(dp1 * n, n)
            else:
                dp0, dp1 = max(dp1 * n, n), min(dp0 * n, n)
            res = max(res, dp0)
        return res


# 定义子问题
# f(i, 01)为s[:i]的最大乘积和最小乘积，必须包括i
# if p = a[i] > 0
# f(i, 0) = max(f(i-1, 0) * p, p)
# f(i, 1) = min(f(i-1, 1) * p, p)
# else
# f(i, 0) = max(f(i-1, 1) * p, p)
# f(i, 0) = min(f(i-1, 0) * p, p)
# 初始化和边界条件
# f(0, 01) = 1
# 返回值
# 这些最大乘积中的最大值
# 优化复杂度
# 只与i-1有关，可以只有两个值
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f0, f1 = 1, 1
        res = float('-inf')
        for num in nums:
            if num > 0:
                f0, f1 = max(f0 * num, num), min(f1 * num, num)
            else:
                f0, f1 = max(f1 * num, num), min(f0 * num, num)
            res = max(res, f0)
        return res


# 定义子问题
# f(i,01)为nums[:i]的最大和最小连续子数组乘积，且以索引i为结尾
# if nums[i] > 0
# f(i, 0) = max(f(i-1, 0) * m, m)
# f(i, 1) = min(f(i-1, 1) * m, m)
# else
# f(i, 0) = max(f(i-1, 1) * m , m)
# f(i, 1) = min(f(i-1, 0) * m , m)
# 初始化和边界条件
# f(i, 0), f(i, 1)都可以初始化为1
# 返回值
# max(f(i, 0))
# 优化复杂度
# 只需要两个变量
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f0, f1 = 1, 1
        res = float('-inf')
        for num in nums:
            if num > 0:
                f0, f1 = max(f0 * num, num), min(f1 * num, num)
            else:
                f0, f1 = max(f1 * num, num), min(f0 * num, num)
            res = max(res, f0)
        return res


def main():
    sol = Solution()

    nums = [2, 3, -2, 4]
    res = sol.maxProduct(nums)
    print(res)

    nums = [-2, 0, -1]
    res = sol.maxProduct(nums)
    print(res)


if __name__ == '__main__':
    main()
