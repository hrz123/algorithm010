# 面试题 08.01. 三步问题.py


# f(i) = f(i-1)+f(i-2)+f(i-3)
# f(1) = 1
# f(2) = 2
# f(3) = 4
# f(0) = 1
class Solution:
    def waysToStep(self, n: int) -> int:
        if n < 3:
            return n
        f0, f1, f2 = 1, 1, 2
        for _ in range(n - 2):
            f0, f1, f2 = f1, f2, (f0 + f1 + f2) % 1000000007
        return f2


class Solution:
    def waysToStep(self, n: int) -> int:
        res = 0

        def dfs(i, pre):
            nonlocal res
            if i == n:
                res += 1
                return
            for c in (1, 2, 3):
                if c != pre and i + c <= n:
                    dfs(i + c, c)

        dfs(0, None)
        return res


class Solution:
    def waysToStep(self, n: int) -> list:
        res = []
        steps = [1, 2, 3]

        def dfs(i, pre):
            if i == n:
                res.append(pre)
                return
            for c in steps:
                if i + c <= n:
                    dfs(i + c, pre + [c])

        dfs(0, [])
        return res


class Solution:
    def waysToStep(self, n: int) -> int:
        if n < 3:
            return n
        f0, f1, f2 = 1, 1, 2
        for _ in range(n - 2):
            f0, f1, f2 = f1, f2, (f0 + f1 + f2) % 1000000007
        return f2


# f(i) = f(i-1) +f(i-2) +f(i-3)
# 初始化和边界条件
# f(1) = 1
# f(0) = 1
# f(2) = 2
# f(3) = 4
class Solution:
    def waysToStep(self, n: int) -> int:
        if n < 3:
            return n
        f0, f1, f2 = 1, 1, 2
        for _ in range(n - 2):
            f0, f1, f2 = f1, f2, (f0 + f1 + f2) % 1000000007
        return f2


def main():
    sol = Solution()
    n = 4
    res = sol.waysToStep(n)
    print(res)


if __name__ == '__main__':
    main()
