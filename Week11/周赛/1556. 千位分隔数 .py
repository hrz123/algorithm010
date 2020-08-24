# 1556. 千位分隔数 .py
class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return '0'
        c = 0
        res = []
        while n:
            n, mod = divmod(n, 10)
            res.append(str(mod))
            c += 1
            if c == 3:
                res.append('.')
                c = 0
        if res[-1] == '.':
            res.pop()
        return ''.join(reversed(res))


def main():
    sol = Solution()
    res = sol.thousandSeparator(123456789)
    print(res)

    res = sol.thousandSeparator(0)
    print(res)

    # res = sol.thousandSeparator(-1)
    # print(res)


if __name__ == '__main__':
    main()
