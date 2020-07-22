# 714. 买卖股票的最佳时机含手续费.py
from typing import List


# 子问题
# 定义状态数组 f(i, j) i 0..n-1表示第i+1天， j表示手里股数
# 递推方程
# f(i,0)= max(f(i-1,0), f(i-1, 1) + a[i] - fee)
# f(i,1)= max(f(i-1, 1), f(i-1, 0) - a[i])
# f(0, 0) = 0
# f(0, 1) = -a[0]
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size = len(prices)

        if size < 2:
            return 0

        # dp[j] 表示 [0, i] 区间内，到第 i 天（从 0 开始）状态为 j 时的最大收益
        # j = 0 表示不持股，j = 1 表示持股
        # 并且规定在买入股票的时候，扣除手续费

        dp0 = 0
        dp1 = -prices[0]

        for i in range(1, size):
            price = prices[i]
            dp0 = max(dp0, dp1 + price - fee)
            dp1 = max(dp1, dp0 - price)
        return dp0


# 以下为自我练习
# 子问题
# 到第i天，手里有j个股票的，最大收益是多少
# 定义状态数组
# f(i, 0), f(i, 1)
# 递推方程
# f(i, 0) = max 不动 f(i-1, 0) 买入 不可能 卖出 f(i-1, 1) + a[i] -fee
# f(i, 1) = max 不动 f(i-1, 1) 买入 f(i-1, 0) - a[i] 卖出 不可能
# 初始化
# f(0, 0) = 0
# f(0, 1) = -a[0]
# 返回值f(n-1, 0)
# 优化空间复杂度
# 可以只用两个值
#
# 再进一步优化，发现可以用0和负无穷初始化两个数值
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        f0, f1 = 0, float('-inf')
        for p in prices:
            f0, f1 = (
                max(f0, f1 + p - fee),
                max(f1, f0 - p)
            )
        return f0


def main():
    prices = [1, 3, 2, 8, 4, 9]
    # prices = [1, 5, 9]
    prices = [1, 3, 7, 5, 10, 3]
    prices = [9, 8, 7, 1, 2]
    prices = [1, 2]

    fee = 0
    sol = Solution()
    res = sol.maxProfit(prices, fee)
    print(res)


if __name__ == '__main__':
    main()
