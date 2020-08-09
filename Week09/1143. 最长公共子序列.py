# 1143. 最长公共子序列.py


# 状态定义
# dp(start, j)是指text1和text2分别在i和j位置的最大子序列长度
# 递推方程
# dp(start,j) = max(dp(start-1, j) dp(start, j-1))   if s1[start] != s2[j]
#         = dp(start-1, j-1) + 1             else
# dp(0, j) = 0
# dp(start, 0) = 0
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        if m > n:
            m, n = n, m
            text1, text2 = text2, text1

        dp = [0] * (m + 1)
        dp_ = [0] * (m + 1)
        # 提前申请快很多，然后将数组重元素复制

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp_[i] = dp[i - 1] + 1
                else:
                    dp_[i] = max(dp[i], dp_[i - 1])
            dp[:] = dp_
        return dp[m]


# 以下为自我练习
# 子问题
# s1到i位置，s2到j位置的最长公共子序列
# 定义状态数组
# f(start, j)
# 递推方程
# f(start, j) = max f(start-1, j), f(start, j-1) if s1[start] != s2[j]
# f(start, j) = f(start-1, j-1) + 1          else
# 初始化
# f(0, j) = 0  j 0..n
# f(start, 0) = 0  start 0..m
# 返回值
# f(m, n)
# 优化空间复杂度
# 需要两个数组来回交替
# 可以使用短的那个字符串的长度作为数组的长度
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m < n:
            m, n = n, m
            text1, text2 = text2, text1
        dp = [0] * (n + 1)
        dp_ = [0] * (n + 1)
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp_[j + 1] = dp[j] + 1
                else:
                    dp_[j + 1] = max(dp[j + 1], dp_[j])
            dp, dp_ = dp_, dp
        return dp[n]


# 定义子问题
# start， j表示分别到i索引，和j索引的最长子序列长度
# 定义状态数组
# f(start, j)
# 递推方程
# f(start, j) = f(start-1, j-1) + 1 if s1[start] == s2[j]
# f(start, j) = max(f(start-1, j), f(start, j-1))
# 初始化
# 可以增加一维哨兵，然后都用0初始化
# 返回值
# f(m, n)
# 优化空间复杂度
# 只用一维数组即可，两个数组滚动
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m < n:
            m, n = n, m
            text1, text2 = text2, text1
        dp = [0] * (n + 1)
        ndp = [0] * (n + 1)
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    ndp[j + 1] = dp[j] + 1
                else:
                    ndp[j + 1] = max(dp[j + 1], ndp[j])
            dp, ndp = ndp, dp
        return dp[n]


# 定义子问题
# s1[:i]和s2[:j]的最长公共子序列
# f（i， j)
# 递推方程
# f(i, j) = s[i] == s[j]  f(i-1, j-1) + 1
# f(i, j) = max(f(i-1, j) f(i, j-1))
# 初始化和边界条件
# f(0, j) = 0
# 返回值返回f(m, n)
# 优化空间复杂度
# 可以两个数组滚动，数组长度为较小的数组加1
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m < n:
            m, n = n, m
            text1, text2 = text2, text1
        dp = [0] * (n + 1)
        ndp = [0] * (n + 1)
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    ndp[j + 1] = dp[j] + 1
                else:
                    ndp[j + 1] = max(dp[j + 1], ndp[j])
            dp, ndp = ndp, dp
        return dp[n]


# f(i, j) s[:i]和t[:j]的最长子序列的长度
# f(i, j) = if s[i] == t[j]  f(i-1, j-1) + 1
#           else             max(f(i-1, j), f(i, j-1))
# 初始化和边界条件
# f(0, 0) = 0
# 因为是求最大值，且最大值一定不小于0，可以用0初始化
# 返回值f(m, n)
# 优化复杂度
# 只需要两个数组来回滚动
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        if m < n:
            m, n = n, m
            s1, s2 = s2, s1
        dp = [0] * (n + 1)
        ndp = [0] * (n + 1)
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    ndp[j + 1] = dp[j] + 1
                else:
                    ndp[j + 1] = max(dp[j + 1], ndp[j])
            dp, ndp = ndp, dp
        return dp[n]


def main():
    sol = Solution()

    text1 = "abcde"
    text2 = "ace"
    res = sol.longestCommonSubsequence(text1, text2)
    print(res)

    text1 = "abc"
    text2 = "abc"
    res = sol.longestCommonSubsequence(text1, text2)
    print(res)

    text1 = "abc"
    text2 = "def"
    res = sol.longestCommonSubsequence(text1, text2)
    print(res)


if __name__ == '__main__':
    main()
