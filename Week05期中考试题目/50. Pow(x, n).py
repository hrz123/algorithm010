# 50. Pow(x, n).py


# 快速幂
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n):
            if n == 0:
                return 1
            half = helper(n >> 1)
            return half * half * x if n & 1 else half * half

        if n < 0:
            x = 1 / x
            n = -n
        return helper(n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n):
            ans = 1

            x_contribute = x
            while n:
                if n & 1:
                    ans *= x_contribute
                x_contribute *= x_contribute
                n >>= 1

            return ans

        if n < 0:
            x = 1 / x
            n = -n
        return helper(n)


def main():
    sol = Solution()
    res = sol.myPow(3, 3)
    print(res)


if __name__ == '__main__':
    main()
