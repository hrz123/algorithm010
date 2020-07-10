# 309. 最佳买卖股票时机含冷冻期.py
from typing import List


# 注意卖出后不能买入，买入后可以卖出，只用记录卖出状态

# dp问题
# 需要记录三个状态
# i表示当前是第几天，0表示第一天
# j表示当天结束，手里剩几张股票
# k表示当天结束，是否进行过交易
# dp(i, j, k)表示在i,j,k的条件下，最大的利润
# i: 0..n-1
# j: 0..1 (本题最多保留一股)
# k: 0..1 (0今天没有卖出，1今天卖出)
# 递推方程：
# dp(i, j, 0) = max(dp(i-1, j, 0), dp(i-1, j, 1), dp(i-1, j-1, 0) - a[i])
# dp(i, j, 1) = dp(i-1, j+1, 0)
# 注意边界条件
# 起始条件：
# dp(0, 0, 0) = 0
# dp(0, 0, 1) = float('-inf') 不可能没有股票并卖出了
# dp(0, 1, 0) = -prices[0] 今天买入了股票
# dp(0, 1, 1) = float('-inf') 不可能有股票并卖出了
# 递推时要注意j的边界
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        size = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)]

        dp[0][1][0] = -prices[0]
        dp[0][0][1] = float('-inf')
        dp[0][1][1] = float('-inf')

        for i in range(1, size):
            for j in range(2):
                # 更新k为0和1的位置
                # 不动时
                dp[1][j][0] = max(
                    dp[0][j][0],  # 昨天也不动或买入
                    dp[0][j][1],  # 昨天卖出，今天不动
                )

                if j == 1:
                    # 买入时
                    # 没有股时才能买入
                    dp[1][j][0] = max(dp[1][j][0],
                                      dp[0][j - 1][0] - prices[i])
                    # 卖出后手里还有一股
                    # 此时也要更新k为1的位置，因为有一股时今天不可能卖出，在不可能地方标记上负无穷
                    dp[1][j][1] = float('-inf')

                else:
                    # 今天卖出，手里没股
                    dp[1][j][1] = dp[0][j + 1][0] + prices[i]

            for j in range(2):
                for k in range(2):
                    dp[0][j][k] = dp[1][j][k]

        return max(dp[0][0][0], dp[0][0][1])


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        size = len(prices)
        dp = [[[float('-inf') for _ in range(2)] for _ in range(2)] for _ in
              range(2)]

        dp[0][0][0] = 0
        dp[0][1][0] = -prices[0]

        for i in range(1, size):
            for j in range(2):
                # 更新k为0和1的位置
                # 不动时
                dp[1][j][0] = max(
                    dp[0][j][0],  # 昨天也不动或买入
                    dp[0][j][1],  # 昨天卖出，今天不动
                )

                if j == 1:
                    # 买入时
                    # 没有股时才能买入
                    dp[1][j][0] = max(dp[1][j][0],
                                      dp[0][j - 1][0] - prices[i])
                    # 卖出后手里还有一股
                    # 此时也要更新k为1的位置，因为有一股时今天不可能卖出，在不可能地方标记上负无穷
                    # dp[1][j][1] = float('-inf')

                else:
                    # 今天卖出，手里没股
                    dp[1][j][1] = dp[0][j + 1][0] + prices[i]

            for j in range(2):
                for k in range(2):
                    dp[0][j][k] = dp[1][j][k]

        return max(dp[0][0][0], dp[0][0][1])


def main():
    prices = [6, 1, 3, 2, 4, 7]
    sol = Solution()
    res = sol.maxProfit(prices)
    print(res)


if __name__ == '__main__':
    main()
