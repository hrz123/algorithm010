# 72. 编辑距离.py


# 子问题：二维矩阵
# 定义状态数组： dp(start, j) stack1[:start]到s2[:j]的编辑距离
# 递推方程：dp(start, j) = dp(start-1, j-1) if stack1[start] == stack2[j]
#           dp(start, j) = min{dp(start-1, j), dp(start, j-1), dp(start-1, j-1)s} +1
# 增加一层哨兵，代码更好写
# dp(0, j) = 0
# dp(start, 0) = 0
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
# s[:start]到t[:j]的编辑距离
# 最终返回s[:n]到t[:m]的编辑距离
# 定义状态数组
# f(start, j)为s到i位置，t到j位置的编辑距离
# 递推方程
# f(start, j) = f(start-1, j-1)                                 if s[start-1] == t[j-1]
# f(start, j) = min(f(start-1, j), f(start, j-1), f(start-1, j-1)) + 1  else
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


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1
        dp = list(reversed(range(n + 1)))
        ndp = [0] * (n + 1)
        for i in range(m - 1, -1, -1):
            ndp[n] = m - i
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    ndp[j] = dp[j + 1]
                else:
                    ndp[j] = min(dp[j], dp[j + 1], ndp[j + 1]) + 1
            dp, ndp = ndp, dp
        return dp[0]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1
        dp = list(range(n + 1))
        ndp = [0] * (n + 1)
        for i in range(m):
            ndp[0] = i + 1
            for j in range(n):
                if word1[i] == word2[j]:
                    ndp[j + 1] = dp[j]
                else:
                    ndp[j + 1] = min(dp[j], dp[j + 1], ndp[j]) + 1
            dp, ndp = ndp, dp
        return dp[n]


#
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1
        dp = list(range(n + 1))
        ndp = [0] * (n + 1)
        for i in range(m):
            ndp[0] = i + 1
            for j in range(n):
                if word1[i] == word2[j]:
                    ndp[j + 1] = dp[j]
                else:
                    ndp[j + 1] = min(ndp[j], dp[j + 1], dp[j]) + 1
            dp, ndp = ndp, dp
        return dp[n]


# f(i, j) = f(i-1, j-1)        if s[i] ==p[j]
# f(i, j) = min(f(i-1, j), f(i, j-1), f(i-1, j-1)) + 1 else
# 初始化
# f(0, j) = j
# f(i, 0) = i
# 返回值f(n,m)
# 优化复杂度
# 可以使用两个一维数组，滚动更新
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1
        dp = list(range(n + 1))
        ndp = [0] * (n + 1)
        for i in range(m):
            ndp[0] = i + 1
            for j in range(n):
                if word1[i] == word2[j]:
                    ndp[j + 1] = dp[j]
                else:
                    ndp[j + 1] = min(dp[j], dp[j + 1], ndp[j]) + 1
            dp, ndp = ndp, dp
        return dp[n]


# 定义子问题
# f(i, j)为s[:i]到t[:j]的编辑距离
# f(i, j) = if s[i] == t[j]  f(i-1, j-1)
# f(i, j) = else min(f(i-1, j-1), f(i-1, j), f(i,j-1)) + 1
# 初始化和边界条件
# f(0, j) = j
# f(i, 0) = i
# 返回值f(n, m)
# 优化复杂度
# 我们只需要i-1的j-1和j索引，还需要i的j-1索引
# 我们可以使用两个数组滚动，数组的大小可以是两个字符串长度的较小值
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1
        dp = list(range(n + 1))
        ndp = [0 for _ in range(n + 1)]
        for i in range(m):
            ndp[0] = i + 1
            for j in range(n):
                if word1[i] == word2[j]:
                    ndp[j + 1] = dp[j]
                else:
                    ndp[j + 1] = min(dp[j + 1], dp[j], ndp[j]) + 1
            dp, ndp = ndp, dp
        return dp[n]


# 定义子问题
# f(i, j)为s[:i]到t[:j]的最小操作数
# if s[i] == t[j]
# f(i, j) = f(i-1, j-1)
# else:
# f(i, j) = min(f(i-1, j), f(i, j-1), f(i-1, j-1)) + 1
# 初始化
# f(0, j) = j
# f(i, 0) = i
# 返回值
# f(n, m)
# 优化复杂度，需要两个数组滚动，可以选用长度较短的
class Solution:
    def minDistance(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            m, n = n, m
            s, t = t, s
        dp = [*range(n + 1)]
        ndp = [0] * (n + 1)
        for i in range(m):
            ndp[0] = i + 1
            for j in range(n):
                if s[i] == t[j]:
                    ndp[j + 1] = dp[j]
                else:
                    ndp[j + 1] = min(ndp[j], dp[j + 1], dp[j]) + 1
            dp, ndp = ndp, dp
        return dp[n]


def main():
    word1 = "intention"
    word2 = "execution"

    sol = Solution()
    res = sol.minDistance(word1, word2)
    print(res)


if __name__ == '__main__':
    main()
