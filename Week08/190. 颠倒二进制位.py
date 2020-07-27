# 190. 颠倒二进制位.py


# 正常循环32次
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1
            res += (n & 1)
            n >>= 1
        return res


# 提前停止
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while i < 32:
            res <<= 1
            res += (n & 1)
            n >>= 1
            i += 1
            if not n:
                break

        return res << 32 - i


# 以下为自我练习
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1
            res += (n & 1)
            n >>= 1
        return res


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while i < 32:
            res <<= 1
            res += (n & 1)
            n >>= 1
            i += 1
            if not n:
                break
        return res << 32 - i


def main():
    sol = Solution()

    n = 43261596
    res = sol.reverseBits(n)
    print(res)


if __name__ == '__main__':
    main()
