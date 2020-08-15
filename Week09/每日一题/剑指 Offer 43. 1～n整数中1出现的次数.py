# 剑指 Offer 43. 1～n整数中1出现的次数.py


class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res


class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur = divmod(n, 10)
        low = 0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit
            high, cur = divmod(high, 10)
            digit *= 10
        return res


class Solution:
    def countDigitOne(self, n: int) -> int:
        digit = 1
        high, cur = divmod(n, 10)
        low = 0
        res = 0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit
            high, cur = divmod(high, 10)
            digit *= 10
        return res


class Solution:
    def countDigitOne(self, n: int) -> int:
        digit = 1
        high, cur = divmod(n, 10)
        low = 0
        res = 0
        while high or cur:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit
            digit *= 10
            high, cur = divmod(high, 10)
        return res


def main():
    sol = Solution()
    n = 13
    res = sol.countDigitOne(n)
    print(res)


if __name__ == '__main__':
    main()
