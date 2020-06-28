# 139. 单词拆分.py
from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]


# 时间复杂度：O(n^2)
# 空间复杂度：O(n)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache(None)
        def back_track(s):
            if not s:
                return True
            res = False
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)


# 时间复杂度：
# 空间复杂度：递归栈的大小

def main():
    sol = Solution()
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    res = sol.wordBreak(s, wordDict)
    print(res)


if __name__ == '__main__':
    main()
