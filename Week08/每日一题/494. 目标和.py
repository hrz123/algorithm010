# 494. 目标和.py
from typing import List


# 定义子问题
# 数组[0..start]能组成j的方法数
# 定义状态数组
# f(start, j)
# 递推方程
# f(start, j) = f(start-1, j+a[start]) + f(start-1, j-a[start])
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


# 以下为自我练习
# 定义子问题
# f(start, j)定义为nums[:start]的数组，可以凑成j目标的方法数
# f(start, j) = 加 f(start-1, j-nums[start]) + 减 f(start-1, j+nums[start])
# 初始化和边界条件
# f(0, 0) = 1, f(0, k) = 0
# j-nums[start]不能小于最小值，j+nums[start]不能大于最大值
# 最大值为sum(nums),最小值为-sum(nums)
# 返回值
# f(n, target)
# 优化空间复杂度
# 两个长度为(最大值-最小值+1)的数组交替
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)
        if S > total or S < -total:
            return 0
        size = (total << 1) + 1
        dp = [0] * total + [1] + [0] * total
        ndp = [0] * size
        for n in nums:
            for i in range(size):
                ndp[i] = (dp[i - n] if i >= n else 0) + \
                         (dp[i + n] if i + n < size else 0)
            dp, ndp = ndp, dp
        return dp[S + total]


# 定义子问题
# 对于nums[:i]。凑成j的方法数
# f(i, j)
# 新的符号是+
# f(i, j) += f(i-1, j-a[i])
# 新的符号是-
# f(i, j) = f(i-1, j+a[i])
# 初始化和边界条件
# f(0, 0) += 1
# j - a[i]， j+a[i]不能越界
# 返回值
# f(n, S）
# 优化状态空间，我们只需要两个范围数组，滚动更新
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)
        if S > total or S < -total:
            return 0
        size = (total << 1) + 1
        dp = [0] * total + [1] + [0] * total
        ndp = [0] * size
        for i in range(len(nums)):
            val = nums[i]
            for j in range(-total, total + 1):
                plus = dp[j - val + total] if j - val + total >= 0 else 0
                minus = dp[j + val + total] if j + val <= total else 0
                ndp[j + total] = plus + minus
            dp, ndp = ndp, dp
        return dp[S + total]


# 定义子问题
# f(i, j)为s[:i]中能凑出j的方法数
# f(i, j) = f(i-1, j-p) + f(i-1, j+p)
# 初始化和边界条件
# f(0, 0) = 1
# 其他都为0
# 最大target为sum，最小为-sum
# 注意递推过程不要越界
# 返回值
# f(n, target)
# 优化复杂度
# 需要两个数组滚动
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        limit = sum(nums)
        if S > limit or S < -limit:
            return 0
        size = limit * 2 + 1
        dp = [0] * size
        dp[limit] = 1
        ndp = [0] * size
        for n in nums:
            for j in range(size):
                plus = dp[j - n] if j - n >= 0 else 0
                minus = dp[j + n] if j + n < size else 0
                ndp[j] = plus + minus
            dp, ndp = ndp, dp
        return dp[S + limit]


def main():
    sol = Solution()

    nums = [1, 1, 1, 1, 1]
    S = 3
    res = sol.findTargetSumWays(nums, S)
    print(res)


if __name__ == '__main__':
    main()
