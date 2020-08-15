# 50. Pow(x, n).py

# 上周预习题，这周默写

# 递归
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(num: int) -> float:
            if num == 0:
                return 1
            y = quickMul(num >> 1)
            return y * y * x if num & 1 else y * y

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


# 迭代
# 维持一个贡献值，初始化ans等于1.0
# while num != 0
# 初始化x_contribute= x
# 如果num是奇数，那么令ans*=x_contribute
# x_contribute*=x_contribute 增加下一次num为奇数时的x_contribute
# num // 2
# 如此循环，返回ans
# 加上num为负时的判断
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(num: int) -> float:
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while num:
                if num & 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 num 二进制表示的最低位，这样我们每次只要判断最低位即可
                num >>= 1
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


# 以下为自我练习
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(x, n):

            x_contribute = x
            ans = 1

            while n:
                if n & 1:
                    ans *= x_contribute
                x_contribute *= x_contribute
                n >>= 1
            return ans

        if n < 0:
            x = 1 / x
            n = -n
        return fast_pow(x, n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(x, n):
            if n == 0:
                return 1

            half = fast_pow(x, n >> 1)

            return half * half * x if n & 1 else half * half

        if n < 0:
            n = -n
            x = 1 / x
        return fast_pow(x, n)


# 递归
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


# 循环
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


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n):
            if n == 0:
                return 1
            half = helper(n >> 1)
            return half * half * x if n & 1 else half * half

        if n < 0:
            n = -n
            x = 1 / x
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
            n = -n
            x = 1 / x
        return helper(n)


# 递归
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


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n):
            if n == 0:
                return 1
            half = helper(n >> 1)
            return half * half * x if n & 1 else half * half

        if n < 0:
            n = -n
            x = 1 / x
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
            n = -n
            x = 1 / x
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
            n = -n
            x = 1 / x
        return helper(n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n):
            if n == 0:
                return 1
            half = helper(n >> 1)
            return half * half * x if n & 1 else half * half

        if n < 0:
            n = -n
            x = 1 / x
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
            n = -n
            x = 1 / x
        return helper(n)


def main():
    x = 2
    n = 10
    sol = Solution()
    res = sol.myPow(x, n)
    print(res)


if __name__ == '__main__':
    main()
