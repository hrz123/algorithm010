# 120. 三角形最小路径和.py
from typing import List


# 子问题
# 定义状态数组：f(i, j) = min(f(i+1, j), f(i+1, j+1)) + a[i,j]
# 返回f(0, 0)
# 递推方程
# f(i, j) = min(f(i+1, j), f(i+1, j+1)) + a[i,j]
# 初始状态
# f(n-1, j) = a[n-1, j]
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[n - 1][:]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]


def main():
    nums = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    sol = Solution()
    res = sol.minimumTotal(nums)
    print(res)


if __name__ == '__main__':
    main()
