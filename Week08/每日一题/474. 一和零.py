# 474. 一和零.py
from typing import List


# 定义子问题
# 到第i个元素，最后还剩下m个0，n个1没用的状态，最多能拼出几个字符串
# 定义状态数组
# f(start, m, n)
# 递推方程
# f(start, m, n) = max(f(start-1, m, n), f(start-1, m+0s, n+1s) + 1)
# 初始化
# f(0, m, n) = 0
# f(0, m-0s, n-1s) = 1 如果不越界
# 加入哨兵
# f(-1, start, j) = float('-inf')
# f(-1, m, n) = 0
# 其余都可以初始化为0
# 返回值
# max(f(n-1))
# 优化空间复杂度
# 只需记录i,start-1两个
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
# dp[start][j][k] 表示输入字符串在子区间 [0, start] 能够使用 j 个 0 和 k 个 1 的字符串的最大数量。
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


# 以下为自我练习

# 定义子问题
# 对于前strs[:start]，j, k个01能凑出多少个字符串
# 递推方程
# 不要当前这个，要当前这个，前面就只剩j-0s，k-1s能取到的最大值
# f(start, j, k) = max(f(start-1, j, k), f(start-1, j-0s, k-1s) +1)
# 边界条件
# j -0s >=0, k - 1s >=0
# f(0, j, k) = 0
# f(1, j, k)
# 返回值f(len, m, n)
# 优化恐慌间复杂度
# 只需要m,n的矩阵，原地更新从右下到左上
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            item_0_count = s.count('0')
            item_1_count = len(s) - item_0_count
            for i in range(m, item_0_count - 1, -1):
                for j in range(n, item_1_count - 1, -1):
                    dp[i][j] = max(dp[i][j],
                                   dp[i - item_0_count][j - item_1_count] + 1)
        return dp[m][n]


# 定义子问题
# 对于strs[:start], j个0，k个1最多可以可拼出多少个字符串
# 递推方程
# f(start, j, k) = 这个不要 f(start-1, j, k) 这个要 f(start-1, j-0s, k-1s) + 1
# 初始化和边界条件
# f(0, j, k)都是0
# j-0s, k-1s >= 0
# 返回值
# f(size, j, k)
# 优化空间复杂度
# 不需要i这一维
# 可以从右下到左上原地递推
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            item_0_count = s.count('0')
            item_1_count = len(s) - item_0_count
            for i in range(m, item_0_count - 1, -1):
                for j in range(n, item_1_count - 1, -1):
                    dp[i][j] = max(dp[i][j],
                                   dp[i - item_0_count][j - item_1_count] + 1)
        return dp[m][n]


# 定义子问题
# 在strs[:i]中，我们有j个0，k个1最多可以拿到多少个字符串
# f(i, j, k)
# 递推方程
# 对于i这个字符串，我们可以要也可以不要
# 不要
# f(i, j, k) = f(i-1, j, k)
# 要
# f(i, j, k) = f(i-1, j-0s, k-1s) + 1
# 初始化和边界条件
# f(0, j, k) = 0
# j - 0s, k-1s >=0
# 返回值
# f(n, j, k)
# 优化状态空间
# 我们只需要维持j, k维的数组
# 从右下往左上更新的时候可以原地更新
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            item_0_count = s.count('0')
            item_1_count = len(s) - item_0_count
            for i in range(m, item_0_count - 1, -1):
                for j in range(n, item_1_count - 1, -1):
                    dp[i][j] = max(dp[i][j],
                                   dp[i - item_0_count][j - item_1_count] + 1)
        return dp[m][n]


# 定义子问题
# f(i, j, k)为s[:i]中有j个0k个1可以最多拼出多少字符串
# f(i, j, k) = max(f(i-1, j, k), f(i-1, j-c0, k-c1)+1)
# 初始化
# f(0, j, k) = 0
# f(1, j, k)
# 返回值
# f(len, m, n)
# 优化复杂度
# 不需要第一维，二维矩阵，增加0这个索引
# 因为c0,c1都是非负数，我们从右下角往左上角可以原地更新
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            c0 = s.count('0')
            c1 = len(s) - c0
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - c0][j - c1] + 1)
        return dp[m][n]


# f(i, m, n) s[:i]可以用m个0n个1最多凑出几个
# f(i, m, n) = max(f(i-1, m, n), f(i-1, m-0s, n-1s) + 1)
# 初始化和边界条件
# f(0, 0, 0) = 0
# f(1, m, n)
# 注意m, n不能越界
# 返回值f(len, m, n)
# 注意给0这个边界条件
# 优化复杂度，我们只需要两维
# 从右下到左上原地更新
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            c0 = s.count('0')
            c1 = len(s) - c0
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - c0][j - c1] + 1)
        return dp[m][n]


# 定义子问题
# f(i, j, k)s[:i]用j个0k个1最多可以凑出几个
# f(i, j, k) = f(i-1, j, k), f(i-1, j-0s, k-1s) + 1
# 初始化和边界条件
# f(0, j, k) = 0
# 注意不要越界
# 返回值
# f(len, m, n)
# 优化复杂度
# 我们只需要i-1时候的，我们从右下往左上可以原地递推
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            c0 = s.count('0')
            c1 = len(s) - c0
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - c0][j - c1] + 1)
        return dp[m][n]


def main():
    sol = Solution()

    arr = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    res = sol.findMaxForm(arr, m, n)
    print(res)

    arr = ["10", "0", "1"]
    m = 1
    n = 1
    res = sol.findMaxForm(arr, m, n)
    print(res)


if __name__ == '__main__':
    main()
