# 90. 子集 II.py
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, pre: list):
            res.append(pre[:])
            for j in range(i, n):
                if j == i or nums[j] != nums[j - 1]:
                    pre.append(nums[j])
                    dfs(j + 1, pre)
                    pre.pop()

        nums.sort()
        res = []
        n = len(nums)
        dfs(0, [])
        return res


def main():
    sol = Solution()
    nums = [1, 2, 2]
    res = sol.subsetsWithDup(nums)
    print(res)


if __name__ == '__main__':
    main()
