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


def main():
    s = "abcda"
    s = "babad"
    # s = "abbd"
    sol = Solution()
    res = sol.longestPalindrome(s)
    print(res)


if __name__ == '__main__':
    main()
