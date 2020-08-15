# 122. 买卖股票的最佳时机 II.py
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(
            max(0, prices[i + 1] - prices[i]) for i in range(len(prices) - 1)
        )


# 以下为自我练习
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(
            max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices))
        )


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[i + 1] - prices[i]) for i in range(len(prices)
                                                                    - 1))


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[i + 1] - prices[i]) for i in range(len(
            prices) - 1))


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[i + 1] - prices[i]) for i in range(len(prices)
                                                                    - 1))


def main():
    pass


if __name__ == '__main__':
    main()
