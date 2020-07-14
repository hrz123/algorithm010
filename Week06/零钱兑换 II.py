# 零钱兑换 II.py
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
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] += dp[i - coin]
        return dp[amount]


def main():
    amount = 5
    coins = [1, 2, 5]
    sol = Solution()
    res = sol.change(amount, coins)
    print(res)


if __name__ == '__main__':
    main()
