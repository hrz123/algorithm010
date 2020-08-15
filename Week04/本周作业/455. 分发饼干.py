# 455. 分发饼干.py
from typing import List


# 第一遍做法
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(s)
        start = 0
        res = 0
        for need in g:
            for i in range(start, n):
                if s[i] >= need:
                    res += 1
                    start = i + 1
                    break
            if start == n:
                break
        return res


# 第二遍改进
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        childi = 0
        cookiei = 0

        while cookiei < len(s) and childi < len(g):
            if s[cookiei] >= g[childi]:
                childi += 1
            cookiei += 1

        return childi


# 时间复杂度：主要在排序上

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        cookie = 0
        child = 0

        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        m, n = len(g), len(s)
        while i < n and j < m:
            if g[j] <= s[i]:
                j += 1
            i += 1
        return j


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        m, n = len(g), len(s)
        i, j = 0, 0
        while i < m and j < n:
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i


def main():
    sol = Solution()

    g = [1, 2, 3]
    s = [1, 2, 3]
    res = sol.findContentChildren(g, s)
    print(res)

    g = [1, 2]
    s = [1, 2, 3]
    res = sol.findContentChildren(g, s)
    print(res)


if __name__ == '__main__':
    main()
