# 188. 买卖股票的最佳时机 IV.py
from typing import List


# 子问题
# 定义状态数组
# f(start, j, k)， start 0..n-1表示第i+1天，j， 0..K表示卖出几次, k 0..1表示手里有多少股票
# max(f(n-1, 0..K, 0)
# 递推方程
# f(start, j, k) = max{
# 不动 f(start-1, j, k)
# 买入 f(start-1, j, k-1) - a[start]
# 卖出 f(start-1, j-1, k+1) + a[start]
# }
# 初始状态
# f(0, 0, 0) = 0
# f(0, 0, 1) = -a[0]
# f(0, 1, 0) = 0
# f(0, 1, 1) = -a[0]
# ...


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        # 剪枝很重要
        if k >= n - 1:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))

        dp = [[0 for _ in range(k + 1)] for _ in range(2)]
        dp_ = [[0 for _ in range(k + 1)] for _ in range(2)]

        for i in range(k + 1):
            dp[1][i] = -prices[0]

        for i in range(1, n):
            price = prices[i]

            dp_[1][0] = max(dp[1][0], -price)
            for j in range(1, k + 1):
                dp_[0][j] = max(
                    dp[0][j],
                    dp[1][j - 1] + price
                )
                dp_[1][j] = max(dp[1][j], dp[0][j] - price)

            dp[0][:] = dp_[0]
            dp[1][:] = dp_[1]

        return max(dp[0])


# 以下为自我练习
# 子问题
# 到第i天， 0..n-1,卖出了j 0..K次，手里还有k股 0..1 时的最大利润是多少
# 返回f(n-1, j, 0) j 0..K的最大值
# 定义状态数组
# f(start, j, k)
# 递推方程
# f(start, j, k) = 不动 f(start-1, j, k)
#            = 买入 f(start-1, j, k-1) - a[start]
#            = 卖出 f(start-1, j-1, k+1) + a[start]
# 取max
#
# f(start, j, 0) = 不动 f(start-1, j, 0)
#            = 卖出 f(start-1, j-1, 1) + a[start]  j >= 1
# 取max
#
# f(start, j, 1) = 不动 f(start-1, j, 1)
#            = 买入 f(start-1, j, 0) - a[start]
# 取max
# 注意边界条件
#
# 初始化
# dp(0, j, 0) = 0       j 0..k
# dp(0, j, 1) = -a[0]   j 0..k
#
# 优化空间
# 需要一个(k+1)*2的矩阵
#
# 最后注意当k >= n//2时，相当于不限做几笔交易，防止k特别大
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        if k >= n // 2:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))
        dp = [[0] * (k + 1) for _ in range(2)]
        dp_ = [[0] * (k + 1) for _ in range(2)]

        # 初始化
        for i in range(k + 1):
            dp[1][i] = -prices[0]

        for i in range(1, n):
            dp_[0][0] = dp[0][0]
            dp_[1][0] = max(dp[1][0], dp[0][0] - prices[i])
            for j in range(1, k + 1):
                dp_[0][j] = max(dp[0][j], dp[1][j - 1] + prices[i])
                dp_[1][j] = max(dp[1][j], dp[0][j] - prices[i])
            dp, dp_ = dp_, dp

        return max(dp[0])


# 定义子问题
# 0..i天卖出过j次，手里有k个股票的最大利润
# 定义状态数组
# f(start, j, k)
# 递推方程
# f(start, k, 0) = f(start-1, k, 0), 卖出 f(start-1, k-1, 1) + a[start]
# f(start, k, 1) = f(start-1, k, 1) 买入 f(start-1, k, 0) - a[start]
# 注意边界
# 初始化
# 加入哨兵初始化
# f(0, j, 0) = 0 手里没股票的最低利润就是0
# f(0, j, 1) = float('-inf') 因为都不可能达到
# 返回值
# 可以只返回f(n, k, 0)
# 优化空间复杂度
# 只关系今天和前一天，只要这两天的数组就可以
# 可以原地更新
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        if k >= len(prices) >> 1:
            return sum(max(0, prices[i + 1] - prices[i]) for i in range(len(
                prices) - 1))
        dp = [[0, float('-inf')] for _ in range(k + 1)]
        for p in prices:
            dp[0][1] = max(dp[0][1], -p)
            dp[k][0] = max(dp[k][0], dp[k - 1][1] + p)
            for i in range(k - 1, 0, -1):
                dp[i][1] = max(dp[i][1], dp[i][0] - p)
                dp[i][0] = max(dp[i][0], dp[i - 1][1] + p)
        return dp[k][0]


def main():
    sol = Solution()

    nums = [2, 4, 1]
    k = 2
    res = sol.maxProfit(k, nums)
    print(res)

    nums = [3, 2, 6, 5, 0, 3]
    k = 2
    res = sol.maxProfit(k, nums)
    print(res)

    k = 2
    nums = [3, 3, 5, 0, 0, 3, 1, 4]
    res = sol.maxProfit(k, nums)
    print(res)

    k = 0
    nums = [1, 3]
    res = sol.maxProfit(k, nums)
    print(res)


if __name__ == '__main__':
    main()
