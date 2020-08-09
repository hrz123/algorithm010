# 342. 4的幂.py


# 1. 暴力解，不解释
# 2. 暴力解法+预计算
# 我们知道输入的整数是32位整数x<2**31-1的，因此我们最大的4的幂次是15
# 所以我们总共有0-15 16种可能性
# 3.大于0且log2后是一个偶数
# 4.位操作：4的幂，二进制位都在1，3，5等位置，00000001, 00000100, 00010000
#          而只是2的幂，二进制都在2,4,6等位置
# 135位置的16进制为0x55555555 32位表示，246的16进制为0xaaaaaaaa，位与上其中一个等于0或1
# 5. 位操作判断是2的幂，对3的余数为1的是4的幂，为2的话是2的幂
class Solution:
    def __init__(self):
        s = 1
        self.nums = {1}
        for i in range(15):
            s *= 4
            self.nums.add(s)

    def isPowerOfFour(self, num: int) -> bool:
        return num in self.nums


class Powers:
    def __init__(self):
        s = 1
        self.nums = {1}
        for i in range(15):
            s *= 4
            self.nums.add(s)


class Solution:
    p = Powers()

    def isPowerOfFour(self, num: int) -> bool:
        return num in self.p.nums


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and not num & (num - 1) and not num & 0xaaaaaaaa


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and not num & (num - 1) and num & 0x55555555


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and (num & 0x55555555) and not num & (num - 1)


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and not num & (num - 1) and bool(num & 0x55555555)


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and not num & (num - 1) and bool(num & 0x55555555)


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and not num & (num - 1) and bool(num & 0x55555555)


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and not num & (num - 1) and bool(num & 0x55555555)


def main():
    sol = Solution()

    num = 16
    res = sol.isPowerOfFour(num)
    print(res)


if __name__ == '__main__':
    main()
