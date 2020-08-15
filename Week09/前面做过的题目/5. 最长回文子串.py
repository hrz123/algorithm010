# 5. 最长回文子串.py


# 暴力解法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)

        if size < 2:
            return s
        max_len = 1
        res = s[0]

        for i in range(size - 1):
            for j in range(i + 1, size):
                if j - i + 1 > max_len and self.__isvalid(s, i, j):
                    max_len = j - i + 1
                    res = s[i: j + 1]

        return res

    def __isvalid(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


# 定义子问题: start, j之间的字符串是不是回文字符串
# 定义状态数组 f(start, j)
# 递推方程
# f(start, j) = f(start+1, j-1) + 2 if (s[start] == s[j])
# 动态规划事实上是在填一张二维表格，由构成子串。因此i和j的关系是
# start <= j, 因此只需要填这张表格对角线以上的部分。
# 边界条件是 j-1-(start+1) +1 < 2, j-start < 3
# 初始化，单个字符一定是回文串
# dp[start][start] = true
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 0
        res = (0, 0)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for k in range(1, n):
            for i in range(n - k):
                j = i + k
                if dp[i + 1][j - 1] == float('-inf'):
                    dp[i][j] = float('-inf')
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        res = (i, j)
                # 否则不可能再为回文串
                else:
                    dp[i][j] = float('-inf')

        return s[res[0]:res[1] + 1]


# 传说中的马拉车算法，不掌握，只作为爱好
class Solution:
    # Manacher algorithm
    def longestPalindrome(self, s: str) -> str:
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking.
        T = '#'.join("^{}$".format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        maxLen = centerIndex = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])
            # Attempt to expand palindrome centered at start.
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            # If palindrome centered at start expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
            if P[i] > maxLen:
                maxLen = P[i]
                centerIndex = i
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]


# 以下为自我练习
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        dp = [[0] * n for _ in range(n)]
        max_len = 1
        res = s[0]
        for i in range(n):
            dp[i][i] = 1
        for j in range(0, n):
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        res = s[i:j + 1]
                else:
                    dp[i][j] = float('-inf')
        return res


# 递推公式
# dp(start, j) = dp(start+1, j-1) + 2
# dp(start, start) = 1
# dp(start, start-1) = 0
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = 1
        res = s[0]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        res = s[i:j + 1]
                else:
                    dp[i][j] = float('-inf')

        return res


# 递推公式dp(start, j) = dp(start + 1, j-1)+2
# dp(start, start) = 1 start 0..n-1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = 1
        res = s[0]

        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        res = s[i:j + 1]
                else:
                    dp[i][j] = float('-inf')
        return res


# 从中间向两边扩散
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        _max_len = 1
        res = s[0]
        for i in range(2 * n - 1):
            idx = i >> 1
            if i & 1:
                _len = 0
                l, r = idx, idx + 1
                while l >= 0 and r < n and s[l] == s[r]:
                    _len += 2
                    if _len > _max_len:
                        _max_len = _len
                        res = s[l:r + 1]
                    l -= 1
                    r += 1
            else:
                _len = 1
                l, r = idx - 1, idx + 1
                while l >= 0 and r < n and s[l] == s[r]:
                    _len += 2
                    if _len > _max_len:
                        _max_len = _len
                        res = s[l:r + 1]
                    l -= 1
                    r += 1
        return res


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        _max_len = 1
        res = s[0]
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if dp[i][j] > _max_len:
                        _max_len = dp[i][j]
                        res = s[i:j + 1]
                else:
                    dp[i][j] = float('-inf')
        return res


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        n = len(s)
        _max_len = 1
        _max_l = 0

        for i in range((n << 1) - 1):
            idx = i >> 1
            if i & 1:
                _len = 0
                l, r = idx, idx + 1
                while l >= 0 and r < n and s[l] == s[r]:
                    _len += 2
                    l -= 1
                    r += 1
                if _len > _max_len:
                    _max_len = _len
                    _max_l = l + 1
            else:
                _len = 1
                l, r = idx - 1, idx + 1
                while l >= 0 and r < n and s[l] == s[r]:
                    _len += 2
                    l -= 1
                    r += 1
                if _len > _max_len:
                    _max_len = _len
                    _max_l = l + 1
        return s[_max_l:_max_l + _max_len]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        _max_len = res_left = 0
        for i in range((n << 1) - 1):
            idx = i >> 1
            if i & 1:
                l, r = idx, idx + 1
                while l >= 0 and r < n and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - l - 1 > _max_len:
                    _max_len = r - l - 1
                    res_left = l + 1
            else:
                l, r = idx - 1, idx + 1
                while l >= 0 and r < n and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - l - 1 > _max_len:
                    _max_len = r - l - 1
                    res_left = l + 1
        return s[res_left:res_left + _max_len]


# i，j是否是回文子串
# f(i, j)
# f(i, j) = f(i+1, j-1) and s[i] == s[j]
# f(i, j) = f(i+1, j-1) + 2 if s[i] == s[j]
#         = float('-inf')
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        _max_len, res_left = 1, 0
        dp = [[False] * n for _ in range(n)]
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                dp[i][j] = s[i] == s[j] and (dp[i + 1][j - 1] or j - i <= 2)
                if dp[i][j]:
                    if j - i + 1 > _max_len:
                        _max_len = j - i + 1
                        res_left = i
        return s[res_left:res_left + _max_len]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        n = len(s)
        _max_len = 1
        left = 0
        for i in range(n * 2 - 1):
            idx = i >> 1
            l = idx if i & 1 else idx - 1
            r = idx + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > _max_len:
                _max_len = r - l - 1
                left = l + 1
        return s[left:left + _max_len]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        size = 0
        res_left = 0
        for i in range((n << 1) - 1):
            idx = i >> 1
            if i & 1:
                l, r = idx, idx + 1
            else:
                l, r = idx - 1, idx + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > size:
                size = r - l - 1
                res_left = l + 1
        return s[res_left:res_left + size]


def main():
    sol = Solution()

    s = "abcda"
    res = sol.longestPalindrome(s)
    print(res)
    assert res == "a"

    s = "babad"
    res = sol.longestPalindrome(s)
    print(res)
    assert res == "bab" or res == "aba"

    s = "abbd"
    res = sol.longestPalindrome(s)
    print(res)
    assert res == "bb"

    s = ""
    res = sol.longestPalindrome(s)
    print(res)
    assert res == ""


if __name__ == '__main__':
    main()
