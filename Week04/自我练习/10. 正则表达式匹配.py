# 10. 正则表达式匹配.py
from functools import lru_cache


# 递归的写法
class Solution:
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = len(s) >= 1 and p[0] in {'.', s[0]}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) \
                   or (first_match and self.isMatch(s[1:], p))

        return first_match and self.isMatch(s[1:], p[1:])


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @lru_cache(None)
        def helper(i, j):
            if j == n:
                return i == m
            first_match = (i < m) and p[j] in {'.', s[i]}
            if j < n - 1 and p[j + 1] == '*':
                return helper(i, j + 2) or (first_match and helper(i + 1, j))
            return first_match and helper(i + 1, j + 1)

        return helper(0, 0)


class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        m = len(s)
        n = len(p)

        def dp(i, j):
            if (i, j) not in memo:
                if j == n:
                    ans = i == m
                else:
                    first_match = i < m and p[j] in {s[i], '.'}
                    if j < n - 1 and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


# 以下为自我练习

class Solution:
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = len(s) > 0 and p[0] in {'.', s[0]}

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) \
                   or (first_match and self.isMatch(s[1:], p))

        return first_match and self.isMatch(s[1:], p[1:])


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        m = len(s)
        n = len(p)

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == n:
                ans = i == m
            else:
                first_match = i < m and p[j] in {'.', s[i]}

                if j + 1 < n and p[j + 1] == "*":
                    ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
                else:
                    ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return memo[(i, j)]

        return dp(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @lru_cache(None)
        def helper(i, j):
            if j == n:
                return i == m

            first_match = i < m and p[j] in {'.', s[i]}

            if j + 1 < n and p[j + 1] == '*':
                return (first_match and helper(i + 1, j)) or helper(i, j + 2)

            return first_match and helper(i + 1, j + 1)

        return helper(0, 0)


# dp写法
# 子问题 s[:start]与p[:j]是否匹配
# 定义状态数组
# f(start, j)
# 递推方程：
# f(start, j) = first_match and f(start+1, j+1)    else
#           (first_match and f(start+1, j)) or f(start, j+2)
#           if j + 1 < n and p[j+1] == '*
# 初始化
# f(m, n) = True
# f(m, j) = False  j 0..n-1
# f(start, n) = False  start 0..m-1
# s到第m层是还要递推，因为p的最后字符可能是?*这种模式，导致可以匹配空
# 而p到n层，如果s还有字符，就一定不能匹配了，这是就返回false了
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[m][n] = True
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first_match = i < m and p[j] in {'.', s[i]}
                if j + 1 < n and p[j + 1] == '*':
                    dp[i][j] = (first_match and dp[i + 1][j]) or dp[i][j + 2]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}

        def helper(i, j):
            if j == n:
                return i == m
            if (i, j) in memo:
                return memo[i, j]
            first_match = i < m and p[j] in {'.', s[i]}
            if j + 1 < n and p[j + 1] == '*':
                memo[i, j] = helper(i, j + 2) or (
                        first_match and helper(i + 1, j))
            else:
                memo[i, j] = first_match and helper(i + 1, j + 1)
            return memo[i, j]

        return helper(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}

        def dfs(i, j):
            if j == n:
                return i == m
            if (i, j) in memo:
                return memo[i, j]
            first_match = i < m and p[j] in {'.', s[i]}
            if j + 1 < n and p[j + 1] == '*':
                memo[i, j] = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                memo[i, j] = first_match and dfs(i + 1, j + 1)
            return memo[i, j]

        return dfs(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        import functools
        @functools.lru_cache(None)
        def helper(i, j):
            if j == n:
                return i == m
            first_match = i < m and p[j] in {'.', s[i]}
            if j + 1 < n and p[j + 1] == '*':
                return helper(i, j + 2) or (first_match and helper(i + 1, j))
            return first_match and helper(i + 1, j + 1)

        return helper(0, 0)


def main():
    sol = Solution()
    s = "aa"
    p = 'a*'
    res = sol.isMatch(s, p)
    print(res)
    s = "aab"
    p = 'c*a*b'
    res = sol.isMatch(s, p)
    print(res)


if __name__ == '__main__':
    main()
