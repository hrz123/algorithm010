# 8. 字符串转换整数 (atoi).py


class Solution:
    def myAtoi(self, s: str) -> int:
        # empty string
        if not s:
            return 0
        i = 0
        n = len(s)
        res = 0
        zero = ord('0')
        # remove spaces
        while i < n and s[i] == ' ':
            i += 1
        # handle illegal
        if i >= n or (s[i] not in {'+', '-'} and not s[i].isdigit()):
            return 0
        # handle signs
        negative = s[i] == '-'
        i = i + 1 if s[i] in {'+', '-'} else i
        exceed = 8 if negative else 7
        limit = -0x80000000 if negative else 0x7fffffff
        while i < n and s[i].isdigit():
            val = ord(s[i]) - zero
            if res > 214748364 or res == 214748364 and val > exceed:
                return limit
            res *= 10
            res += val
            i += 1
        return -res if negative else res


# 以下为自我练习
class Solution:
    def myAtoi(self, s: str) -> int:
        # empty string
        if not s:
            return 0
        i = 0
        n = len(s)
        res = 0
        zero = ord('0')
        # remove spaces
        while i < n and s[i] == ' ':
            i += 1
        # handle illegal
        if i == n or (s[i] not in {'-', '+'} and not s[i].isdigit()):
            return 0
        # handle signs
        negative = s[i] == '-'
        i += 1 if s[i] in {'-', '+'} else 0
        # handle exceed
        digit = 8 if negative else 7
        limit = -2147483648 if negative else 2147483647
        while i < n and s[i].isdigit():
            val = ord(s[i]) - zero
            if res > 214748364 or res == 214748364 and val > digit:
                return limit
            res *= 10
            res += val
            i += 1
        return -res if negative else res


def main():
    sol = Solution()

    s = "42"
    res = sol.myAtoi(s)
    print(res)

    s = "   -42"
    res = sol.myAtoi(s)
    print(res)

    s = "4193 with words"
    res = sol.myAtoi(s)
    print(res)

    s = "words and 987"
    res = sol.myAtoi(s)
    print(res)


if __name__ == '__main__':
    main()
