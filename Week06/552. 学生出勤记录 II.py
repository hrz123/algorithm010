# 552. 学生出勤记录 II.py


# 子问题
# 到索引为i的位置，前面用了几个A，到结尾有几个L，共有多少种
# sum(f(i, 0..1, 0..2))
# 定义状态数组
# f(i, j, k) 表示 到索引为i的位置，前面用了几个A，连续到结尾有几个L，共有多少种
# 递推方程
# 只能在结尾加字符P
# f(i, 0, 0) = f(i-1, 0, 0) + f(i-1, 0, 1) + f(i-1, 0, 2)
# 只能加L
# f(i, 0, 1) = f(i-1, 0, 0)
# f(i, 0, 2) = f(i-1, 0, 1)
# 加P加A
# f(i, 1, 0) = f(i-1, 1, 0) + f(i-1, 1, 1) + f(i-1, 1, 2)  加P
#            + f(i-1, 0, 0) + f(i-1, 0, 1) + f(i-1, 0, 2)  加A
# f(i, 1, 1) = f(i-1, 1, 0)
# f(i, 1, 2) = f(i-1, 1, 1)

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


def main():
    sol = Solution()
    n = 4
    res = sol.checkRecord(n)
    print(res)

    n = 3
    res = sol.checkRecord(n)
    print(res)


if __name__ == '__main__':
    main()
