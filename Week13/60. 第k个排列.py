# 60. 第k个排列.py


# 官方题解
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        k -= 1
        ans = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]

        return "".join(ans)


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        res = []
        k -= 1
        valid = [True] * n
        for i in range(n):
            order = k // factorial[n - 1 - i] + 1
            for j in range(n):
                order -= valid[j]
                if order == 0:
                    res.append(str(j + 1))
                    valid[j] = False
                    break
            k %= factorial[n - 1 - i]
        return ''.join(res)


def main():
    sol = Solution()
    n = 3
    k = 3
    res = sol.getPermutation(n, k)
    print(res)
    n = 4
    k = 9
    res = sol.getPermutation(n, k)
    print(res)


if __name__ == '__main__':
    main()
