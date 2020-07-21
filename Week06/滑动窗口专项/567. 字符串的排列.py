# 567. 字符串的排列.py
from collections import defaultdict


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
#         l = r = 0
#         m, n = len(s1), len(s2)
#
#         while r < n:
#             char = s2[r]
#             r += 1
#             if char not in req:
#                 l = r
#                 # 这个地方没有clear
#             else:
#                 req[char] -= 1
#                 while req[char] < 0:
#                     req[s2[l]] += 1
#                     l += 1
#                 if r - l == m:
#                     return True
#         return False


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


if __name__ == '__main__':
    main()
