# 191. 位1的个数.py


# 调用函数懒蛋法
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


# 每次模2除以2

# 每次右移一位，最后一位&1，&1为1则加1

# 利用x&(x-1)相当抹去最后一位1
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res


# cpp一行求解
# class Solution{
# public:
#     int hammingWeight(uint_32_t n) {
#     return (n > 0) ? 1 + hammingWeight(n & (n-1)) : 0;
#     }
# };


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count


def main():
    sol = Solution()

    n = 11
    res = sol.hammingWeight(n)
    print(res)

    n = (1 << 31) - 1
    res = sol.hammingWeight(n)
    print(res)


if __name__ == '__main__':
    main()
