# 494. 目标和.py
from typing import List


# 定义子问题
# 数组[0..i]能组成j的方法数
# 定义状态数组
# f(i, j)
# 递推方程
# f(i, j) = f(i-1, j+a[i]) + f(i-1, j-a[i])
# 初始化
# 我们可以增加一组哨兵，替代初始化时的条件判断
# f(0, 0) = 1
# f(0, j) = 0 j != 0
# 返回值
# 返回f(n, target)
# 优化空间复杂度
# i只与前一天的情况有关，我们可以用两个数组来回交替
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)
        dp = [0] * ((total << 1) + 1)
        ndp = dp[:]
        dp[total] = 1
        for n in nums:
            for j in range(-total, total + 1):
                ndp[j] = dp[j + n] + dp[j - n]
            dp[:] = ndp
        return dp[S + total] if -total <= S <= total else 0


def main():
    sol = Solution()

    nums = [1, 1, 1, 1, 1]
    S = 3
    res = sol.findTargetSumWays(nums, S)
    print(res)


if __name__ == '__main__':
    main()
