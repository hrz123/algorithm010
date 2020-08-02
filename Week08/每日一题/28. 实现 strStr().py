# 28. 实现 strStr().py


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        m, n = len(needle), len(haystack)
        lps = self.get_lps(needle, m)
        j = 0
        for i in range(n):
            while j != 0 and haystack[i] != needle[j]:
                j = lps[j - 1] + 1
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1

    def get_lps(self, p, m):
        lps = [-1] * m
        k = -1
        for i in range(1, m):
            while k != -1 and p[i] != p[k + 1]:
                k = lps[k]
            if p[i] == p[k + 1]:
                k += 1
            lps[i] = k
        return lps


def main():
    sol = Solution()

    haystack = "hello"
    needle = "ll"
    res = sol.strStr(haystack, needle)
    print(res)

    haystack = "hello"
    needle = ""
    res = sol.strStr(haystack, needle)
    print(res)


if __name__ == '__main__':
    main()
