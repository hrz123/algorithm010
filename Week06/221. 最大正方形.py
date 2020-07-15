# 221. 最大正方形.py
from typing import List


# 定义子问题
# 到i, j位置的最大正方形面积的边长，返回m-1, n-1,必须包含i，j
# 定义状态数组
# dp[i][j] i 0..m-1 j 0..n-1
# 递推方程
# f(i, j) = min{f(i-1, j), f(i, j-1)} if f(i-1, j) != f(i, j-1)
# f(i, j) = f(i, j-1) + 1 if a[i-f(i, j-1)][j-f(i, j-1)] else 0
# 可以只要一层
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        dp = [int(c) for c in matrix[0]]
        ans = max(dp)

        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            dp[0] = int(matrix[i][0])
            ans = max(ans, dp[0])
            for j in range(1, n):
                if matrix[i][j] == '1':
                    if dp[j] != dp[j - 1]:
                        dp[j] = min(dp[j], dp[j - 1]) + 1
                    else:
                        length = dp[j - 1]
                        previ = i - length
                        prevj = j - length
                        dp[j] = (length + 1) if matrix[previ][
                                                    prevj] == '1' else length
                else:
                    dp[j] = 0
                ans = max(ans, dp[j])
        return ans * ans


def main():
    matrix = [["0", "0", "0", "1"],
              ["1", "1", "0", "1"],
              ["1", "1", "1", "1"],
              ["0", "1", "1", "1"],
              ["0", "1", "1", "1"]]
    sol = Solution()
    res = sol.maximalSquare(matrix)
    print(res)


if __name__ == '__main__':
    main()
