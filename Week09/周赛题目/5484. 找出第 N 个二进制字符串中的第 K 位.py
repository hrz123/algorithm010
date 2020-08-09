# 5484. 找出第 N 个二进制字符串中的第 K 位.py
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1 and k == 1:
            return '0'
        size = (1 << n) - 1
        idx = k - 1
        if idx == size >> 1:
            return '1'
        if idx < size >> 1:
            return self.findKthBit(n - 1, k)
        return '1' if self.findKthBit(n - 1, size - idx) == '0' else '0'


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        i = 1

        while i < n:
            cur = s + '1' + ''.join(['0' if c == '1' else '1' for c in s[::-1]])
            s = cur
            i += 1

        return s[k - 1]


def main():
    sol = Solution()
    n = 4
    k = 11
    res = sol.findKthBit(n, k)
    print(res)

    n = 2
    k = 3
    res = sol.findKthBit(n, k)
    print(res)


if __name__ == '__main__':
    main()
