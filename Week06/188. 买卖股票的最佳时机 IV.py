# 188. 买卖股票的最佳时机 IV.py
from typing import List


# 子问题
# 定义状态数组
# f(i, j, k)， i 0..n-1表示第i+1天，j， 0..K表示卖出几次, k 0..1表示手里有多少股票
# max(f(n-1, 0..K, 0)
# 递推方程
# f(i, j, k) = max{
# 不动 f(i-1, j, k)
# 买入 f(i-1, j, k-1) - a[i]
# 卖出 f(i-1, j-1, k+1) + a[i]
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


def main():
    nums = [2, 4, 1]
    # nums = [3, 2, 6, 5, 0, 3]
    k = 100000000000
    sol = Solution()
    res = sol.maxProfit(k, nums)
    print(res)


if __name__ == '__main__':
    main()
