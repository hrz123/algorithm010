# 552. 学生出勤记录 II.py


# 子问题
# 到索引为i的位置，前面用了几个A，到结尾有几个L，共有多少种
# sum(f(start, 0..1, 0..2))
# 定义状态数组
# f(start, j, k) 表示 到索引为i的位置，前面用了几个A，连续到结尾有几个L，共有多少种
# 递推方程
# 只能在结尾加字符P
# f(start, 0, 0) = f(start-1, 0, 0) + f(start-1, 0, 1) + f(start-1, 0, 2)
# 只能加L
# f(start, 0, 1) = f(start-1, 0, 0)
# f(start, 0, 2) = f(start-1, 0, 1)
# 加P加A
# f(start, 1, 0) = f(start-1, 1, 0) + f(start-1, 1, 1) + f(start-1, 1, 2)  加P
#            + f(start-1, 0, 0) + f(start-1, 0, 1) + f(start-1, 0, 2)  加A
# f(start, 1, 1) = f(start-1, 1, 0)
# f(start, 1, 2) = f(start-1, 1, 1)

# 初始化
# f(0, 0, 0) = 1
# f(0, 0, 1) = 1
# f(0, 0, 2) = 0
# f(0, 1, 0) = 1
# f(0, 1, 1) = 0
# f(0, 1, 2) = 0
class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3
        mod = 10 ** 9 + 7
        a00, a01, a02, a10, a11, a12 = 1, 1, 0, 1, 0, 0
        for i in range(1, n):
            a00, a01, a02, a10, a11, a12 = (
                (a00 + a01 + a02) % mod,
                a00,
                a01,
                (a00 + a01 + a02 + a10 + a11 + a12) % mod,
                a10,
                a11
            )
        return (a00 + a01 + a02 + a10 + a11 + a12) % mod


# 以下为自我练习
# 定义子问题
# f(start, j, k), i表示当前记录个数，j表示A的个数，k表示结尾连续L的个数
# 定义状态数组
# f(start, j, k)
# f(start, 0, 0), f(start, 0, 1), f(start, 0, 2), f(start, 1, 0), f(start, 1, 1), f(start, 1, 2)
# 递推方程
# f(start, 0, 0) = f(start-1, 0, 0) + f(start-1,0,1) + f(start-1, 0, 2)
# f(start,0,1) = f(start-1,0,0)
# f(start,0, 2) = f(start-1,0,1)
# f(start, 1, 0) = (添加p) f(start-1,1,0) + f(start-1,1,1) + f(start-1, 1, 2)
#            + (添加A) f(start-1,0,0) + f(start-1,0,1) + f(start-1, 0, 2)
# f(start, 1, 1) = f(start-1, 1, 0)
# f(start, 1, 2) = f(start-1, 1, 1)
# 初始化
# 0, 0, 0  1
# 0, 0, 1  1
# 0, 0, 2  0
# 0, 1, 0  1
# 0, 1, 1  0
# 0, 1, 2  0
# 返回值
# sum(000, 001, 002, 010, 011, 012) % 10^9+7
# 优化空间复杂度
# 只需要6个值
class Solution:
    def checkRecord(self, n: int) -> int:
        f00, f01, f02, f10, f11, f12 = 1, 1, 0, 1, 0, 0
        mod = 10 ** 9 + 7
        for i in range(1, n):
            # 注意这里不每一步取模的话会超时
            f00, f01, f02, f10, f11, f12 = (
                (f00 + f01 + f02) % mod,
                f00,
                f01,
                (f00 + f01 + f02 + f10 + f11 + f12) % mod,
                f10,
                f11
            )
        return (f00 + f01 + f02 + f10 + f11 + f12) % mod


class Solution:
    def checkRecord(self, n: int) -> int:
        f00, f01, f02, f10, f11, f12 = 1, 0, 0, 0, 0, 0
        mod = 10 ** 9 + 7
        for _ in range(n):
            f00, f01, f02, f10, f11, f12 = (
                (f00 + f01 + f02) % mod,
                f00,
                f01,
                (f00 + f01 + f02 + f10 + f11 + f12) % mod,
                f10,
                f11
            )
        return (f00 + f01 + f02 + f10 + f11 + f12) % mod


# f(i, j, k)表示当前索引数，j表示有A的个数，k表示末尾L的个数
# f(i, 0, 0) = f(i-1, 0, 0) + f(i-1, 0, 1) + f(i-1, 0, 2)
# f(i, 0, 1) = f(i-1, 0, 0)
# f(i, 0, 2) = f(i-1, 0, 1)
# f(i, 1, 0) = f(i-1, 1, 0) + f(i-1, 1, 1) + f(i-1, 1, 2)
#              f(i-1, 0, 0) + f(i-1, 0, 1) + f(i-1, 0, 2)
# f(i, 1, 1) = f(i-1, 1, 0)
# f(i, 1, 2) = f(i-1, 1, 1)
# 初始化
# 我们知道，n=1时，只有ALP三种，f00 = 1 f01 = 1 f02 = 0 f10 = 1 f11 =0 f12=0
# 我们可否使用哨兵
# f00 = 1，其他为0就可以实现
# 返回值，这些的和
# 优化空间复杂度，常量
class Solution:
    def checkRecord(self, n: int) -> int:
        f00 = 1
        f01 = f02 = f10 = f11 = f12 = 0
        mod = 10 ** 9 + 7
        for i in range(n):
            f00, f01, f02, f10, f11, f12 = (
                (f00 + f01 + f02) % mod,
                f00,
                f01,
                (f00 + f01 + f02 + f10 + f11 + f12) % mod,
                f10,
                f11
            )
        return (f00 + f01 + f02 + f10 + f11 + f12) % mod


# 定义子问题
# f(i, 01, 012) A的数量为01，结尾有多少个
# f00 = f00 + f01 + f02
# f01= f00
# f02=f01
# f10 = f00,f01,f02,f10,f11,f12
# f11= f10
# f12 = f11
class Solution:
    def checkRecord(self, n: int) -> int:
        f00 = 1
        f01 = f02 = f10 = f11 = f12 = 0
        mod = 10 ** 9 + 7
        for _ in range(n):
            f00, f01, f02, f10, f11, f12 = (
                (f00 + f01 + f02) % mod,
                f00,
                f01,
                (f00 + f01 + f02 + f10 + f11 + f12) % mod,
                f10,
                f11
            )
        return (f00 + f01 + f02 + f10 + f11 + f12) % mod


# f(i, 01, 012)n个记录，01个A前面有，012个连续的L结尾
# f(i, 0, 0) = f(i-1, 0, 0) +f(i-1, 0, 1) + f(i-1, 0, 2)
# f(i, 0, 1) = f(i-1, 0, 0)
# f(i, 0, 2) = f(i-1, 0, 1)
# f(i, 1, 0) = f(i-1, 0, 0) + f01+f11+f10+f11+f12
# f(i, 1, 1) = f(i-1, 1, 0)
# f(i, 1, 2) = f(i, 1, 1)
# 初始化和边界条件
# f00, f01, f10 == 1在一个索引时
# 我们添加哨兵
# 可以让f00 = 1，其余为0
# 返回值这些的和，mod上
# 优化复杂度
# 只需要6个变量
class Solution:
    def checkRecord(self, n: int) -> int:
        f00 = 1
        f01 = f02 = f10 = f11 = f12 = 0
        mod = 10 ** 9 + 7
        for i in range(n):
            f00, f01, f02, f10, f11, f12 = (
                (f00 + f01 + f02) % mod,
                f00,
                f01,
                (f00 + f01 + f02 + f10 + f11 + f12) % mod,
                f10,
                f11
            )
        return (f00 + f01 + f02 + f10 + f11 + f12) % mod


def main():
    sol = Solution()
    n = 4
    res = sol.checkRecord(n)
    print(res)

    n = 3
    res = sol.checkRecord(n)
    print(res)

    n = 2
    res = sol.checkRecord(n)
    print(res)


if __name__ == '__main__':
    main()
