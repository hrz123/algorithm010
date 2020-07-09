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


def main():
    sol = Solution()
    s = "aa"
    p = 'a'
    res = sol.isMatch(s, p)
    print(res)


if __name__ == '__main__':
    main()
