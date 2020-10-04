# 4.py


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        p = n.bit_length()
        return (1 << p) - 1 - self.minimumOneBitOperations(n - (1 << (p - 1)))


def main():
    sol = Solution()
    n = 56162567
    res = sol.minimumOneBitOperations(n)
    print(res)


if __name__ == '__main__':
    main()
