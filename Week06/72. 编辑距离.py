# 72. 编辑距离.py


# 子问题：二维矩阵
# 定义状态数组： dp(i, j) s1[:i]到s2[:j]的编辑距离
# 递推方程：dp(i, j) = dp(i-1, j-1) if s1[i] == s2[j]
#           dp(i, j) = min{dp(i-1, j), dp(i, j-1), dp(i-1, j-1)s} +1
# 增加一层哨兵，代码更好写
# dp(0, j) = 0
# dp(i, 0) = 0
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m > n:
            m, n = n, m
            word1, word2 = word2, word1

        dp = range(m + 1)
        dp_ = [0] * (m + 1)

        for j, c2 in enumerate(word2):
            dp_[0] = j + 1
            for i, c1 in enumerate(word1):
                if c1 == c2:
                    dp_[i + 1] = dp[i]
                else:
                    dp_[i + 1] = min(dp[i], dp[i + 1], dp_[i]) + 1
            dp = dp_[:]

        return dp[m]


def main():
    word1 = "intention"
    word2 = "execution"

    sol = Solution()
    res = sol.minDistance(word1, word2)
    print(res)


if __name__ == '__main__':
    main()
