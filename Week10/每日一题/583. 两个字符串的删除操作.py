# 583. 两个字符串的删除操作.py


# 定义子问题
# f(i,j)s[i]到t[j]需要的最小步数
# f(i,j) s[i] == t[j]   f(i-1, j-1)
# f(i, j) else min(f(i-1, j), f(i, j-1)) + 1
# 初始化和边界条件
# 返回值
# 优化复杂度
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
                    ndp[j + 1] = min(dp[j + 1], ndp[j]) + 1
            dp, ndp = ndp, dp
        return dp[n]


# 定义子问题
# f(i,j)为s[:i]和t[:j]的最小步数
# f(i,j) if s[i] == t[j] f(i-1, j-1)
# f(i,j) else min(f(i-1, j), f(i, j-1)) + 1
# 初始化
# f(0, j) = j
# f(i, 0) = i
# 返回值
# f(m, n)
# 优化复杂度
# 两个数组滚动
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
                    ndp[j + 1] = min(dp[j + 1], ndp[j]) + 1
            dp, ndp = ndp, dp
        return dp[n]


def main():
    sol = Solution()
    a = "sea"
    b = "eat"
    res = sol.minDistance(a, b)
    print(res)


if __name__ == '__main__':
    main()
