# 309. 最佳买卖股票时机含冷冻期.py
from typing import List


# 子问题
# 定义状态数组
# f(start, j, k) start 0..n-1表示第几天, j0..1表示可不可以买，0表示可以，k 0..1表示当前手里的股票
# max{f(n-1, 0, 0), f(n-1, 1, 0)
# 递推方程
# f(start, 0, 0) = max{f(start-1, 0, 0), f(start-1, 1, 0)}
# f(start, 0, 1) = max{f(start-1, 0, 1), f(start-1, 0, 0) - a[start])}
# f(start, 1, 0) = f(start-1, 0, 1) + a[start]
# 起始状态
# f(0, 0, 0) = 0
# f(0, 0, 1) = -a[0]
# f(0, 1, 0) = 0
# 返回值
# 优化空间复杂度
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        f00 = f10 = 0
        f01 = -prices[0]

        for i in range(1, len(prices)):
            price = prices[i]
            f00, f01, f10 = max(f00, f10), max(f01, f00 - price), f01 + price
        return max(f00, f10)


# 定义子问题
# 到第i天，可以不可以买入股票（当天是否卖出）j，0表示可以，1表示不可以，k手里的股票数
# 定义状态数组
# f(start, 0, 0), f(start, 0, 1) f(start, 1, 1)
# 递推方程

# f(start, 0, 0) = 不动 max f(start-1, 0, 0) f(start-1, 1, 0)
# f(start, 0, 1) = max 不动 f(start-1, 0, 1) 买入 f(start-1, 0, 0) -a[start]
# f(start, 1, 0) = 卖出 f(start-1, 0, 1) + a[start]

# 初始化
# f(0, 0, 0 = f(0, 1, 0) = 0, f(0, 0, 1) = -a[0]

# 返回值
# 返回 f(n-1, 0, 0) f(n-1, 1, 0)中较大的

# 优化空间复杂度
# 用三个数就可以了
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        f00, f01, f10 = 0, -prices[0], 0
        for i in range(1, len(prices)):
            price = prices[i]
            f00, f01, f10 = max(f00, f10), max(f01, f00 - price), f01 + price

        return max(f00, f10)


# 注意卖出后不能买入，买入后可以卖出，只用记录卖出状态

# dp问题
# 需要记录三个状态
# i表示当前是第几天，0表示第一天
# j表示当天结束，手里剩几张股票
# k表示当天结束，是否进行过交易
# dp(start, j, k)表示在i,j,k的条件下，最大的利润
# start: 0..n-1
# j: 0..1 (本题最多保留一股)
# k: 0..1 (0今天没有卖出，1今天卖出)
# 递推方程：
# dp(start, j, 0) = max(dp(start-1, j, 0), dp(start-1, j, 1), dp(start-1, j-1, 0) - a[start])
# dp(start, j, 1) = dp(start-1, j+1, 0)
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


# 定义子问题
# 在第i天，今天卖出为1，不卖出为0，手里有k股股票的时候，最大收益是多少
# f(start, j, k)
# 递推方程
# f(start, 0, 0) = f(start-1, 0, 0), f(start-1, 1, 0)
# f(start, 0, 1) = f(start-1, 0, 1), f(start-1, 0, 0) - a[start] 买入
# f(start, 1, 0) = 卖出f(start-1, 0, 1) + a[start]
# f(start, 1, 1)这种状态不会出现
# 初始化
# f(0, 0, 0) = 0
# f(0,1,0) = 0
# f(0, 0, 1) = -a[0]
# 返回值
# f(n-1, 0, 0) f(n-1, 1, 0)的较大者
# 优化空间复杂度
# 可以只使用3个变量
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        f00, f01, f10 = 0, -prices[0], 0
        for i in range(1, len(prices)):
            f00, f01, f10 = (
                max(f00, f10),
                max(f01, f00 - prices[i]),
                f01 + prices[i]
            )
        return max(f00, f10)


# 定义子问题
# 在第i天，这天结束后你不能1或能0买入股票，并且结束后手中有k个股票的最大利润
# 定义状态数组
# f(start, j, k)
# 递推方程
# f(start, 0, 0) = 不动 f(start-1, 0, 0) f(start-1, 1, 0)
# f(start, 0, 1) = 不动 f(start-1, 0, 1) 买入 f(start-1, 0, 0) - a[start]
# f(start, 1, 0) = 卖出 f(start-1, 0, 1) + a[start]
# f(start, 1, 1) 不存在
# 初始化
# f00 = 0
# f01 = -p
# f10 = 0
# 加入哨兵
# f00 = 0
# f01 = float('-inf')
# f10 = 0
# 返回值
# 返回 f00 f10的最大值
# 优化空间复杂度
# 只需要三个变量
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f00, f01, f10 = 0, float('-inf'), 0
        for p in prices:
            f00, f01, f10 = (
                max(f00, f10),
                max(f01, f00 - p),
                f01 + p
            )
        return f10


# f(i, 0/1, 0/1)表示第i天，是否卖出，手里有几张股票
# f(i, 0, 0) = f(i-1, 0, 0), f(i-1, 1, 0)
# f(i, 0, 1) = f(i-1, 0, 1), f(i-1, 0, 0) - p
# f(i, 1, 0) = f(i-1, 0, 1) + p
# 初始化
# f00, f10 = 0, f01 = float('-inf')
# 返回值
# max(f00, f10)
# 优化复杂度
# 只需要三个变量
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f00 = f10 = 0
        f01 = float('-inf')
        for p in prices:
            f00, f01, f10 = (
                max(f00, f10),
                max(f01, f00 - p),
                f01 + p
            )
        return max(f00, f10)


# 定义子问题
# f(i, j, k) 为i天，当天是否卖出股票，手里是否有股票
# f00 = f00, f10
# f01 = f01, f00 - p
# f10 = f01 + p
# f11没有这种状态
# 初始化和边界条件
# f00,f10 = 0, f01 = float('-inf')
# 返回值f00和f10中的最大值
# 优化复杂度
# 只需要三个值
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f00 = f10 = 0
        f01 = float('-inf')
        for p in prices:
            f00, f01, f10 = (
                max(f00, f10),
                max(f01, f00 - p),
                f01 + p
            )
        return max(f00, f10)


# f(i, 01, 01)表示i天，是否卖出股票，手里有几张股票的最大收益
# f(i, 0, 0) = f(i-1, 0, 0), f(i-1, 1, 0)
# f(i, 0, 1) = f(i-1, 0, 1), f(i-1, 0, 0) - p
# f(i, 1, 0) = f(i-1, 1, 0), 卖出 f(i-1, 0, 1) + p
# f(i, 1, 1) = 不可能卖出了手里还有一股股票
# 初始化
# f00 , f10 = 0, f01 = float('-inf')
# 返回值
# f10, f00中的最大值
# 优化复杂度
# 只需要三个变量
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f00, f10 = 0, 0
        f01 = float('-inf')
        for p in prices:
            f00, f01, f10 = (
                max(f00, f10),
                max(f01, f00 - p),
                max(f10, f01 + p)
            )
        return max(f00, f10)


def main():
    sol = Solution()

    prices = [6, 1, 3, 2, 4, 7]
    res = sol.maxProfit(prices)
    print(res)

    nums = [1, 2, 3, 0, 2]
    res = sol.maxProfit(nums)
    print(res)


if __name__ == '__main__':
    main()
