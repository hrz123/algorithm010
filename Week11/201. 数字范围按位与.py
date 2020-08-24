# 201. 数字范围按位与.py


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # 抹去最右边的 1
            n = n & (n - 1)
        return n


def main():
    pass


if __name__ == '__main__':
    main()
