# 389. 找不同.py


# Map法
# 字符串ASCII差值法：
# 异或法
from functools import reduce


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        memo = [0] * 26
        a = ord('a')
        for c in s:
            memo[ord(c) - a] += 1
        for c in t:
            if memo[ord(c) - a] == 0:
                return c
            memo[ord(c) - a] -= 1


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for c in s:
            res ^= ord(c)
        for c in t:
            res ^= ord(c)
        return chr(res)


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = reduce(lambda acc, x: acc ^ ord(x), s, 0)
        return chr(reduce(lambda acc, x: acc ^ ord(x), t, res))


def main():
    sol = Solution()

    s = "abcd"
    t = "abcde"
    res = sol.findTheDifference(s, t)
    print(res)


if __name__ == '__main__':
    main()
