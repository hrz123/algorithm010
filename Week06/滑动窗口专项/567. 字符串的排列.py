# 567. 字符串的排列.py
from collections import defaultdict, Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lookup = defaultdict(int)
        for c in s1:
            lookup[c] += 1
        l = r = 0
        n = len(s2)
        m = len(s1)
        curr = defaultdict(int)
        while r < n:
            char = s2[r]
            r += 1
            if char not in lookup:
                l = r
                curr.clear()
            else:
                curr[char] += 1
                while curr[char] > lookup[char]:
                    curr[s2[l]] -= 1
                    l += 1
                if r - l == m:
                    return True
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        req = defaultdict(int)
        for c in s1:
            req[c] += 1
        l = r = 0
        m, n = len(s1), len(s2)
        curr = defaultdict(int)
        while r < n:
            char = s2[r]
            r += 1
            if char not in req:
                l = r
                curr.clear()
            else:
                curr[char] += 1
                while curr[char] > req[char]:
                    curr[s2[l]] -= 1
                    l += 1
                if r - l == m:
                    return True
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        req = defaultdict(int)
        for c in s1:
            req[c] += 1
        l = r = 0
        m, n = len(s1), len(s2)
        curr = defaultdict(int)
        while r < n:
            char = s2[r]
            r += 1
            if char not in req:
                l = r
                curr.clear()
            else:
                curr[char] += 1
                while curr[char] > req[char]:
                    curr[s2[l]] -= 1
                    l += 1
                if r - l == m:
                    return True
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        req = defaultdict(int)
        for c in s1:
            req[c] += 1
        l = r = 0
        m, n = len(s1), len(s2)
        curr = defaultdict(int)
        while r < n:
            char = s2[r]
            r += 1
            if char not in req:
                l = r
                curr.clear()
            else:
                curr[char] += 1
                while curr[char] > req[char]:
                    curr[s2[l]] -= 1
                    l += 1
                if r - l == m:
                    return True
        return False


# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         req = defaultdict(int)
#         for c in s1:
#             req[c] += 1
#         l = row = 0
#         m, n = len(s1), len(s2)
#
#         while row < n:
#             char = s2[row]
#             row += 1
#             if char not in req:
#                 l = row
#                 # 这个地方没有clear
#             else:
#                 req[char] -= 1
#                 while req[char] < 0:
#                     req[s2[l]] += 1
#                     l += 1
#                 if row - l == m:
#                     return True
#         return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        lookup = defaultdict(int)
        for c in s1:
            lookup[c] += 1
        l = r = 0
        counter = defaultdict(int)
        while r < n:
            ch = s2[r]
            r += 1
            if ch in lookup:
                counter[ch] += 1
                while counter[ch] > lookup[ch]:
                    counter[s2[l]] -= 1
                    l += 1
                if r - l == m:
                    return True
            else:
                l = r
                counter.clear()
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        req = Counter(s1)
        l, r = 0, 0
        m, n = len(s1), len(s2)
        counter = defaultdict(int)
        while r < n:
            tmp = s2[r]
            r += 1
            if tmp in req:
                counter[tmp] += 1
                while counter[tmp] > req[tmp]:
                    counter[s2[l]] -= 1
                    l += 1
                if r - l == m:
                    return True
            else:
                l = r
                counter.clear()
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        req = Counter(s1)
        l, r = 0, 0
        m, n = len(s1), len(s2)
        counter = defaultdict(int)
        while r < n:
            tmp = s2[r]
            r += 1
            if tmp in req:
                counter[tmp] += 1
                while counter[tmp] > req[tmp]:
                    counter[s2[l]] -= 1
                    l += 1
                if r - l == m:
                    return True
            else:
                l = r
                counter.clear()
        return False


def main():
    sol = Solution()

    s1 = "ab"
    s2 = "bao"
    res = sol.checkInclusion(s1, s2)
    print(res)

    s1 = "ky"
    s2 = "kifyk"
    res = sol.checkInclusion(s1, s2)
    print(res)

    s1 = "ab"
    s2 = "eidboaoo"
    res = sol.checkInclusion(s1, s2)
    print(res)

    s1 = "hello"
    s2 = "ooolleoooleh"
    res = sol.checkInclusion(s1, s2)
    print(res)


if __name__ == '__main__':
    main()
