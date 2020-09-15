# 1492. m 的第 k 个因子.py


# 暴力解法
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for c in range(1, n + 1):
            if n % c == 0:
                k -= 1
                if k == 0:
                    return c
        return -1


# 枚举优化
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        factor = 1
        while factor * factor <= n:
            if n % factor == 0:
                count += 1
                if count == k:
                    return factor
            factor += 1
        factor -= 1
        if factor * factor == n:
            factor -= 1
        while factor > 0:
            if n % factor == 0:
                count += 1
                if count == k:
                    return n // factor
            factor -= 1
        return -1


def main():
    pass


if __name__ == '__main__':
    main()
