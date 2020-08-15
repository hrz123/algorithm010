# 231. 2的幂.py


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not n & n - 1


# 注意这里一定是n>0，python语言的int类型和java中不一样
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not n & (n - 1)


# Java解法
# class Solution {
#     public boolean isPowerOfTwo(int n) {
#         return n > 0 && (n & (n - 1)) == 0;
#     }
# }


# 以下为自我练习
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not n & (n - 1)


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not n & (n - 1)


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not n & (n - 1)


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not n & (n - 1)


def main():
    sol = Solution()

    n = 0
    res = sol.isPowerOfTwo(n)
    print(res)

    n = -1
    res = sol.isPowerOfTwo(n)
    print(res)

    n = 2
    res = sol.isPowerOfTwo(n)
    print(res)


if __name__ == '__main__':
    main()
