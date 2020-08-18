# 76. 最小覆盖子串.py
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        min_len = n + 1
        res = ''

        bool_array = [False] * len(t)

        def dfs(i, bool_array):
            if all(bool_array):
                return i

            while i < n and s[i] not in t:
                i += 1

            if i == n:
                return None

            idx = t.find(s[i])
            while idx != -1 and bool_array[idx]:
                idx = t.find(s[i], idx + 1)
            if idx != -1:
                bool_array[idx] = True
            end = dfs(i + 1, bool_array)
            if end is not None:
                return end
            bool_array[idx] = False

        for i in range(n):
            if s[i] in t:
                ba = bool_array.copy()
                idx = dfs(i, ba)
                if idx is not None:
                    cur_len = idx - i
                    if cur_len < min_len:
                        min_len = cur_len
                        res = s[i:idx]

        return res


# 我们只要保证窗口(队列)字符串的个数含有t中字符的个数大于等于t里相应元素个数，如方法一
# 还有一种方法记录队列元素和t中元素的差值。
class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        t = Counter(t)
        lookup = Counter()
        start = 0
        end = 0
        min_len = float("inf")
        res = ""
        while end < len(s):
            lookup[s[end]] += 1
            end += 1
            while all(map(lambda x: lookup[x] >= t[x], t.keys())):
                if end - start < min_len:
                    res = s[start:end]
                    min_len = end - start
                lookup[s[start]] -= 1
                start += 1
        return res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)
        lookup = Counter()
        start = 0
        end = 0
        min_len = float("inf")
        res = ""
        while end < len(s):
            lookup[s[end]] += 1
            end += 1
            while all(map(lambda x: lookup[x] >= t[x], t.keys())):
                # 这个操作比较耗时
                if end - start < min_len:
                    min_len = end - start
                    res = s[start:end]
                lookup[s[start]] -= 1
                start += 1
        return res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1

        start = 0
        end = 0
        min_len = float('inf')
        res = ''
        counter = len(t)

        n = len(s)
        while end < n:
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1

        start = 0
        end = 0
        min_len = float('inf')
        res = ""
        counter = len(t)
        n = len(s)

        while end < n:
            # 只要结尾在查找表中
            if lookup[s[end]] > 0:
                # 计数器就减一
                counter -= 1
            # 在lookup中减一
            lookup[s[end]] -= 1
            # end挪到下一位
            end += 1
            # 如果计数器为0
            while not counter:
                if end - start < min_len:
                    min_len = end - start
                    res = s[start:end]
                # 一旦遇到t中的数了，非t中的数都减了一，不可能回到正数
                if lookup[s[start]] == 0:
                    # 计数器就加一，也就跳出了循环
                    counter += 1
                # 否则减掉的数加一
                lookup[s[start]] += 1
                # start向右移一位
                start += 1
        return res


# 以下为自我练习
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float('inf')
        res = ""
        n = len(s)
        counter = len(t)

        while end < n:
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if end - start < min_len:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = defaultdict(int)
        start = 0
        end = 0
        n = len(s)
        counter = len(t)
        min_len = float('inf')
        res = ""
        for c in t:
            lookup[c] += 1

        while end < n:
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if end - start < min_len:
                    min_len = end - start
                    res = s[start: end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = end = 0
        counter = len(t)
        min_len = float('inf')
        res = ''

        while end < len(s):
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if end - start < min_len:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1

        return res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = end = 0
        counter = len(t)
        min_len = float('inf')
        res = ''
        n = len(s)
        while end < n:
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if end - start < min_len:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        req = defaultdict(int)
        for c in t:
            req[c] += 1
        l = r = 0
        n = len(s)
        min_len = n + 1
        res = ""
        counter = len(t)
        while r < n:
            if req[s[r]] > 0:
                counter -= 1
            req[s[r]] -= 1
            r += 1
            while counter == 0:
                if r - l < min_len:
                    min_len = r - l
                    res = s[l:r]
                if req[s[l]] == 0:
                    counter += 1
                req[s[l]] += 1
                l += 1
        return res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        l = r = 0
        n = len(s)
        min_len = n + 1
        res = ""
        counter = len(t)
        while r < n:
            if lookup[s[r]] > 0:
                counter -= 1
            lookup[s[r]] -= 1
            r += 1
            while counter == 0:
                if r - l < min_len:
                    min_len = r - l
                    res = s[l:r]
                if lookup[s[l]] == 0:
                    counter += 1
                lookup[s[l]] += 1
                l += 1
        return res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        _min_len = m + 1
        res = ""
        l = r = 0
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        while r < m:
            if lookup[s[r]] > 0:
                n -= 1
            lookup[s[r]] -= 1
            r += 1
            while n == 0:
                if r - l < _min_len:
                    _min_len = r - l
                    res = s[l:r]
                if lookup[s[l]] == 0:
                    n += 1
                lookup[s[l]] += 1
                l += 1
        return res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        m, n = len(t), len(s)
        l = r = 0
        target = m
        res = ""
        _min_len = n + 1
        while r < n:
            tmp = s[r]
            r += 1
            if lookup[tmp] > 0:
                target -= 1
            lookup[tmp] -= 1
            while target == 0:
                if r - l < _min_len:
                    _min_len = r - l
                    res = s[l:r]
                if lookup[s[l]] == 0:
                    target += 1
                lookup[s[l]] += 1
                l += 1
        return res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        l, r = 0, 0
        req = defaultdict(int)
        for c in t:
            req[c] += 1
        target = n
        _min_length = float('inf')
        res_left = None
        while r < m:
            tmp = s[r]
            r += 1
            if req[tmp] > 0:
                target -= 1
            req[tmp] -= 1
            while target == 0:
                if r - l < _min_length:
                    _min_length = r - l
                    res_left = l
                if req[s[l]] == 0:
                    target += 1
                req[s[l]] += 1
                l += 1
        return "" if _min_length == float('inf') else s[res_left:res_left +
                                                                 _min_length]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        counter = Counter(t)
        res_left = 0
        res = m + 1
        l, r = 0, 0
        while r < m:
            tmp = s[r]
            r += 1
            if counter[tmp] > 0:
                n -= 1
            counter[tmp] -= 1
            while n == 0:
                if r - l < res:
                    res = r - l
                    res_left = l
                if counter[s[l]] == 0:
                    n += 1
                counter[s[l]] += 1
                l += 1
        return '' if res == m + 1 else s[res_left:res_left + res]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        l, r = 0, 0
        req = defaultdict(int)
        res = m + 1
        left = 0
        for c in t:
            req[c] += 1
        while r < m:
            tmp = s[r]
            r += 1
            if req[tmp] > 0:
                n -= 1
            req[tmp] -= 1
            while n == 0:
                if r - l < res:
                    res = r - l
                    left = l
                if req[s[l]] == 0:
                    n += 1
                req[s[l]] += 1
                l += 1
        return '' if res == m + 1 else s[left:left + res]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        req = defaultdict(int)
        for c in t:
            req[c] += 1
        l, r = 0, 0
        res = m + 1
        left = 0
        while r < m:
            tmp = s[r]
            r += 1
            if req[tmp] > 0:
                n -= 1
            req[tmp] -= 1
            while n == 0:
                if r - l < res:
                    res = r - l
                    left = l
                if req[s[l]] == 0:
                    n += 1
                req[s[l]] += 1
                l += 1
        return '' if res == m + 1 else s[left:left + res]


def main():
    sol = Solution()

    S = "ADOBECODEBANC"
    T = "ABC"
    res = sol.minWindow(S, T)
    print(res)

    S = "ADOBECODEBANC"
    T = "ABCC"
    res = sol.minWindow(S, T)
    print(res)


if __name__ == '__main__':
    main()
