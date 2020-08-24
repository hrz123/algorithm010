# 1544. 整理字符串.py
import string


class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        flag = False
        for i in range(len(s) - 1):
            if s[i] and s[i + 1] and abs(ord(s[i]) - ord(s[i + 1])) == 32:
                s[i] = ""
                s[i + 1] = ""
                flag = True
        s = "".join(s)
        if flag:
            return self.makeGood(s)
        return s


class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        lo = string.ascii_lowercase
        hi = string.ascii_uppercase

        for c in s:
            if not res:
                res.append(c)
            else:
                if c in lo:
                    if res[-1] in hi and lo.index(c) == hi.index(res[-1]):
                        res.pop()
                    else:
                        res.append(c)
                else:
                    if res[-1] in lo and hi.index(c) == lo.index(res[-1]):
                        res.pop()
                    else:
                        res.append(c)
        return ''.join(res)


def main():
    sol = Solution()
    s = "leEeetcode"
    res = sol.makeGood(s)
    print(res)


if __name__ == '__main__':
    main()
