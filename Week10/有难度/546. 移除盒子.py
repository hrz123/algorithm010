# 546. 移除盒子.py
from typing import List


class Solution:

    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        self.dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        return self.calculatePoints(boxes, 0, n - 1, 0)

    def calculatePoints(self, boxes, l, r, k):
        dp = self.dp
        if l > r:
            return 0
        if dp[l][r][k]:
            return dp[l][r][k]
        while r > l and boxes[r] == boxes[r - 1]:
            r -= 1
            k += 1
        dp[l][r][k] = self.calculatePoints(boxes, l, r - 1, 0) + (
                k + 1) * (k + 1)
        for i in range(l, r):
            if boxes[i] == boxes[r]:
                dp[l][r][k] = max(
                    dp[l][r][k],
                    self.calculatePoints(boxes, l, i, k + 1) +
                    self.calculatePoints(boxes, i + 1, r - 1, 0)
                )
        return dp[l][r][k]


# class Solution:
#     def removeBoxes(self, boxes: List[int]) -> int:
#
#         m = len(boxes)
#
#         dp = [[[0] * m for _ in range(m)] for n in range(m)]
#
#         def helper(m, r, k):  # 删除区间[m,r]和r右侧k个a[r]的积分
#             if m > r:
#                 return 0
#             if dp[m][r][k] != 0:
#                 return dp[m][r][k]
#             while r > m and boxes[r] == boxes[
#                 r - 1]:  # 找到尾巴重复数的个数，这个时候a[r]为重复数，
#                 r -= 1  # 如果尾巴不是重复，这里的k不会变
#                 k += 1
#
#             dp[m][r][k] = helper(m, r - 1, 0) + (k + 1) * (
#                     k + 1)  # 移除a[r]和k个a[r]
#
#             for i in range(m, r):
#                 if boxes[i] == boxes[r]:  # 移除a[r]和k个a[r],移除i,r之间的数,再移除剩下的
#                     dp[m][r][k] = max(dp[m][r][k],
#                                       helper(m, i, k + 1) + helper(i + 1, r - 1,
#                                                                    0))
#             return dp[m][r][k]
#
#         return helper(0, m - 1, 0)


def main():
    sol = Solution()
    res = sol.removeBoxes([1, 2, 3])
    print(res)


if __name__ == '__main__':
    main()
