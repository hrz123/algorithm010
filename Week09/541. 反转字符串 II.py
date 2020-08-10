# 541. 反转字符串 II.py


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        i = 0
        two_k = k << 1
        while i < n:
            l, r = i, min(i + k - 1, n - 1)
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            i += two_k
        return ''.join(s)


# 以下为自我练习
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        i = 0
        two_k = k << 1
        while i < n:
            l, r = i, min(i + k - 1, n - 1)
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            i += two_k
        return ''.join(s)


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        i = 0
        two_k = k << 1
        while i < n:
            l, r = i, min(i + k - 1, n - 1)
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            i += two_k
        return ''.join(s)


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        i = 0
        two_k = k << 1
        while i < n:
            l, r = i, min(i + k - 1, n - 1)
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            i += two_k
        return ''.join(s)


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        i = 0
        two_k = k << 1
        while i < n:
            l, r = i, min(i + k - 1, n - 1)
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            i += two_k
        return ''.join(s)


def main():
    sol = Solution()

    s = "abcdefg"
    k = 2
    res = sol.reverseStr(s, k)
    print(res)

    s = "abcdefg"
    k = 8
    res = sol.reverseStr(s, k)
    print(res)


if __name__ == '__main__':
    main()
