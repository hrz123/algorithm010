# 解决博弈问题动态规划通用思路.py


# 我们把石头游戏改得更具有一般性
# 你和你的朋友面前有一排石头堆，用一个数组piles表示
# piles[start]表示第i堆石子有多少个。
# 你们轮流拿石头，一次拿一堆，但是只能拿走最左边或者最右边的石头堆。
# 所有石头被拿完后，谁拥有的石头多，谁获胜
# 假设两人都很聪明，请你设计一个算法，返回先手和后手最后得分（石头总数）之差
# 比如：
# piles = [1, 100, 3]
# 先手能得4分，后手能得100分，返回-96

# 思路
# 子问题
# 在第i到第j堆石头，先手能获得最大石头数是多少，后手是多少
# 定义状态数组
# f(start, j, 0) f(start, j, 1) 表示第i到第j个石头，包括第i和第j个，0表示先手，1表示后手
# 因为两人都极聪明，先手选完就变后手，来回交替的
# 递推方程
# f(start, j, 0) = max 拿左边 f(start+1, j, 1) + a[start]
#            =     拿右边 f(start, j-1, 1) + a[j]
# 知道了拿左边还是右边后
# f(start, j, 1) =     先手拿左边 f(start+1, j, 0)
#            =     先手拿右边 f(start, j-1, 0)
# 初始化
# f(start, start, 0) = a[start] 只有一堆石子的时候，先手为该堆石子个数，后手就为0
# f(start, start, 1) = 0
# 返回值
# f(0, m-1, 0) 先手最终石子数 - f(0, m-1, 1)后手最终石子数
# 优化空间复杂度
# 是对角线的递推，这种情况最好不要优化空间，还可以利用计算机的缓存
from typing import List


class Solution:
    def game(self, piles: List[int]) -> int:
        if not piles:
            return 0
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
        return dp[0][n - 1][0] - dp[0][n - 1][1]


# 定义子问题
# f(i, j, 01)表示s[i, j]中先后手的最大分数
# 递推方程
# f(i, j, 0) = max(f(i+1, j, 1) + a[i], f(i, j-1, 1) + a[j])
# f(i, j, 1) = f(i+1, j, 0), f(i, j-1, 0),看先手的情况
# 初始化
# f(i, i, 0) = a[i]
# f(i, i, 1) = 0
# 返回值
# f(0, m-1, 1) - f(0, m-1, 0)
# 优化复杂度
# 对角线递推，不优化
class Solution:
    def game(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i][0] = piles[i]
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                left = dp[i + 1][j][1] + piles[i]
                right = dp[i][j - 1][1] + piles[j]
                if left >= right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0]
        return dp[0][n - 1][0] - dp[0][n - 1][1]


def main():
    sol = Solution()

    piles = [1, 100, 3, 1]
    res = sol.game(piles)
    print(res)


if __name__ == '__main__':
    main()
