# 1312. 让字符串成为回文串的最少插入次数.py


# f(i, j)定义为s[i:j]字符串成为回文串的最少插入次数
# f(i, j) = min(f(i+1, j), f(i, j-1)) + 1
# f(i, j) = f(i+1, j-1) if s[i] == s[j]
# 初始化
# f(i, i) = 0
# 返回值
# f(0, n-1)
# 优化复杂度
# 对角线递推，不优化
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
                if s[i] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j - 1])
        return dp[0][n - 1]


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][n - 1]


# f(i, j)定义为让字符串s[i:j]成为回文串的最少操作次数
# f(i, j) if s[i] == s[j] = f(i+1, j-1)
# f(i, j) else min(f(i+1, j), f(i, j-1)) + 1
# 初始化和边界条件
# f(i, i) = 0
# f(i, i-1) = 0
# 返回值f(0, n-1)
# 优化复杂度
# 对角线递推，不优化
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][n - 1]


def main():
    sol = Solution()
    s = "leetcode"
    res = sol.minInsertions(s)
    print(res)


if __name__ == '__main__':
    main()
