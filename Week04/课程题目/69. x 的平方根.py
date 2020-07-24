# 69. x 的平方根.py


# 基本的二分法，因为x的平方在x为正时是单调递增的
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x // 2

        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            # mid = left + (right - left + 1) // 2
            mid = (left + right + 1) >> 1
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        # 因为一定存在，因此无需后处理
        return left


class Solution:
    def mySqrt(self, x: int) -> int:
        # 这里处理特殊情况后，二分法的右边界可以使用x//2
        if x <= 1:
            return x

        left = 0
        right = x // 2
        while left <= right:
            mid = left + (right - left) // 2
            tmp = mid * mid
            if tmp == x:
                return mid
            elif tmp < x:
                left = mid + 1
            else:
                right = mid - 1
        return right


# 牛顿法
class Solution:
    def mySqrt(self, x: int) -> int:
        res = x
        while res * res > x:
            res = (res + x // res) // 2
        return res


# 以下为自我练习
# 牛顿法
class Solution:
    def mySqrt(self, x: int) -> int:
        res = x
        while res * res > x:
            res = (res + x // res) // 2
        return res


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left = 1
        right = x // 2
        while left <= right:
            mid = left + ((right - left) >> 1)
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left <= right:
            mid = left + ((right - left) >> 1)
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


class Solution:
    def mySqrt(self, x: int) -> int:
        res = x
        while res * res > x:
            res = (res + x // res) >> 1
        return res


def main():
    sol = Solution()
    res = sol.mySqrt(2)
    print(res)


if __name__ == '__main__':
    main()
