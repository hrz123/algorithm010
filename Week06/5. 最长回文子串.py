# 5. 最长回文子串.py


# 暴力解法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)

        if size < 2:
            return s
        max_len = 1
        res = s[0]

        for i in range(size - 1):
            for j in range(i + 1, size):
                if j - i + 1 > max_len and self.__isvalid(s, i, j):
                    max_len = j - i + 1
                    res = s[i: j + 1]

        return res

    def __isvalid(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


# 定义子问题: i, j之间的字符串是不是回文字符串
# 定义状态数组 f(i, j)
# 递推方程
# f(i, j) = f(i+1, j-1) + 2 if (s[i] == s[j])
# 动态规划事实上是在填一张二维表格，由构成子串。因此i和j的关系是
# i <= j, 因此只需要填这张表格对角线以上的部分。
# 边界条件是 j-1-(i+1) +1 < 2, j-i < 3
# 初始化，单个字符一定是回文串
# dp[i][i] = true
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 0
        res = (0, 0)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for k in range(1, n):
            for i in range(n - k):
                j = i + k
                if dp[i + 1][j - 1] == float('-inf'):
                    dp[i][j] = float('-inf')
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        res = (i, j)
                # 否则不可能再为回文串
                else:
                    dp[i][j] = float('-inf')

        return s[res[0]:res[1] + 1]


# 传说中的马拉车算法，不掌握，只作为爱好
class Solution:
    # Manacher algorithm
    def longestPalindrome(self, s: str) -> str:
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking.
        T = '#'.join("^{}$".format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        maxLen = centerIndex = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])
            # Attempt to expand palindrome centered at i.
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
            if P[i] > maxLen:
                maxLen = P[i]
                centerIndex = i
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]


# 以下为自我练习
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        dp = [[0] * n for _ in range(n)]
        max_len = 1
        res = s[0]
        for i in range(n):
            dp[i][i] = 1
        for j in range(0, n):
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        res = s[i:j + 1]
                else:
                    dp[i][j] = float('-inf')
        return res


# 递推公式
# dp(i, j) = dp(i+1, j-1) + 2
# dp(i, i) = 1
# dp(i, i-1) = 0
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = 1
        res = s[0]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        res = s[i:j + 1]
                else:
                    dp[i][j] = float('-inf')

        return res


def main():
    sol = Solution()

    s = "abcda"
    res = sol.longestPalindrome(s)
    print(res)
    assert res == "a"

    s = "babad"
    res = sol.longestPalindrome(s)
    print(res)
    assert res == "bab" or res == "aba"

    s = "abbd"
    res = sol.longestPalindrome(s)
    print(res)
    assert res == "bb"


if __name__ == '__main__':
    main()
