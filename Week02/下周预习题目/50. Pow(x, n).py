# 50. Pow(x, n).py

# 1.暴力法：while n:
# 不断相乘
# 比较简单，不再赘述。
# 2.快速求幂。有递归和迭代两种写法。
# 递归
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(n: int) -> float:
            if n == 0:
                return 1.0
            y = quickMul(n >> 1)
            return y * y if not n & 1 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


# 时间复杂度：O(log(n))。递归的层数
# 空间复杂度：O(log(n))。递归的函数调用会使用栈空间。

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N & 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N >>= 1
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


# 时间复杂度：O(logn)，对n进行二进制拆分的时间复杂度。
# 空间复杂度：O(1)
def main():
    pass


if __name__ == '__main__':
    main()
