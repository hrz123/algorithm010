# 557. 反转字符串中的单词 III.py


class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        s = list(s)
        i = j = 0
        while j < n:
            while j < n and s[j] != ' ':
                j += 1
            l, r = i, j - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            j += 1
            i = j
        return ''.join(s)


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split(' ')[::-1])[::-1]


# 以下为自我练习
class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        s = list(s)
        i = j = 0
        while j < n:
            while j < n and s[j] != ' ':
                j += 1
            l, r = i, j - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            j += 1
            i = j
        return ''.join(s)


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]


class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        s = list(s)
        i, j = 0, 0
        while j < n:
            while j < n and s[j] != ' ':
                j += 1
            l, r = i, j - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            j += 1
            i = j
        return ''.join(s)


class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        s = list(s)
        i = j = 0
        while j < n:
            while j < n and s[j] != ' ':
                j += 1
            l, r = i, j - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            j += 1
            i = j
        return ''.join(s)


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]


def main():
    sol = Solution()
    s = "Let's take LeetCode contest"
    res = sol.reverseWords(s)
    print(res)


if __name__ == '__main__':
    main()
