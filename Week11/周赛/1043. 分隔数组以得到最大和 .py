# 1043. 分隔数组以得到最大和 .py
from typing import List


# 定义子问题
# f(i, j, k)为s[i:j]分成k连续子树组的最大值
# f(i, j, k) = f(i, p, k-1) + f(p+1, j, 1)
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for k in range(1, K + 1):
                if i >= k:
                    dp[i] = max(dp[i], max(A[i - k:i]) * k + dp[i - k])
        return dp[-1]


def main():
    sol = Solution()
    nums = [1, 15, 7, 9, 2, 5, 10]
    n = 3
    res = sol.maxSumAfterPartitioning(nums, n)
    print(res)

    nums = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
    n = 4
    res = sol.maxSumAfterPartitioning(nums, n)
    print(res)


if __name__ == '__main__':
    main()
