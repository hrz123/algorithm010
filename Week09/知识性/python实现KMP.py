# python实现KMP.py


class Solution:
    def KMPSearch(self, p, s):
        m = len(p)
        n = len(s)

        # create lps[] that will hold the longest prefix suffix
        # values for pattern
        lps = self.get_lps(p, m)

        j = 0  # index for p[]
        for i in range(n):
            while j > 0 and s[i] != p[j]:
                j = lps[j - 1] + 1
            if s[i] == p[j]:
                j += 1
            if j == m:
                # print("Found pattern at index " + str(start - j + 1))
                # j = lps[j - 1] + 1
                return i - m + 1
        return -1

    # Python program for KMP Algorithm
    def get_lps(self, p, m):
        lps = [-1] * m
        k = -1
        for i in range(1, m):
            while k != -1 and p[k + 1] != p[i]:
                k = lps[k]
            if p[k + 1] == p[i]:
                k += 1
            lps[i] = k
        return lps


# 以下为自我练习

class Solution:
    def KMPSearch(self, p, s):
        m, n = len(p), len(s)
        lps = self.get_lps(p, m)
        j = 0
        for i in range(n):
            while j > 0 and s[i] != p[j]:
                j = lps[j - 1] + 1
            if s[i] == p[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1

    def get_lps(self, p, m):
        lps = [-1] * m
        k = -1
        for i in range(1, m):
            while k != -1 and p[k + 1] != p[i]:
                k = lps[k]
            if p[k + 1] == p[i]:
                k += 1
            lps[i] = k
        return lps


class Solution:
    def KMPSearch(self, p, s):
        m, n = len(p), len(s)
        lps = self.get_lps(p, m)

        j = 0
        for i in range(n):
            while j > 0 and s[i] != p[j]:
                j = lps[j - 1] + 1
            if s[i] == p[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1

    def get_lps(self, p, m):
        lps = [-1] * m
        k = -1
        for i in range(1, m):
            while k != -1 and p[k + 1] != p[i]:
                k = lps[k]
            if p[k + 1] == p[i]:
                k += 1
            lps[i] = k
        return lps


class Solution:
    def KMPSearch(self, p, s):
        m, n = len(p), len(s)
        lps = self.get_lps(p, m)

        j = 0
        for i in range(n):
            while j != 0 and p[j] != s[i]:
                j = lps[j - 1] + 1
            if p[j] == s[i]:
                j += 1
            if j == m:
                return i - m + 1
        return -1

    def get_lps(self, p, m):
        lps = [-1] * m
        k = -1
        for i in range(1, m):
            while k != -1 and p[k + 1] != p[i]:
                k = lps[k]
            if p[k + 1] == p[i]:
                k += 1
            lps[i] = k
        return lps


class Solution:
    def KMPSearch(self, p, s):
        m, n = len(p), len(s)
        lps = self.get_lps(p, m)
        j = 0
        for i in range(n):
            while j != 0 and s[i] != p[j]:
                j = lps[j - 1] + 1
            if s[i] == p[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1

    def get_lps(self, p, m):
        lps = [-1] * m
        k = -1
        for i in range(1, m):
            while k != -1 and p[k + 1] != p[i]:
                k = lps[k]
            if p[k + 1] == p[i]:
                k += 1
            lps[i] = k
        return lps


class Solution:
    def KMPSearch(self, p, s):
        m, n = len(p), len(s)
        lps = self.get_lps(p, m)
        j = 0
        for i in range(n):
            while j != 0 and s[i] != p[j]:
                j = lps[j - 1] + 1
            if s[i] == p[j]:
                j += 1
            if j == m:
                # return start - m + 1
                print("find at {}".format(i - m + 1))
                j = lps[j - 1] + 1
        # return -1

    def get_lps(self, p, m):
        lps = [-1] * m
        k = -1
        # 注意
        for i in range(1, m):
            while k != -1 and p[i] != p[k + 1]:
                k = lps[k]
            if p[i] == p[k + 1]:
                k += 1
            lps[i] = k
        return lps


class Solution:
    def KMPSearch(self, p, s):
        m, n = len(p), len(s)
        lps = self.get_lps(p, m)
        j = 0
        for i in range(n):
            while j != 0 and s[i] != p[j]:
                j = lps[j - 1] + 1
            if s[i] == p[j]:
                j += 1
            if j == m:
                # return start - m + 1
                print("find at " + str(i - m + 1))
                j = lps[j - 1] + 1
        return -1

    def get_lps(self, p, m):
        lps = [-1] * m
        k = -1
        # 注意
        for i in range(1, m):
            while k != -1 and p[i] == p[k + 1]:
                k = lps[k]
            if p[i] == p[k + 1]:
                k += 1
            lps[i] = k
        return lps


class Solution:
    def KMPSearch(self, p, s):
        # 特判，当p为空字符串的时候
        if not p:
            return 0
        m, n = len(p), len(s)
        lps = self.get_lps(p, m)
        j = 0
        for i in range(n):
            while j != 0 and s[i] != p[j]:
                j = lps[j - 1] + 1
            if s[i] == p[j]:
                j += 1
            if j == m:
                print("find at {}".format(i - m + 1))
                j = lps[j - 1] + 1
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


# 练习
class Solution:
    def KMPSearch(self, p, s):
        # 为了严谨，特判，当p为空字符串的时候
        if not p:
            return 0
        m, n = len(p), len(s)
        lps = self.get_lps(p, m)
        j = 0
        for i in range(n):
            while j != 0 and s[i] != p[j]:
                j = lps[j - 1] + 1
            if s[i] == p[j]:
                j += 1
            if j == m:
                print("find at {}".format(i - m + 1))
                j = lps[j - 1] + 1
        return -1

    def get_lps(self, p, m):
        lps = [-1] * m
        k = -1
        # 注意从1开始
        for i in range(1, m):
            while k != -1 and p[i] != p[k + 1]:
                k = lps[k]
            if p[i] == p[k + 1]:
                k += 1
            lps[i] = k
        return lps


class Solution:
    def KMPSearch(self, p, s):
        m, n = len(p), len(s)
        lps = self.get_lps(p, m)
        j = 0
        for i in range(n):
            while j != 0 and s[i] != p[j]:
                j = lps[j - 1] + 1
            if s[i] == p[j]:
                j += 1
            if j == m:
                print("find at {}".format(i - m + 1))
                j = lps[j - 1] + 1
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


class Solution:
    def KMPSearch(self, p, s):
        m, n = len(p), len(s)
        lps = self.get_lps(p, m)
        j = 0
        for i in range(n):
            while j != 0 and s[i] != p[j]:
                j = lps[j - 1] + 1
            if s[i] == p[j]:
                j += 1
            if j == m:
                # return i - m + 1
                print("find at {}".format(i - m + 1))
                j = lps[j - 1] + 1
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


class Solution:
    def KMPSearch(self, p, s):
        m, n = len(p), len(s)
        lps = self.get_lps(p, m)
        j = 0
        for i in range(n):
            while j != 0 and s[i] != p[j]:
                j = lps[j - 1] + 1
            if s[i] == p[j]:
                j += 1
            if j == m:
                # return i - m + 1
                print("find at {}".format(i - m + 1))
                j = lps[j - 1] + 1
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


class Solution:
    def KMPSearch(self, p, s):
        m, n = len(p), len(s)
        lps = self.get_lps(p, m)
        j = 0
        for i in range(n):
            while j != 0 and s[i] != p[j]:
                j = lps[j - 1] + 1
            if s[i] == p[j]:
                j += 1
            if j == m:
                # return i - m + 1
                print("find at {}".format(i - m + 1))
                j = lps[j - 1] + 1
        return -1

    def get_lps(self, p, m):
        lps = [-1] * m
        k = -1
        for i in range(1, m):
            while k != -1 and p[i] != p[k + 1]:
                k = lps[k]
            if p[k + 1] == p[i]:
                k += 1
            lps[i] = k
        return lps


class Solution:
    def KMPSearch(self, p, s):
        m, n = len(p), len(s)
        lps = self.get_lps(p, m)
        j = 0
        for i in range(n):
            while j != 0 and s[i] != p[j]:
                j = lps[j - 1] + 1
            if s[i] == p[j]:
                j += 1
            if j == m:
                print("find at {}".format(i - m + 1))
                j = lps[j - 1] + 1
                # return i - m + 1
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

    s = "abcruizheuhuruizheaasdasd"
    p = "ruizhe"
    res = sol.KMPSearch(p, s)
    print(res)


if __name__ == '__main__':
    main()
