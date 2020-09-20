# 5504. 使数组和能被 P 整除.py
from typing import List


class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        mod = 1000000007
        ans = []
        dp = [0 for _ in range(1501)]
        pre = None
        for num in nums:
            res = float('inf')
            start, end = 1000, -501
            if pre:
                start, end = min(1000, pre + 10), max(pre - 10, -501)
            for k in range(start, end, -1):
                k += 500
                dp[k] = dp[k - 1] + abs(num - k + 500)
                if dp[k] < res:
                    res = dp[k]
                    pre = k - 500
            ans.append(res % mod)
        return ans


class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        mod = 1000000007
        ans = []
        dp = [0 for _ in range(200001)]
        for num in nums:
            res = float('inf')
            for k in range(100000, -100001, -1):
                dp[k + 100000] = dp[k + 100000 - 1] + abs(num - k)
                if dp[k + 100000] < res:
                    res = dp[k + 100000]
            ans.append(res % mod)
        return ans


def main():
    sol = Solution()
    nums = [1, 1, 1, 2, 3, 4]
    res = sol.numsGame(nums)
    print(res)

    nums = [*range(1, 100001)]
    res = sol.numsGame(nums)
    print(res)
    print(all(i == 0 for i in res))
    print(res.count(0))


if __name__ == '__main__':
    main()
