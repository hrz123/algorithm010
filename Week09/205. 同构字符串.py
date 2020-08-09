# 205. 同构字符串.py
from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = defaultdict(str)
        t2s = defaultdict(str)
        for i, c in enumerate(t):
            p = s[i]
            if p not in s2t and c not in t2s:
                s2t[p] = c
                t2s[c] = p
            else:
                if s2t[p] != c or t2s[c] != p:
                    return False
        return True


class Solution:
    def isIsomorphic(self, s, t):
        d1, d2 = [0 for _ in range(256)], [0 for _ in range(256)]
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i + 1
            d2[ord(t[i])] = i + 1
        return True


class Solution:
    def isIsomorphic(self, s, t):
        d1, d2 = [0] * 256, [0] * 256
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i + 1
            d2[ord(t[i])] = i + 1
        return True


def main():
    sol = Solution()

    s = "rgg"
    t = "add"
    res = sol.isIsomorphic(s, t)
    print(res)

    s = "ab"
    t = "aa"
    res = sol.isIsomorphic(s, t)
    print(res)


if __name__ == '__main__':
    main()
