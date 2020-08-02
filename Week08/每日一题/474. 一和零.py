# 474. 一和零.py
from typing import List


# 定义子问题
# 到第i个元素，最后还剩下m个0，n个1没用的状态，最多能拼出几个字符串
# 定义状态数组
# f(i, m, n)
# 递推方程
# f(i, m, n) = max(f(i-1, m, n), f(i-1, m+0s, n+1s) + 1)
# 初始化
# f(0, m, n) = 0
# f(0, m-0s, n-1s) = 1 如果不越界
# 加入哨兵
# f(-1, i, j) = float('-inf')
# f(-1, m, n) = 0
# 其余都可以初始化为0
# 返回值
# max(f(n-1))
# 优化空间复杂度
# 只需记录i,i-1两个
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if not strs:
            return 0
        _len = len(strs)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        ndp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = 0
        for s in strs:
            s00 = s.count('0')
            s01 = len(s) - s00
            for i in range(m + 1):
                for j in range(n + 1):
                    ndp[i][j] = max(dp[i][j],
                                    dp[i + s00][j + s01] + 1
                                    if 0 <= i + s00 <= m and 0 <= j + s01 <= n
                                    else float('-inf'))
            dp, ndp = ndp, dp
        return max(e for row in dp for e in row)


# 依然是尝试「题目问啥，就把啥定义成状态」。
#
# dp[i][j][k] 表示输入字符串在子区间 [0, i] 能够使用 j 个 0 和 k 个 1 的字符串的最大数量。
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if len(strs) == 0:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 准备很多个背包
        for strs_item in strs:
            item_count0 = strs_item.count('0')
            item_count1 = len(strs_item) - item_count0
            # 遍历可容纳的背包
            for i in range(m, item_count0 - 1, -1):  # 采取倒序
                for j in range(n, item_count1 - 1, -1):
                    dp[i][j] = max(dp[i][j],
                                   1 + dp[i - item_count0][j - item_count1])
        return dp[m][n]


def main():
    sol = Solution()

    arr = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    res = sol.findMaxForm(arr, m, n)
    print(res)


if __name__ == '__main__':
    main()
