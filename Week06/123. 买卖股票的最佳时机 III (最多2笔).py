# 123. 买卖股票的最佳时机 III (最多2笔).py
from typing import List


# 子问题
# 定义状态数组 f(start, j, k), 表示第i:0..n-1天，卖出过j:0..2次的最大值, k：0..1表示手里有股，'
# 的最大值
# max(f(n-1,0..2,0))
# 递推方程
# f(start, j, k) = max{
# 不动 f(start-1, j, k)
# 买入 f(start-1, j, k-1) - a[start]
# 卖出 f(start-1, j-1, k+1) + a[start]
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


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f01 = f11 = float('-inf')
        f10 = f20 = 0
        for p in prices:
            f01, f10, f11, f20 = (
                max(f01, -p),
                max(f10, f01 + p),
                max(f11, f10 - p),
                max(f20, f11 + p)
            )
        return f20


# 定义状态
# f(i, 0/1/2, 0/1) 表示第i天，交易了几笔，手里有几张股票的最大收益
# f(i, 0, 0) = 不动f(i-1, 0, 0) 买入 卖出
# f(i, 0, 1) = f(i-1, 0, 1), f(i-1, 0, 0) - a[i]
# f(i, 1, 0) = f(i-1, 1, 0), f(i-1, 0, 1) + a[i]
# f(i, 1, 1) = f(i-1, 1, 1), f(i-1,1, 0)- a[i]
# f(i, 2, 0) = f(i, 2, 0), f(i-1, 1, 1) + a[i]
# 初始化 f01 = f11 = float('-inf')， f10 = f20 = 0
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f01 = f11 = float('-inf')
        f10 = f20 = 0
        for p in prices:
            f01, f10, f11, f20 = (
                max(f01, -p),
                max(f10, f01 + p),
                max(f11, f10 - p),
                max(f20, f11 + p)
            )
        return f20


# 定义子问题
# f(i, 012, 01)表示第i天，已经卖出了012笔，手里还有01股票的收益
# f(i, 0, 0) = f(i-1, 0, 0)
# f(i, 0, 1) = f(i-1, 0, 1) f(i-1, 0, 0) - p
# f(i, 1, 0) = f(i-1, 1, 0) f(i-1, 0, 1) + p
# f(i, 1, 1) = f(i-1, 1, 1) f(i-1, 1, 0) - p
# f(i, 2, 0) = f(i-1, 2, 0) f(i-1, 1, 1) + p
# f(i, 2, 1)这个状态没有意义
# 初始化
# f01 = f11 = float('-inf')
# f10 = f20 = 0
# 返回值，f20是一直的最大值
# 优化复杂度
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f01 = f11 = float('-inf')
        f10 = f20 = 0
        for p in prices:
            f01, f10, f11, f20 = (
                max(f01, -p),
                max(f10, f01 + p),
                max(f11, f10 - p),
                max(f20, f11 + p)
            )
        return f20


# 定义子问题
# f(i, 012, 01)为第i天卖出了012次，手里有几股股票的最大收益
# f(i, 0, 0) = f(i-1, 0, 0)
# f(i, 0, 1) = f(i-1, 0, 1), f(i-1, 0, 0) - p,
# f(i, 1, 0) = f(i-1, 1, 0), f(i-1, 0, 1) + p
# f(i, 1, 1) = f(i-1, 1, 1), f(i-1, 1, 0) - p
# f(i, 2, 0) = f(i-1, 2, 0), f(i-1, 1, 1) + p
# 初始化
# 我们可以初始化
# f(01）， f(11)为float('-inf')
# f(10)f(20)为0
# 返回值
# 返回 f20
# 优化复杂度，我们只需要4个变量
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f01 = f11 = float('-inf')
        f10 = f20 = 0
        for p in prices:
            f01, f10, f11, f20 = (
                max(f01, -p),
                max(f10, f01 + p),
                max(f11, f10 - p),
                max(f20, f11 + p)
            )
        return f20


def main():
    sol = Solution()

    nums = [3, 3, 5, 0, 0, 3, 1, 4]
    res = sol.maxProfit(nums)
    print(res)

    nums = [1, 2, 3, 4, 5]
    res = sol.maxProfit(nums)
    print(res)


if __name__ == '__main__':
    main()
