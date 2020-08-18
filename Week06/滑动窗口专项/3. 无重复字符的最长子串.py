# 3. 无重复字符的最长子串.py
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        n = len(s)
        counter = 0
        while end < n:
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1

            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = defaultdict(int)
        start = 0
        end = 0
        n = len(s)
        res = 0
        while end < n:
            lookup[s[end]] += 1

            if lookup[s[end]] == 1:
                if end - start + 1 > res:
                    res = end - start + 1
            else:
                while lookup[s[end]] == 2:
                    lookup[s[start]] -= 1
                    start += 1
            end += 1
        return res


# 以下为自我练习
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = defaultdict(int)
        start = 0
        end = 0
        n = len(s)
        counter = 0
        max_len = 0
        while end < n:
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter == 1:
                if lookup[s[start]] == 2:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = defaultdict(int)
        start = end = 0
        counter = 0
        max_len = 0
        while end < len(s):
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter == 1:
                if lookup[s[start]] == 2:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = defaultdict(int)
        start = end = 0
        counter = 0
        max_len = 0
        n = len(s)
        while end < n:
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter == 1:
                if lookup[s[start]] == 2:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = defaultdict(int)
        l = r = 0
        flag = False
        max_len = 0
        n = len(s)
        while r < n:
            if lookup[s[r]] > 0:
                flag = True
            lookup[s[r]] += 1
            r += 1

            while flag:
                if lookup[s[l]] == 2:
                    flag = False
                lookup[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l)
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = defaultdict(int)
        l = r = 0
        n = len(s)
        flag = False
        max_len = 0
        while r < n:
            if lookup[s[r]] > 0:
                flag = True
            lookup[s[r]] += 1
            r += 1
            while flag:
                if lookup[s[l]] == 2:
                    flag = False
                lookup[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l)
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        counter = defaultdict(int)
        while r < len(s):
            ch = s[r]
            counter[s[r]] += 1
            r += 1
            while counter[ch] > 1:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l)
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = len(s)
        l, r = 0, 0
        counter = defaultdict(int)
        res = 0
        while r < m:
            tmp = s[r]
            r += 1
            counter[tmp] += 1
            while counter[tmp] > 1:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l)
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        counter = {}
        n = len(s)
        res = 0
        while r < n:
            tmp = s[r]
            counter[tmp] = counter.get(tmp, 0) + 1
            r += 1
            while counter[tmp] > 1:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l)
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        counter = defaultdict(int)
        n = len(s)
        res = 0
        while r < n:
            tmp = s[r]
            r += 1
            counter[tmp] += 1
            while counter[tmp] > 1:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l)
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        n = len(s)
        counter = defaultdict(int)
        res = 0
        while r < n:
            tmp = s[r]
            r += 1
            counter[tmp] += 1
            while counter[tmp] > 1:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l)
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        n = len(s)
        counter = defaultdict(int)
        res = 0
        while r < n:
            tmp = s[r]
            r += 1
            counter[tmp] += 1
            while counter[tmp] > 1:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l)
        return res


def main():
    sol = Solution()

    s = "abcabcbb"
    res = sol.lengthOfLongestSubstring(s)
    print(res)

    s = "bbbbb"
    res = sol.lengthOfLongestSubstring(s)
    print(res)

    s = "pwwkew"
    res = sol.lengthOfLongestSubstring(s)
    print(res)


if __name__ == '__main__':
    main()
