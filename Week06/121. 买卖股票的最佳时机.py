# 121. 买卖股票的最佳时机.py
from typing import List


# 只能完成一笔交易
# 子问题
# 定义状态数组: f(i)为第i+1天卖出的最大值, max(f(i))
# 递推方程
# f(i) = max(f(i-1) + a[i] - a[i-1], 0)
# f(0) = 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = 0
        res = 0
        for i in range(1, len(prices)):
            x += prices[i] - prices[i - 1]
            x = max(x, 0)
            res = max(res, x)
        return res


def main():
    nums = [7, 1, 5, 3, 6, 4]
    nums = [7, 6, 5, 4, 3]
    sol = Solution()
    res = sol.maxProfit(nums)
    print(res)


if __name__ == '__main__':
    main()
