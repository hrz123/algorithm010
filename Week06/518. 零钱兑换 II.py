# 518. 零钱兑换 II.py
from typing import List


# 题解：https://leetcode-cn.com/problems/coin-change-2/solution/ling-qian-dui-huan-iihe-pa-lou-ti-wen-ti-dao-di-yo/
# class Solution1 {
# public:
#     int change(int amount, vector<int>& coins) {
#         int dp[amount+1];
#         memset(dp, 0, sizeof(dp)); //初始化数组为0
#         dp[0] = 1;
#         for (int j = 1; j <= amount; j++){ //枚举金额
#             for (int coin : coins){ //枚举硬币
#                 if (j < coin) continue; // coin不能大于amount
#                 dp[j] += dp[j-coin];
#             }
#         }
#         return dp[amount];
#     }
# };
# class Solution2 {
# public:
#     int change(int amount, vector<int>& coins) {
#         int dp[amount+1];
#         memset(dp, 0, sizeof(dp)); //初始化数组为0
#         dp[0] = 1;
#         for (int coin : coins){ //枚举硬币
#             for (int j = 1; j <= amount; j++){ //枚举金额
#                 if (j < coin) continue; // coin不能大于amount
#                 dp[j] += dp[j-coin];
#             }
#         }
#         return dp[amount];
#     }
# };

# 定义子问题
# 定义状态数组
# 定义递推方程
# 这道题的子问题应该这么定义
# 前k个硬币凑齐i金额的组合数等于前k-1个硬币凑齐i金额的组合数和前k个硬币凑齐i-coins[k]金额的组合数
# f(k, i) = f(k-1, i) + f(k, i - coins[k-1])  if i >= coins[k]
# f(k, i) = f(k-1, i)                       else
# f(0, 0) = 1
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        dp = [[0] * (amount + 1) for _ in range(m + 1)]
        for k in range(m + 1):
            dp[k][0] = 1
        for k in range(1, m + 1):
            for i in range(1, amount + 1):
                if i >= coins[k - 1]:
                    dp[k][i] = dp[k - 1][i] + dp[k][i - coins[k - 1]]
                else:
                    dp[k][i] = dp[k - 1][i]
        return dp[m][amount]


# 之前爬楼梯问题中，我们将一维数组降维成点。这里问题能不能也试着降低一个维度，只用一个数组进行表示呢
# 这个时候，我们就需要重新定义我们的子问题了。
# 此时的子问题是，对于硬币从0到k，我们必须使用第k个硬币的时候，当前金额的组合数。
# 因此状态数组DP[i]表示的是对于第k个硬币能凑的组合数。
# 状态转移方程如下
# dp[i] = dp[i] + dp[i-coins[k]]
# 于是得到solution
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] += dp[i - coin]
        return dp[amount]


# 这里的内外循环能换吗？
# 显然不能，因为我们这里定义的子问题是，必须选择第k个硬币时，凑成金额的方案。
# 如果交换了，我们的子问题就变成了，对于金额i，我们选择硬币的方案。
# 同样的，我们回答之前爬楼梯的留下的问题，元勋结构对应的子问题是，对于楼梯数i，
# 我们的爬楼梯方案。第二种循环结构则是，固定爬楼梯的顺序，我们爬楼梯的方案，
# 也就是第一种循环下，对于楼梯3，你可以先2再1，或者先1再2，
# 但是对于第二种循环，对于楼梯3，你只能先1再2，不能先2再1。（假如coins中1在2前面）


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(1, amount + 1):
                dp[i] += dp[i - c] if i >= c else 0
        return dp[amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(1, amount + 1):
                if i >= c:
                    dp[i] += dp[i - c]
        return dp[amount]


def main():
    sol = Solution()

    amount = 5
    coins = [1, 2, 5]
    res = sol.change(amount, coins)
    print(res)

    amount = 3
    coins = [2]
    res = sol.change(amount, coins)
    print(res)

    amount = 10
    coins = [10]
    res = sol.change(amount, coins)
    print(res)


if __name__ == '__main__':
    main()
