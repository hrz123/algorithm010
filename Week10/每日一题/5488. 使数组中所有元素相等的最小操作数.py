# 5488. 使数组中所有元素相等的最小操作数.py
class Solution:
    def minOperations(self, n: int) -> int:
        if n & 1:
            return (n - 1) * (n + 1) >> 2
        return n * n >> 2


def main():
    pass


if __name__ == '__main__':
    main()
