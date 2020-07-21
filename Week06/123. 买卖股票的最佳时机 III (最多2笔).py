# 123. 买卖股票的最佳时机 III (最多2笔).py
from typing import List


# 子问题
# 定义状态数组 f(i, j, k), 表示第i:0..n-1天，卖出过j:0..2次的最大值, k：0..1表示手里有股，'
# 的最大值
# max(f(n-1,0..2,0))
# 递推方程
# f(i, j, k) = max{
# 不动 f(i-1, j, k)
# 买入 f(i-1, j, k-1) - a[i]
# 卖出 f(i-1, j-1, k+1) + a[i]
# }
# 注意边界条件
# 起始条件
# f(0, 0, 0) = 0
# f(0, 0, 1) = -a[0]
# f(0, 1, 0) = 0
# f(0, 1, 1) = -a[0]
# f(0, 2, 0) = 0
# f(0, 2, 1) = -a[0]
# 最小用6
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        d00 = d10 = d20 = 0
        d01 = d11 = -prices[0]

        for i in range(1, len(prices)):
            price = prices[i]
            # nd00 = d00
            nd10 = max(d10, d01 + price)
            nd20 = max(d20, d11 + price)
            nd01 = max(d01, d00 - price)
            nd11 = max(d11, d10 - price)
            # nd21 = max(d21, d20 - price)

            d10, d20, d01, d11 = nd10, nd20, nd01, nd11

        return max(d00, d10, d20)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        d00 = d10 = d20 = 0
        d01 = d11 = -prices[0]

        for i in range(1, len(prices)):
            price = prices[i]
            d10, d20, d01, d11 = (
                max(d10, d01 + price),
                max(d20, d11 + price),
                max(d01, d00 - price),
                max(d11, d10 - price)
            )

        return max(d00, d10, d20)


# 以下为自我练习

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        dp00 = dp10 = dp20 = 0
        dp01 = dp11 = -prices[0]

        for i in range(1, len(prices)):
            dp10, dp20, dp01, dp11 = (
                max(dp10, dp01 + prices[i]),
                max(dp20, dp11 + prices[i]),
                max(dp01, dp00 - prices[i]),
                max(dp11, dp10 - prices[i])
            )
        # dp10永远为0，dp10永远大于等于0
        return max(dp10, dp20)


def main():
    nums = [3, 3, 5, 0, 0, 3, 1, 4]
    nums = [1, 2, 3, 4, 5]
    sol = Solution()
    res = sol.maxProfit(nums)
    print(res)


if __name__ == '__main__':
    main()
