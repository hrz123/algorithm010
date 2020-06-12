# 322.零钱兑换.py

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 自底向上
        # dp[i] 表示金额为i需要最少的硬币
        # dp[i] = min(dp[i], dp[i - coins[j]]) j所有硬币

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min(
                dp[i - c] if i - c >= 0 else float("inf") for c in coins) + 1
        return dp[-1] if dp[-1] != float("inf") else -1


def main():
    pass


if __name__ == '__main__':
    main()
