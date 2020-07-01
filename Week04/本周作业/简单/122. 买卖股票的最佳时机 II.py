# 122. 买卖股票的最佳时机 II.py
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[i + 1] - prices[i]) for i in range(len(
            prices) - 1))


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            pricesi = prices[i]
            pricesi_1 = prices[i - 1]
            if pricesi > pricesi_1:
                res += pricesi - pricesi_1
        return res


def main():
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    res = sol.maxProfit(prices)
    print(res)


if __name__ == '__main__':
    main()
