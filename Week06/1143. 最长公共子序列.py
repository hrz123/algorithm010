# 1143. 最长公共子序列.py


# 状态定义
# dp(i, j)是指text1和text2分别在i和j位置的最大子序列长度
# 递推方程
# dp(i,j) = max(dp(i-1, j) dp(i, j-1))   if s1[i] != s2[j]
#         = dp(i-1, j-1) + 1             else
# dp(0, j) = 0
# dp(i, 0) = 0
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
# f(i, j)
# 递推方程
# f(i, j) = max f(i-1, j), f(i, j-1) if s1[i] != s2[j]
# f(i, j) = f(i-1, j-1) + 1          else
# 初始化
# f(0, j) = 0  j 0..n
# f(i, 0) = 0  i 0..m
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
