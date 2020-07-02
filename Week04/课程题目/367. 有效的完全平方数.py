# 367. 有效的完全平方数.py

# 暴力解法
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i * i < num:
            i += 1
        return i * i == num


# 二分查找
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l < r:
            mid = l + (r - l) // 2
            if mid * mid < num:
                l = mid + 1
            else:
                r = mid
        return l * l == num


# 数学规律，等差数列
# 所有平方都可以协程奇书相加的形式
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        num1 = 1
        while num > 0:
            num -= num1
            num1 += 2
        return num == 0


# 牛顿法
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ans = num
        while ans * ans > num:
            ans = (ans + num // ans) // 2
        return ans * ans == num


def main():
    sol = Solution()
    res = sol.isPerfectSquare(15)
    print(res)


if __name__ == '__main__':
    main()
