# 389. 找不同.py

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


def main():
    sol = Solution()

    s = "abcd"
    t = "abcde"
    res = sol.findTheDifference(s, t)
    print(res)


if __name__ == '__main__':
    main()
