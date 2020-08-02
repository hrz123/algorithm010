# 416. 分割等和子集.py
from typing import List


# 定义子问题
# 到了i这个索引，j这个数字能不能取到
# 定义状态数组
# f(i, j)
# 递推方程
# f(i, j) = f(i-1, j) or f(i - 1, j - a[i])
# 初始化
# 初始化全部为False，将f(0, a[0]) 和 f(0, 0)初始化为True，注意要判断越界
# i 0 .. n-1 j 0 .. target
# 返回值，一旦f(k, target)为True，返回True，否则返回False
# 优化空间复杂度
# 我们只需要两个数组来回表示i-1和i的情况即可
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum & 1:
            return False
        target = _sum >> 1
        dp = [False] * (target + 1)
        dp[0] = True
        if nums[0] <= target:
            dp[nums[0]] = True
        ndp = [False] * (target + 1)
        for i in range(1, len(nums)):
            if dp[target]:
                return True
            for j in range(target + 1):
                ndp[j] = dp[j] or dp[j - nums[i]]
            dp, ndp = ndp, dp
        return dp[target]


def main():
    sol = Solution()

    nums = [1, 5, 5, 11]
    res = sol.canPartition(nums)
    print(res)

    nums = [1, 1]
    res = sol.canPartition(nums)
    print(res)


if __name__ == '__main__':
    main()
