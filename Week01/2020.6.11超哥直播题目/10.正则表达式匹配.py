# 10.正则表达式匹配.py

from functools import lru_cache


class Solution:
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        # 没有 *

        if not p:
            return not s

        # process first char and "."
        first_match = bool(s and p[0] in {'.', s[0]})

        if len(p) >= 2 and p[1] == "*":
            # process '*: 0个或者多个 prev char
            return self.isMatch(s, p[2:]) or \
                   first_match and self.isMatch(s[1:], p)

        return first_match and self.isMatch(s[1:], p[1:])


class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


def main():
    pass


if __name__ == '__main__':
    main()
