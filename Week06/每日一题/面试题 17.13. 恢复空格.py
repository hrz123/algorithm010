# 面试题 17.13. 恢复空格.py
from functools import lru_cache
from typing import List


# 直接暴力解法


# dp[i]表示s[:i]的最少未识别字符数
# dp[i] = min(dp[i - k] + (0 if s[i - k:i] in set else k)) for k in 1..i
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


def main():
    dictionary = ["looked", "just", "like", "her", "brother"]
    sentence = "jesslookedjustliketimherbrother"

    sol = Solution()
    res = sol.respace(dictionary, sentence)
    print(res)


if __name__ == '__main__':
    main()
