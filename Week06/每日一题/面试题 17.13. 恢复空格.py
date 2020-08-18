# 面试题 17.13. 恢复空格.py
from functools import lru_cache
from typing import List


# 直接暴力解法


# dp[start]表示s[:start]的最少未识别字符数
# dp[start] = min(dp[start - k] + (0 if s[start - k:start] in set else k)) for k in 1..start
# 起始条件
# dp[0] = 0

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        words = set(dictionary)
        max_length = max([len(word) for word in words])
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = min(
                [dp[i - k] for k in range(1, min(i, max_length) + 1) if
                 sentence[i - k:i] in words] + [dp[i - 1] + 1]
            )

        return dp[n]


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = {w for w in dictionary if sentence.find(w) != -1}
        # dictionary = set(dictionary)
        lens = list({len(w) for w in dictionary})
        lens.sort(reverse=True)
        N, res = len(sentence), 0

        @lru_cache(None)
        def sol(i):
            if i >= N:
                return 0
            tails = [sol(i + l) for l in lens
                     if i + l <= N and sentence[i:i + l] in dictionary]
            tails += [1 + sol(i + 1)]
            return min(tails) if tails else 0

        return sol(0)


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        # 首先，将dictionary遍历，求出每一个元素的长度，以为后面的遍历节约开销
        d = {}
        for i in dictionary:
            d[i] = len(i)

        # 创建一个做标记的数组，用dp表示
        len_sentence = len(sentence)
        dp = [0] * (len_sentence + 1)

        for i in range(len_sentence - 1, -1, -1):
            # 首先，将当前元素的标记值在后一个元素的基础上加一，作为未匹配的最坏情况
            dp[i] = dp[i + 1] + 1

            # 遍历字典d
            for j in d:
                # 如果有匹配的值，就更新当前的dp元素
                if sentence[i: i + d[j]] == j:
                    dp[i] = min(dp[i], dp[i + d[j]])

        return dp[0]


# 以下为自我练习
# 定义子问题
# 第i个字符到最后，未识别的字符数是多少, start 0..len(s)
# 定义状态数组
# f(start)
# 递推方程
# f(start) = min(f(start+l))   if s[start:start+l] in dict start+l < N  and l in lens
#      = f(start+1) + 1  else
# 两者取最小值
# 初始化
# f(n) = 0
# 返回值
# f(0)
# 优化空间复杂度
# 没法优化
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        dictionary = set(dictionary)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = min(dp[k] if sentence[k:i] in dictionary else float('inf')
                        for k in range(i))
            dp[i] = min(dp[i], dp[i - 1] + 1)
        return dp[n]


# 1100ms

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        dictionary = {w for w in dictionary if sentence.find(w) != -1}
        if not dictionary:
            return len(sentence)
        _max_len = len(max(dictionary, key=len))
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = min(dp[k] if sentence[k:i] in dictionary else float('inf')
                        for k in range(i - _max_len, i))
            dp[i] = min(dp[i], dp[i - 1] + 1)
        return dp[n]


# 优化
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = {w for w in dictionary if sentence.find(w) != -1}
        if not dictionary:
            return len(sentence)
        n = len(sentence)
        lens = {len(w) for w in dictionary}
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = min([1 + dp[i - 1]] +
                        [dp[i - l] for l in lens
                         if i - l >= 0 and sentence[i - l:i] in dictionary])
        return dp[n]


# 828ms

# 定义子问题
# 第i个字符到最后，未识别的字符数是多少, start 0..len(s)
# 定义状态数组
# f(start)
# 递推方程
# f(start) = min(f(start+l))   if s[start:start+l] in dict start+l < N  and l in lens
#      = f(start+1) + 1  else
# 两者取最小值
# 初始化
# f(n) = 0
# 返回值
# f(0)
# 优化空间复杂度
# 没法优化
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = {w for w in dictionary if sentence.find(w) != -1}
        if not dictionary:
            return len(sentence)
        n = len(sentence)
        lens = {len(w) for w in dictionary}
        memo = {}

        def dfs(i):
            if i == n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min([1 + dfs(i + 1)] +
                          [dfs(i + l) for l in lens
                           if i + l <= n and sentence[i:i + l] in dictionary])

            return memo[i]

        return dfs(0)


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = {w for w in dictionary if sentence.find(w) != -1}
        if not dictionary:
            return len(sentence)
        n = len(sentence)
        lens = {len(w) for w in dictionary}
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = min([dp[i + l] for l in lens if i + l <= n
                         and sentence[i:i + l] in dictionary] + [1 + dp[i + 1]])
        return dp[0]


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = {w for w in dictionary if sentence.find(w) != -1}
        if not dictionary:
            return len(sentence)
        n = len(sentence)
        dp = [0] * (n + 1)
        lens = {len(w) for w in dictionary}
        for i in range(1, n + 1):
            dp[i] = min([1 + dp[i - 1]] +
                        [dp[i - l] for l in lens
                         if i - l >= 0 and sentence[i - l:i] in dictionary])
        return dp[n]


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = {w for w in dictionary if sentence.find(w) != -1}
        if not dictionary:
            return len(sentence)
        n = len(sentence)
        lens = {len(w) for w in dictionary}
        memo = {}

        def dfs(i):
            if i == 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min([1 + dfs(i - 1)] +
                          [dfs(i - l) for l in lens
                           if i - l >= 0 and sentence[i - l:i] in dictionary])
            return memo[i]

        return dfs(n)


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = {w for w in dictionary if sentence.find(w) != -1}
        if not dictionary:
            return len(sentence)
        sizes = {len(w) for w in dictionary}
        n = len(sentence)
        memo = {}

        def dfs(i):
            if i == 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min([1 + dfs(i - 1)] +
                          [dfs(i - l) for l in sizes
                           if i - l >= 0 and sentence[i - l:i] in dictionary])
            return memo[i]

        return dfs(n)


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = {w for w in dictionary if sentence.find(w) != -1}
        if not dictionary:
            return len(sentence)
        n = len(sentence)
        memo = {}
        sizes = {len(w) for w in dictionary}

        def dfs(i):
            if i == 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min([1 + dfs(i - 1)] +
                          [dfs(i - l) for l in sizes if i - l >= 0
                           and sentence[i - l:i] in dictionary])
            return memo[i]

        return dfs(n)


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        dictionary = {d for d in dictionary if sentence.find(d) != -1}
        lens = {len(d) for d in dictionary}
        import functools
        @functools.lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            res = dp(i + 1) + 1
            for l in lens:
                if i + l <= n and sentence[i:i + l] in dictionary:
                    res = min(res, dp(i + l))
            return res

        return dp(0)


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        d = {w for w in dictionary if sentence.find(w) != -1}
        lens = {len(w) for w in d}
        n = len(sentence)
        import functools
        @functools.lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            res = dp(i + 1) + 1
            for l in lens:
                if i + l <= n and sentence[i:i + l] in d:
                    res = min(res, dp(i + l))
            return res

        return dp(0)


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        d = {}.fromkeys(dictionary)
        n = len(sentence)
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] + 1
            for j in range(i):
                if sentence[j:i] in d:
                    f[i] = min(f[i], f[j])
        return f[-1]


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        dp = [0] * (n + 1)
        dic = {w for w in dictionary if sentence.find(w) != -1}
        lens = {len(w) for w in dic}
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for l in lens:
                if sentence[i - l:i] in dic:
                    dp[i] = min(dp[i], dp[i - l])
        return dp[n]


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        dp = [0] * (n + 1)
        dic = {w for w in dictionary if sentence.find(w) != -1}
        lens = {len(w) for w in dic}
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for l in lens:
                if i - l >= 0 and sentence[i - l:i] in dic:
                    dp[i] = min(dp[i], dp[i - l])
        return dp[n]


def main():
    dictionary = ["looked", "just", "like", "her", "brother"]
    sentence = "jesslookedjustliketimherbrother"

    sol = Solution()
    res = sol.respace(dictionary, sentence)
    print(res)


if __name__ == '__main__':
    main()
