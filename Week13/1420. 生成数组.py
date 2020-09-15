# 1420. 生成数组.py


class Solution:
    def f(self, n, i, k):
        if self.tmp[n][i][k] != -1:
            return self.tmp[n][i][k]
        if n == 0 or k == 0 or i == 0:
            self.tmp[n][i][k] = 0
            return 0
        if n == 1 and k == 1:
            self.tmp[n][i][k] = 1
            return 1
        r = 0
        for j in range(1, i):
            r += self.f(n - 1, j, k - 1)
            r %= 1000000007
        r += self.f(n - 1, i, k) * i
        r %= 1000000007
        self.tmp[n][i][k] = r
        return r

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        self.tmp = [[[-1 for _ in range(k + 1)] for _ in range(m + 1)] for _ in
                    range(n + 1)]
        r = 0
        for i in range(1, m + 1):
            r += self.f(n, i, k)
            r %= 1000000007
        return r


def main():
    pass


if __name__ == '__main__':
    main()
