# 30. 串联所有单词的子串.py
from collections import defaultdict
from typing import List


# 思路1：
# 一个len(words)*len(words[0])的窗口，滑动，判断里面的字符是否符合要求
# 滑动O(m)
# 判断：O(n),m为words个数
# 总时间复杂度O(m*n)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        nw = len(words)
        wl = len(words[0])
        length = nw * wl
        counter = defaultdict(int)
        for w in words:
            counter[w] += 1
        end = length
        size = len(s)
        res = []
        while end <= size:
            counter_copy = counter.copy()
            for e in range(end, end - length, -wl):
                if s[e - wl:e] not in counter_copy \
                        or counter_copy[s[e - wl:e]] == 0:
                    break
                else:
                    counter_copy[s[e - wl:e]] -= 1
            else:
                res.append(end - length)
            end += 1
        return res


# 思路2：
# 也是一个len(words)*len(words[0])的窗口，滑动
# 复杂度O(m)
# 这个时候从0-k-1为起点分别开始，k为len(words[0])，一个单词的长度
# 时间复杂度为O(m*k),k为一个单词的长度
# 大多数情况单词的长度比单词的个数小，所以方法二更快
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        size = len(s)
        wl = len(words[0])
        nw = len(words)
        lookup = defaultdict(int)
        for w in words:
            lookup[w] += 1
        length = wl * nw
        res = []
        for start in range(wl):
            counter = 0
            lookup_copy = lookup.copy()
            for end in range(start + wl, start + length + wl, wl):
                if lookup_copy[s[end - wl:end]] <= 0:
                    counter += 1
                lookup_copy[s[end - wl:end]] -= 1
            if counter == 0:
                res.append(start)
            for end in range(start + length + wl, size + 1, wl):
                if lookup_copy[s[end - wl:end]] <= 0:
                    counter += 1
                lookup_copy[s[end - wl:end]] -= 1
                lookup_copy[s[end - length - wl:end - length]] += 1
                if lookup_copy[s[end - length - wl:end - length]] <= 0:
                    counter -= 1
                if counter == 0:
                    res.append(end - length)
        return res


# 国际站解法
class Solution:
    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        curr = {}
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = len(words) * k
        req = {}
        for w in words:
            req[w] = req[w] + 1 if w in req else 1
        ans = []
        for i in range(min(k, n - t + 1)):
            self._findSubstring(i, i, n, k, t, s, req, ans)
        return ans


class Solution:
    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        curr = defaultdict(int)
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] += 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = len(words) * k
        lookup = defaultdict(int)
        for w in words:
            lookup[w] += 1
        ans = []
        for i in range(min(k, n - t + 1)):
            self._findSubstring(i, i, n, k, t, s, lookup, ans)
        return ans


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = k * len(words)
        lookup = defaultdict(int)
        for w in words:
            lookup[w] += 1
        ans = []
        for i in range(min(k, n - t + 1)):
            self._findSubstring(i, i, n, k, t, s, lookup, ans)
        return ans

    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        curr = defaultdict(int)
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] += 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)


# 要求无重复的时候最好新建一个curr的查找表，否则要一个一个清除，不如直接clear这个查找表
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []

        req = defaultdict(int)
        for w in words:
            req[w] += 1

        n = len(s)
        k = len(words[0])
        t = len(words) * k
        ans = []
        for i in range(min(k, n - t + 1)):
            self._findSubstring(i, i, n, k, t, s, req, ans)
        return ans

    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        curr = defaultdict(int)
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] += 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        lookup = defaultdict(int)
        for w in words:
            lookup[w] += 1
        n = len(s)
        k = len(words[0])
        t = k * len(words)
        ans = []
        for i in range(min(k, n - t + 1)):
            self._findSubstring(i, i, n, k, t, s, lookup, ans)
        return ans

    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        curr = defaultdict(int)
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] += 1
                while curr[w] > req[w]:
                    curr[s[l: l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        m, n = len(s), len(words[0])
        t = n * len(words)
        req = defaultdict(int)
        for w in words:
            req[w] += 1
        res = []
        for start in range(min(n, m - n + 1)):
            self.find(start, s, req, n, m, t, res)
        return res

    def find(self, start, s, req, n, m, t, res):
        l = r = start
        counter = defaultdict(int)
        while r < m:
            word = s[r:r + n]
            r += n
            if word in req:
                counter[word] += 1
                while counter[word] > req[word]:
                    counter[s[l:l + n]] -= 1
                    l += n
                if r - l == t:
                    res.append(l)
            else:
                l = r
                counter.clear()


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        res = []
        n = len(words[0])
        t = n * len(words)
        m = len(s)
        req = defaultdict(int)
        for w in words:
            req[w] += 1
        for start in range(min(n, m - n + 1)):
            self.find(s, start, req, n, t, m, res)
        return res

    def find(self, s, start, req, n, t, m, res):
        counter = defaultdict(int)
        l = r = start
        while r < m:
            tmp = s[r:r + n]
            r += n
            if tmp in req:
                counter[tmp] += 1
                while counter[tmp] > req[tmp]:
                    counter[s[l:l + n]] -= 1
                    l += n
                if r - l == t:
                    res.append(l)
            else:
                l = r
                counter.clear()


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        n = len(words[0])
        t = n * len(words)
        m = len(s)
        res = []
        req = defaultdict(int)
        for w in words:
            req[w] += 1
        for i in range(min(n, m - n + 1)):
            self._find(i, s, req, n, t, m, res)
        return res

    def _find(self, i, s, req, n, t, m, res):
        counter = defaultdict(int)
        l, r = i, i
        while r < m:
            tmp = s[r:r + n]
            r += n
            if tmp in req:
                counter[tmp] += 1
                while counter[tmp] > req[tmp]:
                    counter[s[l:l + n]] -= 1
                    l += n
                if r - l == t:
                    res.append(l)
            else:
                l = r
                counter.clear()


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        n = len(words[0])
        t = len(words) * n
        m = len(s)
        res = []
        req = defaultdict(int)
        for w in words:
            req[w] += 1
        for i in range(min(n, m - n + 1)):
            self.find(i, req, res, s, n, t, m)
        return res

    def find(self, i, req, res, s, n, t, m):
        l, r = i, i
        counter = defaultdict(int)
        while r < m:
            tmp = s[r:r + n]
            r += n
            if tmp in req:
                counter[tmp] += 1
                while counter[tmp] > req[tmp]:
                    counter[s[l:l + n]] -= 1
                    l += n
                if r - l == t:
                    res.append(l)
            else:
                l = r
                counter.clear()


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        n = len(words[0])
        t = len(words) * n
        m = len(s)
        req = defaultdict(int)
        for w in words:
            req[w] += 1
        res = []
        for i in range(min(n, m - t + 1)):
            self.find(i, s, req, n, t, m, res)
        return res

    def find(self, i, s, req, n, t, m, res):
        l, r = i, i
        counter = defaultdict(int)
        while r < m:
            tmp = s[r:r + n]
            r += n
            if tmp in req:
                counter[tmp] += 1
                while counter[tmp] > req[tmp]:
                    counter[s[l:l + n]] -= 1
                    l += n
                if r - l == t:
                    res.append(l)
            else:
                l = r
                counter.clear()


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        n = len(words[0])
        t = n * len(words)
        m = len(s)
        req = defaultdict(int)
        for w in words:
            req[w] += 1
        res = []
        for i in range(min(n, m - t + 1)):
            self.find(i, req, s, n, t, m, res)
        return res

    def find(self, i, req, s, n, t, m, res):
        counter = defaultdict(int)
        l, r = i, i
        while r < m:
            tmp = s[r:r + n]
            r += n
            if tmp in req:
                counter[tmp] += 1
                while counter[tmp] > req[tmp]:
                    counter[s[l:l + n]] -= 1
                    l += n
                if r - l == t:
                    res.append(l)
            else:
                l = r
                counter.clear()


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        n = len(words[0])
        t = len(words) * n
        m = len(s)
        req = defaultdict(int)
        for w in words:
            req[w] += 1
        res = []
        for i in range(min(n, m - t + 1)):
            self.find(i, s, req, n, m, t, res)
        return res

    def find(self, i, s, req, n, m, t, res):
        l, r = i, i
        counter = defaultdict(int)
        while r < m:
            tmp = s[r: r + n]
            r += n
            if tmp in req:
                counter[tmp] += 1
                while counter[tmp] > req[tmp]:
                    counter[s[l:l + n]] -= 1
                    l += n
                if r - l == t:
                    res.append(l)
            else:
                l = r
                counter.clear()


def main():
    sol = Solution()

    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    res = sol.findSubstring(s, words)
    print(res)

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    res = sol.findSubstring(s, words)
    print(res)

    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    res = sol.findSubstring(s, words)
    print(res)

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    res = sol.findSubstring(s, words)
    print(res)

    s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words = ["fooo", "barr", "wing", "ding", "wing"]
    res = sol.findSubstring(s, words)
    print(res)

    s = "aaaaaaaa"
    words = ["aa", "aa", "aa"]
    res = sol.findSubstring(s, words)
    print(res)


if __name__ == '__main__':
    main()
