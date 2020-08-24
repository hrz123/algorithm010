# 878. 第 N 个神奇数字.py


class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        i1, i2 = 1, 1
        data = [1]
        for _ in range(N):
            p1, p2 = i1 * A, i2 * B
            small = min(p1, p2)
            data.append(small)
            if small == p1:
                i1 += 1
            if small == p2:
                i2 += 1
        return data[-1] % (10 ** 9 + 7)


class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        from math import gcd
        mod = 10 ** 9 + 7

        l = A // gcd(A, B) * B
        m = l // A + l // B - 1
        q, r = divmod(N, m)

        if r == 0:
            return q * l % mod

        heads = [A, B]
        for _ in range(r - 1):
            if heads[0] <= heads[1]:
                heads[0] += A
            else:
                heads[1] += B

        return (q * l + min(heads)) % mod


class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        from math import gcd
        mod = 10 ** 9 + 7
        l = A // gcd(A, B) * B

        def magic_below_x(x):
            # How many magical numbers are <= x?
            return x // A + x // B - x // l

        lo = 0
        hi = 10 ** 15
        while lo < hi:
            mi = (lo + hi) // 2
            if magic_below_x(mi) < N:
                lo = mi + 1
            else:
                hi = mi

        return lo % mod


def main():
    sol = Solution()

    n = 1
    a = 2
    b = 3
    res = sol.nthMagicalNumber(n, a, b)
    print(res)

    n = 4
    a = 2
    b = 3
    res = sol.nthMagicalNumber(n, a, b)
    print(res)

    n = 5
    a = 2
    b = 4
    res = sol.nthMagicalNumber(n, a, b)
    print(res)

    n = 3
    a = 6
    b = 4
    res = sol.nthMagicalNumber(n, a, b)
    print(res)

    n = 1000000000
    a = 40000
    b = 40000
    res = sol.nthMagicalNumber(n, a, b)
    print(res)


if __name__ == '__main__':
    main()
