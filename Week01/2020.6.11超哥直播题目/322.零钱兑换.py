# 322.零钱兑换.py

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 自底向上
        # dp[start] 表示金额为i需要最少的硬币
        # dp[start] = min(dp[start], dp[start - coins[j]]) j所有硬币

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min(
                dp[i - c] if i - c >= 0 else float("inf") for c in coins) + 1
        return dp[-1] if dp[-1] != float("inf") else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        _max = float('inf')
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] if i >= c else _max for c in coins) + 1
        return -1 if dp[amount] == _max else dp[amount]


# f(i) = min(f(i-c)) + 1
# 初始值
# f(0) = 0
# 其他的值因为我们求最小值，我们可以初始化一个极大值，float('inf')
# 返回值f(target)
# 优化复杂度
# 无法优化
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]


def main():
    sol = Solution()

    coins = [1, 2, 5]
    amount = 11
    res = sol.coinChange(coins, amount)
    print(res)


if __name__ == '__main__':
    main()
