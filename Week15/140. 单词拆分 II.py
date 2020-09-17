# 140. 单词拆分 II.py


from typing import List
from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        size = len(s)
        word_set = {word for word in wordDict}
        dp = [False for _ in range(size)]
        dp[0] = s[0] in wordDict
        # print(dp)
        for r in range(1, size):
            if s[:r + 1] in word_set:
                dp[r] = True
                continue
            for l in range(r):
                if dp[l] and s[l + 1: r + 1] in word_set:
                    dp[r] = True
                    break
        res = []
        if dp[-1]:
            deq = deque()
            self.dfs(s, size - 1, word_set, res, deq, dp)
        return res

    def dfs(self, s, end, word_set, res, path, dp):
        if s[:end + 1] in word_set:
            path.appendleft(s[:end + 1])
            res.append(' '.join(path))
            path.popleft()
        for i in range(end):
            if dp[i]:
                suffix = s[i + 1:end + 1]
                if suffix in word_set:
                    path.appendleft(suffix)
                    self.dfs(s, i, word_set, res, path, dp)
                    path.popleft()


def main():
    sol = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    res = sol.wordBreak(s, wordDict)
    print(res)


if __name__ == '__main__':
    main()
