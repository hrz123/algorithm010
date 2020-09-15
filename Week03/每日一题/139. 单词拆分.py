# 139. 单词拆分.py
from collections import deque
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


# 时间复杂度：O(m^2)
# 空间复杂度：O(m)


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


# 以下为自我练习
# 定义一个子函数
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(start):
            if start == n:
                return True
            if start in memo:
                return memo[start]
            for end in range(start + 1, n + 1):
                if s[start:end] in words and dfs(end):
                    memo[start] = True
                    return memo[start]
            memo[start] = False
            return memo[start]

        return dfs(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(start):
            if start == n:
                return True
            if start in memo:
                return memo[start]
            for i in range(start + 1, n + 1):
                if s[start: i] in words and dfs(i):
                    memo[start] = True
                    return True
            memo[start] = False
            return False

        return dfs(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = {w for w in wordDict if s.find(w) != -1}
        lens = {len(w) for w in words}
        n = len(s)

        import functools
        @functools.lru_cache(None)
        def backtrace(i):
            if i == n:
                return True
            for l in lens:
                if s[i:i + l] in words:
                    if backtrace(i + l):
                        return True
            return False

        return backtrace(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        lens = {len(w) for w in words}
        lens = sorted(list(lens), reverse=True)
        n = len(s)
        d = set()
        deq = deque([0])
        while deq:
            i = deq.popleft()
            if i >= n:
                return True
            if i in d:
                continue
            d.add(i)
            for l in lens:
                if s[i:i + l] in words:
                    deq.append(i + l)
        return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        lens = {len(w) for w in words}
        lens = sorted(list(lens), reverse=True)
        deq = deque([0])
        d = set()
        while deq:
            i = deq.pop()
            if i >= n:
                return True
            if i in d:
                continue
            d.add(i)
            for l in lens:
                if s[i:i + l] in words:
                    deq.append(i + l)
        return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        lens = {len(w) for w in words}
        lens = sorted(list(lens), reverse=True)
        n = len(s)
        d = [False] * n

        def dfs(i):
            if i >= n:
                return True
            if d[i]:
                return False
            d[i] = True
            for l in lens:
                if s[i:i + l] in words:
                    if dfs(i + l):
                        return True
            return False

        return dfs(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def dfs(i):
            if i == n:
                return True
            for l in lens:
                if i + l <= n and s[i:i + l] in words:
                    if dfs(i + l):
                        return True
            return False

        words = {w for w in wordDict if s.find(w) != -1}
        lens = {len(w) for w in words}
        n = len(s)
        return dfs(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def dfs(i):
            if i == n:
                return True
            for l in lens:
                if i + l <= n and s[i:i + l] in words:
                    if dfs(i + l):
                        return True
            return False

        n = len(s)
        words = {w for w in wordDict if s.find(w) != -1}
        lens = {len(w) for w in words}
        return dfs(0)


def main():
    sol = Solution()
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    res = sol.wordBreak(s, wordDict)
    print(res)

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    res = sol.wordBreak(s, wordDict)
    print(res)

    s = "aaaaaaa"
    wordDict = ["aaaa", "aaa"]
    res = sol.wordBreak(s, wordDict)
    print(res)


if __name__ == '__main__':
    main()
