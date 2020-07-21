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


# 以下为自我练习

# 定义子问题
# s[:i]到t[:j]的编辑距离
# 最终返回s[:m]到t[:n]的编辑距离
# 定义状态数组
# f(i, j)为s到i位置，t到j位置的编辑距离
# 递推方程
# f(i, j) = f(i-1, j-1)                                 if s[i-1] == t[j-1]
# f(i, j) = min(f(i-1, j), f(i, j-1), f(i-1, j-1)) + 1  else
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
                    dp_[i + 1] = min(dp[i + 1], dp[i], dp_[i]) + 1
            dp = dp_[:]
        return dp[m]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1
        dp = list(range(n + 1))
        dp_ = [0] * (n + 1)

        for i, c1 in enumerate(word1):
            dp_[0] = i + 1
            for j, c2 in enumerate(word2):
                if c1 == c2:
                    dp_[j + 1] = dp[j]
                else:
                    dp_[j + 1] = min(dp[j + 1], dp[j], dp_[j]) + 1
            dp[:] = dp_
        return dp[n]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m > n:
            m, n = n, m
            word1, word2 = word2, word1
        dp = list(range(n + 1))
        dp_ = [0] * (n + 1)

        for i, c1 in enumerate(word1):
            dp_[0] = i + 1
            for j, c2 in enumerate(word2):
                if c1 == c2:
                    dp_[j + 1] = dp[j]
                else:
                    dp_[j + 1] = min(dp[j + 1], dp[j], dp_[j]) + 1
            dp[:] = dp_
        return dp[n]


def main():
    word1 = "intention"
    word2 = "execution"

    sol = Solution()
    res = sol.minDistance(word1, word2)
    print(res)


if __name__ == '__main__':
    main()
