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


def main():
    sol = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    res = sol.combinationSum2(candidates, target)
    print(res)


if __name__ == '__main__':
    main()
