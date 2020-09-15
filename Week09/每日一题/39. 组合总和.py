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


# 以下为自我练习
class Solution:
    def combinationSum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        res = []
        n = len(candidates)

        def dfs(i, pre, ans):
            if pre >= target:
                if pre == target:
                    res.append(ans)
                return
            for j in range(i, n):
                dfs(j, pre + candidates[j], ans + [candidates[j]])

        dfs(0, 0, [])
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        res = []
        n = len(candidates)

        def dfs(i, pre, ans):
            if pre == target:
                res.append(ans)
                return
            for j in range(i, n):
                if pre + candidates[j] <= target:
                    dfs(j, pre + candidates[j], ans + [candidates[j]])

        dfs(0, 0, [])
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[
        List[int]]:
        res = []
        n = len(candidates)

        def dfs(i, val, pre):
            if val == target:
                res.append(pre)
                return
            for j in range(i, n):
                if val + candidates[j] <= target:
                    dfs(j, val + candidates[j], pre + [candidates[j]])

        dfs(0, 0, [])
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[
        List[int]]:
        res = []
        n = len(candidates)

        def dfs(i, val, pre):
            if val == target:
                res.append(pre)
                return
            for j in range(i, n):
                if candidates[j] + val <= target:
                    dfs(j, val + candidates[j], pre + [candidates[j]])

        dfs(0, 0, [])
        return res


class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        def dfs(i, val, pre):
            if val == target:
                res.append(pre)
                return
            for j in range(i, n):
                if val + candidates[j] <= target:
                    dfs(j, val + candidates[j], pre + [candidates[j]])

        res = []
        n = len(candidates)
        dfs(0, 0, [])
        return res


def main():
    sol = Solution()

    nums = [2, 3, 6, 7]
    target = 7
    res = sol.combinationSum(nums, target)
    print(res)


if __name__ == '__main__':
    main()
