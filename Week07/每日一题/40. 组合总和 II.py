# 40. 组合总和 II.py
from typing import List


# dfs


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[
        List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def _dfs(i, pre, target):
            if target == 0:
                res.append(pre)
                return
            for j in range(i + 1, n):
                # 去重
                if j == i + 1 or candidates[j] != candidates[j - 1]:
                    if candidates[j] <= target:
                        _dfs(j, pre + [candidates[j]], target - candidates[j])
                    else:
                        break

        for i in range(n):
            # 去重
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            elif candidates[i] <= target:
                _dfs(i, [candidates[i]], target - candidates[i])
            else:
                break
        return res


# 以下为自我练习
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[
        List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []

        # 下一个访问位置的开头，之前的和是pre，得到该和的数组是ans
        def dfs(i, pre, ans):
            if pre == target:
                res.append(ans)
                return
            for j in range(i, n):
                if j == i or candidates[j] != candidates[j - 1]:
                    if pre + candidates[j] <= target:
                        dfs(j + 1, pre + candidates[j], ans + [candidates[j]])

        dfs(0, 0, [])
        return res


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[
        List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def dfs(i, pre, ans):
            if pre == target:
                res.append(ans)
                return
            for j in range(i, n):
                if j == i or candidates[j] != candidates[j - 1]:
                    if pre + candidates[j] <= target:
                        dfs(j + 1, pre + candidates[j], ans + [candidates[j]])

        dfs(0, 0, [])

        return res


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[
        List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, pre, ans):
            if pre == target:
                res.append(ans)
                return
            for j in range(i, n):
                if j == i or candidates[j] != candidates[j - 1]:
                    if pre + candidates[j] <= target:
                        dfs(j + 1, pre + candidates[j], ans + [candidates[j]])

        dfs(0, 0, [])
        return res


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[
        List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, pre, ans):
            if pre == target:
                res.append(ans)
                return
            for j in range(i, n):
                if j == i or candidates[j] != candidates[j - 1]:
                    if pre + candidates[j] <= target:
                        dfs(j + 1, pre + candidates[j], ans + [candidates[j]])

        dfs(0, 0, [])
        return res


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[
        List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, val, pre):
            if val == target:
                res.append(pre)
                return
            for j in range(i, n):
                if j == i or candidates[j] != candidates[j - 1]:
                    if val + candidates[j] <= target:
                        dfs(j + 1, val + candidates[j], pre + [candidates[j]])

        dfs(0, 0, [])
        return res


class Solution:
    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        def dfs(i, value, pre):
            if value == target:
                res.append(pre)
                return
            for j in range(i, n):
                if j == i or candidates[j] != candidates[j - 1]:
                    if value + candidates[j] <= target:
                        dfs(j + 1, value + candidates[j], pre + [candidates[j]])

        n = len(candidates)
        res = []
        candidates.sort()
        dfs(0, 0, [])
        return res


def main():
    sol = Solution()

    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    res = sol.combinationSum2(candidates, target)
    print(res)

    candidates = [2, 5, 2, 1, 2]
    target = 5
    res = sol.combinationSum2(candidates, target)
    print(res)

    candidates = [14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12,
                  34, 16, 25, 32,
                  8, 7, 30, 12, 33, 20, 21, 29, 24, 17, 27, 34, 11, 17, 30, 6,
                  32, 21, 27,
                  17, 16, 8, 24, 12, 12, 28, 11, 33, 10, 32, 22, 13, 34, 18, 12]
    target = 27
    res = sol.combinationSum2(candidates, target)
    print(res)
    print(len(res))


if __name__ == '__main__':
    main()
