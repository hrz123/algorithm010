# 29. 两数相除.py


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        # 把除数不断左移，直到它大于被除数
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count  # 这里的移位运算是把二进制（第count+1位上的1）转换为十进制
                dividend -= divisor
        if sign:
            result = -result
        return result if -(1 << 31) <= result <= (1 << 31) - 1 \
            else (1 << 31) - 1


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count
                dividend -= divisor
        if sign:
            result = -result
        return result if -(1 << 31) <= result <= (1 << 31) - 1 \
            else (1 << 31) - 1


def main():
    pass


if __name__ == '__main__':
    main()
