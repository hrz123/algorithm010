# 59. 螺旋矩阵 II.py
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r, u, d = 0, n - 1, 0, n - 1
        c = 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        while l <= r and u <= d:
            i, j = l, u
            while j <= r:
                res[i][j] = c
                c += 1
                j += 1
            i, j = l + 1, r
            while i <= d:
                res[i][j] = c
                c += 1
                i += 1
            if l <= r - 1 and u <= d - 1:
                i, j = d, r - 1
                while j >= l:
                    res[i][j] = c
                    c += 1
                    j -= 1
                i, j = d - 1, l
                while i > u:
                    res[i][j] = c
                    c += 1
                    i -= 1
            l += 1
            r -= 1
            u += 1
            d -= 1
        return res


class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1):  # left to right
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1):  # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1):  # right to left
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1):  # bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat


class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1):
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1):
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1):
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1):
                mat[i][l] = num
                num += 1
            l += 1
        return mat


def main():
    sol = Solution()
    res = sol.generateMatrix(3)
    print(res)
    res = sol.generateMatrix(1)
    print(res)
    res = sol.generateMatrix(2)
    print(res)


if __name__ == '__main__':
    main()
