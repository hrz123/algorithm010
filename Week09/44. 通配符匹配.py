# 44. 通配符匹配.py
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if p[0] == '*':
            return self.isMatch(s, p[1:]) \
                   or (len(s) >= 1 and self.isMatch(s[1:], p))
        first_match = len(s) >= 1 and p[0] in {'?', s[0]}

        return first_match and self.isMatch(s[1:], p[1:])


# 每个字符串都是新的一块内存空间，申请内存空间增加了时间和空间复杂度

# 改进，字符串只有s和p，用指针指向开头的位置
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)

        @lru_cache(None)
        def helper(i, j):
            if j == n:
                return i == m
            if p[j] == '*':
                return helper(i, j + 1) or (i < m and helper(i + 1, j))
            first_match = i < m and p[j] in {'?', s[i]}
            return first_match and helper(i + 1, j + 1)

        return helper(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        @lru_cache(None)
        def helper(i, j):
            if j == n:
                return i == m

            if p[j] == '*':
                return helper(i, j + 1) or (i < m and helper(i + 1, j))

            first_match = i < m and p[j] in {s[i], '?'}
            return first_match and helper(i + 1, j + 1)

        return helper(0, 0)


class Solution:
    memo = {}

    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if (s, p) in self.memo:
            return self.memo[s, p]
        if p[0] == '*':
            self.memo[s, p] = self.isMatch(s, p[1:]) \
                              or len(s) > 0 and self.isMatch(s[1:], p)
            return self.memo[s, p]
        first_match = len(s) > 0 and p[0] in {'?', s[0]}
        self.memo[s, p] = first_match and self.isMatch(s[1:], p[1:])
        return self.memo[s, p]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}

        def helper(i, j):
            if j == n:
                return i == m
            if (i, j) in memo:
                return memo[i, j]
            if p[j] == '*':
                memo[i, j] = helper(i, j + 1) or i < m and helper(i + 1, j)
            else:
                first_match = i < m and p[j] in {'?', s[i]}
                memo[i, j] = first_match and helper(i + 1, j + 1)
            return memo[i, j]

        return helper(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}

        def helper(i, j):
            if j == n:
                return i == m
            if (i, j) in memo:
                return memo[i, j]
            if p[j] == '*':
                memo[i, j] = helper(i, j + 1) or (i < m and helper(i + 1, j))
            else:
                first_match = i < m and p[j] in {'?', s[i]}
                memo[i, j] = first_match and helper(i + 1, j + 1)
            return memo[i, j]

        return helper(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}

        def helper(i, j):
            if j == n:
                return i == m
            if (i, j) in memo:
                return memo[i, j]
            if p[j] == '*':
                memo[i, j] = helper(i, j + 1) or (i < m and helper(i + 1, j))
            else:
                memo[i, j] = i < m and p[j] in {'?', s[i]} and helper(i + 1,
                                                                      j + 1)
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
            if p[j] == '*':
                memo[i, j] = dfs(i, j + 1) or (i < m and dfs(i + 1, j))
            else:
                memo[i, j] = i < m and p[j] in {'?', s[i]} and dfs(i + 1, j + 1)
            return memo[i, j]

        return dfs(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @lru_cache(None)
        def helper(i, j):
            if j == n:
                return i == m
            if p[j] == '*':
                return helper(i, j + 1) or (i < m and helper(i + 1, j))
            return i < m and p[j] in {'?', s[i]} and helper(i + 1, j + 1)

        return helper(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        import functools
        @functools.lru_cache(None)
        def helper(i, j):
            if j == n:
                return i == m
            if p[j] == '*':
                return helper(i, j + 1) or (i < m and helper(i + 1, j))
            return i < m and p[j] in {'?', s[i]} and helper(i + 1, j + 1)

        return helper(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        import functools
        @functools.lru_cache(None)
        def helper(i, j):
            if j == n:
                return i == m
            if p[j] == '*':
                return helper(i, j + 1) or (i < m and helper(i + 1, j))
            return i < m and p[j] in {'?', s[i]} and helper(i + 1, j + 1)

        return helper(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import functools
        @functools.lru_cache(None)
        def helper(i, j):
            if j == n:
                return i == m
            if p[j] == '*':
                return helper(i, j + 1) or (i < m and helper(i + 1, j))
            return i < m and p[j] in {'?', s[i]} and helper(i + 1, j + 1)

        m, n = len(s), len(p)
        return helper(0, 0)


def main():
    sol = Solution()

    s = "aa"
    p = "a"
    res = sol.isMatch(s, p)
    print(res)

    s = "aa"
    p = "*"
    res = sol.isMatch(s, p)
    print(res)

    s = "cb"
    p = "?a"
    res = sol.isMatch(s, p)
    print(res)

    s = "adceb"
    p = "*a*b"
    res = sol.isMatch(s, p)
    print(res)

    s = "acdcb"
    p = "a*c?b"
    res = sol.isMatch(s, p)
    print(res)


if __name__ == '__main__':
    main()
