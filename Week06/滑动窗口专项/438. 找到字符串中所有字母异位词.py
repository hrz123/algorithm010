# 438. 找到字符串中所有字母异位词.py
from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lookup = defaultdict(int)
        for c in p:
            lookup[c] += 1
        l, r = 0, 0
        counter = defaultdict(int)
        m, n = len(p), len(s)
        res = []
        while r < n:
            tmp = s[r]
            r += 1
            if tmp in lookup:
                counter[tmp] += 1
                while counter[tmp] > lookup[tmp]:
                    counter[s[l]] -= 1
                    l += 1
                if r - l == m:
                    res.append(l)
            else:
                l = r
                counter.clear()
        return res


# 以下为自我练习
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lookup = defaultdict(int)
        for c in p:
            lookup[c] += 1
        l, r = 0, 0
        m, n = len(p), len(s)
        counter = defaultdict(int)
        res = []
        while r < n:
            tmp = s[r]
            r += 1
            if tmp in lookup:
                counter[tmp] += 1
                while counter[tmp] > lookup[tmp]:
                    counter[s[l]] -= 1
                    l += 1
                if r - l == m:
                    res.append(l)
            else:
                l = r
                counter.clear()
        return res


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        req = defaultdict(int)
        for c in p:
            req[c] += 1
        l, r = 0, 0
        n, m = len(s), len(p)
        counter = defaultdict(int)
        while r < n:
            tmp = s[r]
            r += 1
            if tmp in req:
                counter[tmp] += 1
                while counter[tmp] > req[tmp]:
                    counter[s[l]] -= 1
                    l += 1
                if r - l == m:
                    res.append(l)
            else:
                l = r
                counter.clear()
        return res


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        req = defaultdict(int)
        for c in p:
            req[c] += 1
        l, r = 0, 0
        counter = defaultdict(int)
        n, m = len(s), len(p)
        res = []
        while r < n:
            tmp = s[r]
            r += 1
            if tmp in req:
                counter[tmp] += 1
                while counter[tmp] > req[tmp]:
                    counter[s[l]] -= 1
                    l += 1
                if r - l == m:
                    res.append(l)
            else:
                l = r
                counter.clear()
        return res


def main():
    sol = Solution()
    s = "cbaebabacd"
    p = "abc"
    res = sol.findAnagrams(s, p)
    print(res)


if __name__ == '__main__':
    main()
