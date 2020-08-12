# 696. 计数二进制子串.py


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        cur, pre = 1, 0
        res = 0
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(cur, pre)
                pre = cur
                cur = 1
        return res + min(cur, pre)


# 以下为自我练习
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        cur, pre = 1, 0
        res = 0
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(cur, pre)
                pre = cur
                cur = 1
        return res + min(cur, pre)


# 以下为自我练习
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        cur, pre = 1, 0
        res = 0
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(cur, pre)
                pre = cur
                cur = 1
        return res + min(pre, cur)


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        pre, cur = 0, 1
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(cur, pre)
                pre = cur
                cur = 1
        return res + min(cur, pre)


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        pre, cur = 0, 1
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(cur, pre)
                pre = cur
                cur = 1
        return res + min(cur, pre)


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        pre, cur = 0, 1
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(pre, cur)
                pre = cur
                cur = 1
        return res + min(cur, pre)


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre, cur = 0, 1
        res = 0
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(cur, pre)
                pre = cur
                cur = 1
        return res + min(cur, pre)


def main():
    sol = Solution()

    s = "00110011"
    res = sol.countBinarySubstrings(s)
    print(res)

    s = "10101"
    res = sol.countBinarySubstrings(s)
    print(res)


if __name__ == '__main__':
    main()
