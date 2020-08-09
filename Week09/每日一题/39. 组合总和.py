# 39. 组合总和.py
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        res = []
        n = len(candidates)

        def dfs(i, pre, total):
            if total == target:
                res.append(pre)
                return
            for j in range(i, n):
                if total + candidates[j] <= target:
                    dfs(j, pre + [candidates[j]], total + candidates[j])

        dfs(0, [], 0)

        return res


def main():
    sol = Solution()

    nums = [2, 3, 6, 7]
    target = 7
    res = sol.combinationSum(nums, target)
    print(res)


if __name__ == '__main__':
    main()
