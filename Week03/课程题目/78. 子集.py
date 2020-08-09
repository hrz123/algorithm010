# 78. 子集.py
import itertools
from functools import reduce
from typing import List


# 思路1：库函数
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums) + 1):
            for tmp in itertools.combinations(nums, i):
                # 产生从nums中选出i个的组合
                res.append(tmp)
        return res


# 思路2：迭代
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [[num] + ans for ans in res]
        return res


# 思路3：递归（回溯算法）
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(i, ans):
            res.append(ans)
            for j in range(i, n):
                helper(j + 1, ans + [nums[j]])

        helper(0, [])
        return res


# 以下为自我练习
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(i, ans):
            res.append(ans)

            for j in range(i, n):
                helper(j + 1, ans + [nums[j]])

        helper(0, [])
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [[num] + ans for ans in res]
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(level, ans):
            res.append(ans)

            for i in range(level, n):
                helper(i + 1, ans + [nums[i]])

        helper(0, [])

        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res.extend([ans + [num] for ans in res])
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            # 注意这里不加最外面的中括号会报错
            res.extend([ans + [num] for ans in res])
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res.extend([ans + [num] for ans in res])
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res.extend([ans + [n] for ans in res])
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return reduce(
            lambda acc, x: acc + [ans + [x] for ans in acc],
            nums,
            [[]]
        )


def main():
    sol = Solution()
    res = sol.subsets([1, 2, 3])
    print(res)


if __name__ == '__main__':
    main()
