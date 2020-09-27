# 1.py

class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """

    def kDistance(self, words, target, k):
        res = []
        for word in words:
            if self.__editdistance(word, target, k):
                res.append(word)
        return res

    def __editdistance(self, s, t, k):
        m, n = len(s), len(t)
        # f(i, j) = if s[i] == t[j] f(i, j) = f(i - 1, j - 1)
        # f(i, j) = if s[i] != t[j] f(i, j) = min(f(i - 1, j), f(i, j - 1),
        # f(i - 1, j - 1)) + 1
        # f(0, j) = j
        # f(i, 0) = i
        if m < n:
            m, n = n, m
            s, t = t, s
        if m - n > k:
            return False
        dp = [*range(n + 1)]
        ndp = [0] * (n + 1)
        for i in range(m):
            ndp[0] = i + 1
            for j in range(n):
                if s[i] == t[j]:
                    ndp[j + 1] = dp[j]
                else:
                    ndp[j + 1] = min(dp[j + 1], ndp[j], dp[j]) + 1
            dp, ndp = ndp, dp
        return dp[-1] <= k


def main():
    sol = Solution()
    words = ["abc", "abd", "abcd", "adc"]
    target = "ac"
    k = 1
    res = sol.kDistance(words, target, k)
    print(res)

    words = ["acc", "abcd", "ade", "abbcd"]
    target = "abc"
    k = 2

    res = sol.kDistance(words, target, k)
    print(res)

    words = ["ac" * 1000] * 10
    target = "ac" * 500
    k = 2

    res = sol.kDistance(words, target, k)
    print(res)


if __name__ == '__main__':
    main()
