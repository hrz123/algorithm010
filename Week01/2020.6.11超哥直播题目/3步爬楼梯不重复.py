# 3步爬楼梯不重复.py


# 思考
# 如果没有不能同步数限制
# f(m) = f(m-3) + f(m-2) + f(m-1)

# 但是需要记录额外信息，即上一次走了几步

# f(m) = f(m-3) if last_step != 3
#      + f(m-2) if last_step != 2
#      + f(m-1) if last_step != 1

# 所以需要记录两个状态
# f(start, j) i表示走到第i个台阶，j表示这一步走了j个台阶

# f(start, 1) = f(start-1, 2) + f(start-1, 3)
# f(start, 2) = f(start-2, 1) + f(start-2, 3)
# f(start, 3) = f(start-3, 1) + f(start-3, 2)

# f(start)= sum f(start, j) j = 1, 2, 3

# f(1, 1) = 1
# 1, 2 = 0
# 1, 3 = 0
# 2, 1 = 0
# 2, 2 = 1
# 2, 3 = 0
# 3, 1 = 1
# 3, 2 = 1
# 3, 3 = 1


class Solution:

    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        return self.helper(n, 1) + self.helper(n, 2) + self.helper(n, 3)

    def helper(self, n, k) -> int:
        memo = {
            (1, 1): 1,
            (1, 2): 0,
            (1, 3): 0,
            (2, 1): 0,
            (2, 2): 1,
            (2, 3): 0,
            (3, 1): 1,
            (3, 2): 1,
            (3, 3): 1
        }

        def inner(n, k):
            if (n, k) in memo:
                return memo[(n, k)]

            if k == 1:
                memo[(n, k)] = self.helper(n - k, 2) + self.helper(n - k, 3)
            elif k == 2:
                memo[(n, k)] = self.helper(n - k, 1) + self.helper(n - k, 3)
            else:
                memo[(n, k)] = self.helper(n - k, 1) + self.helper(n - k, 2)

            return memo[(n, k)]

        return inner(n, k)


def main():
    s = Solution()
    res = s.climbStairs(5)
    print(res)


if __name__ == '__main__':
    main()
