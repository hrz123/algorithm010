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
