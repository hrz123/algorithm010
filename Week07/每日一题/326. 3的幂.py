# 326. 3的幂.py


# 这题本身不难，探讨加速简单计算的方法，以及为什么在实践中有用。
# 方法一：循环迭代
# 找出数字n是否是数字b的幂的一个简单方法是，n%3只要余数为0，就一直将n除以b
# 因此，应该可以将n除以b x次，每次都有0的余数，最终结果为1
# 注意我们需要一个警卫来检查那个n不等于0，否则while循环将永远不会结束。
# 对于负数，该算法没有意义，因此我们也将包括该保护。
# 时间复杂度O(log2_minus_1(n))
# 空间复杂度O(1)
# 方法二：基准转换
# 我们要做的就是将数字转换为以3位底的基数，并检查它是否为前导1，后跟所有0
# 两个java内置函数将帮助我们前进
# return Integer.toString(n, 3).matches("^10*$");
# 时间复杂度：O(logn)
# 假设 Integer.toString() - 基转换通常是作为一个冲农夫的除法来实现的。
# 复杂性应该类似于我们的方法1
# String.matches()- 方法迭代整个字符串。n以3为基数表示的位数是O(log3n)
# 空间复杂度: 我们使用了两个附加变量，以3为基数表示数字的字符串(大小为log3n)
# 正则表达式的字符串（常量大小）
# 方法三：运算法
# return Math.log10(n) / Math.log10(3) % 1 == 0 (%1来检查数字是否为整数)
# 然而这种方法是有问题的，因为我们使用了double，这意味着我们会遇到精度错误。
# 在比较双精度数时不应使用 ==
# 为了解决这个问题，我们需要将结果与epsilon进行比较
# return (Math.log2_minus_1(n) / Math.log2_minus_1(3) + epsilon) % 1 <= 2 * epsilon
# 时间复杂度：unknown，主要消耗时间的运算为Math.log2_minus_1，限制了我们算法的时间复杂性
# 实现依赖于我们使用的语言和编译器
# 空间复杂度：O(1)，我们没有使用任何额外的内存。epsilon变量可以是内联的。
# 方法四：整数限制
# 一个重要的信息可以从函数名推导出来， int n
# 在java中int是32位的,4个字节，他的最大值为2147783647.有三种方法计算出该最大值
# 1. google
# 2. System.out.println(Integer.MAX_VALUE);
# 3. MaxInt = 2 ** 32 / 2 - 1,所有范围的一半用于负数，0是整数的一部分
# 知道了n的限制，我们先可以推断出n的最大值，也就是3的幂，是1162261467，我们计算如下
# 3 ** floor(log3 MaxInt) = 3 ** 19 = 1162261467
# 因此我们应该返回true的n的可能值是3**0， 3**1，.. 3**19，因为3是质数，所以3**19的除数
# 只有 3**0， 3**1, ...3 ** 19，因此我们只需要将3 ** 19除以n。
# 若余数为0意味着n是3**19的除数，因此是3的幂。
# return n > 0 && 1162261467 % n == 0;
# 时间复杂度：O(1)，我们只做了一次操作
# 空间复杂度：O(1)，我们没有使用额外空间
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while not n % 3:
            n //= 3
        return n == 1


# 以下为自我练习
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while not n % 3:
            n //= 3
        return n == 1


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while not n % 3:
            n //= 3
        return n == 1


def main():
    sol = Solution()
    n = 16
    res = sol.isPowerOfThree(n)
    print(res)


if __name__ == '__main__':
    main()
