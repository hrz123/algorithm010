# 面试题 17.13. 恢复空格.py
from typing import List


# dp[i]表示s[:i]的最少未识别字符数
# dp[i] = min(dp[i - k] + (0 if s[i - k:i] in set else k)) for k in 1..i
# 起始条件
# dp[0] = 0

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        words = set(dictionary)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = min(
                [dp[i - k] + (0 if sentence[i - k:i] in words else k)
                 for k in range(1, i + 1)]
            )

        return dp[n]


def main():
    dictionary = ["looked", "just", "like", "her", "brother"]
    sentence = "jesslookedjustliketimherbrother"

    sol = Solution()
    res = sol.respace(dictionary, sentence)
    print(res)


if __name__ == '__main__':
    main()
