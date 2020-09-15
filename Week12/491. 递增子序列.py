# 491. 递增子序列.py
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 1:
            return []
        res = []

        def dfs(i, pre):
            dic = set()
            if len(pre) >= 2:
                res.append(pre)
            if i == n:
                return
            for j in range(i, n):
                if nums[j] not in dic:
                    if i == 0 or nums[j] >= nums[i - 1]:
                        dic.add(nums[j])
                        dfs(j + 1, pre + [nums[j]])

        dfs(0, [])
        return res


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = [[nums[0]]]
        idx_map = {nums[0]: -1}
        for i in range(1, len(nums)):
            if nums[i] not in idx_map:
                idx_map[nums[i]] = len(res)
                res += [lst + [nums[i]] for lst in res if
                        lst[-1] <= nums[i]] + [[nums[i]]]
            else:
                tmp = len(res)
                res += [res[j] + [nums[i]] for j in range(tmp) if
                        res[j][-1] <= nums[i] and j >= idx_map[nums[i]]]
                idx_map[nums[i]] = tmp
        return [lst for lst in res if len(lst) > 1]


# 以下为自我练习
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, pre):
            if len(pre) > 1:
                res.append(pre)
            if i == n:
                return
            mem = set()
            for j in range(i, n):
                if nums[j] not in mem and (i == 0 or nums[j] >= nums[i - 1]):
                    mem.add(nums[j])
                    dfs(j + 1, pre + [nums[j]])

        res = []
        n = len(nums)
        dfs(0, [])
        return res


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, pre):
            if len(pre) > 1:
                res.append(pre)
            if i == n:
                return
            mem = set()
            for j in range(i, n):
                if nums[j] not in mem and (i == 0 or nums[j] >= nums[i - 1]):
                    mem.add(nums[j])
                    dfs(j + 1, pre + [nums[j]])

        res = []
        n = len(nums)
        dfs(0, [])
        return res


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, pre):
            if len(pre) > 1:
                res.append(pre)
            if i == n:
                return
            mem = set()
            for j in range(i, n):
                if nums[j] not in mem and (i == 0 or nums[j] >= nums[i - 1]):
                    mem.add(nums[j])
                    dfs(j + 1, pre + [nums[j]])

        n = len(nums)
        res = []
        dfs(0, [])
        return res


def main():
    sol = Solution()
    nums = [4, 6, 7, 7]
    res = sol.findSubsequences(nums)
    print(res)

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]
    res = sol.findSubsequences(nums)
    print(res)


if __name__ == '__main__':
    main()
