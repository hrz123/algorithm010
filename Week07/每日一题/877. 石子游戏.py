# 877. 石子游戏.py
from typing import List


# 数学规律
#
# 先拿者可以拿到序号为 1,3,5...n-1 的石子堆，
# 也可以拿到序号为 2,4,6...n 的石子堆。
# 因为总石子数为奇数，所以这两种方式中，其中一种拿到的石子数大于另一种。
# 所以不按照拿尽量多的石子数，按照这种纯奇数序号或者纯偶数序号的方式拿，先拿者总可以赢。

# https://leetcode-cn.com/problems/stone-game/solution/jie-jue-bo-yi-wen-ti-de-dong-tai-gui-hua-tong-yong/
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


# 这道道规定了石子堆的个数是偶数
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if not piles:
            return True
        n = len(piles)
        dp = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i][0] = piles[i]
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                left = dp[i + 1][j][1] + piles[i]
                right = dp[i][j - 1][1] + piles[j]
                # 先手选左边
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]
                # 先手选右边
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0]
        return bool(dp[0][n - 1][0] - dp[0][n - 1][1])


def main():
    sol = Solution()

    piles = [5, 3, 4, 5]
    res = sol.stoneGame(piles)
    print(res)


if __name__ == '__main__':
    main()
