# 46. 全排列.py
from typing import List


# 使用 数组 来判断某个位置的元素是否已经使用过
# 使用O(n)的空间
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(depth, nums, size, path, used, res):
            # recursion terminator
            if depth == size:
                res.append(path[:])
                return

            # process current row logic
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    # drill down
                    dfs(depth + 1, nums, size, path, used, res)

                    # reverse current row status if needed
                    used[i] = False
                    path.pop()

        size = len(nums)
        if size == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(0, nums, size, [], used, res)
        return res


# 使用 hashset 来判断某个位置的元素是否已经使用过
# 使用O(n)的空间
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, hash_set, path, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not nums[i] in hash_set:
                    hash_set.add(nums[i])
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, hash_set, path, res)
                    path.pop()
                    hash_set.remove(nums[i])

        size = len(nums)
        if size == 0:
            return []
        res = []
        path = []
        hash_set = set()
        dfs(nums, size, 0, hash_set, path, res)
        return res


# 使用 位掩码 来判断某个位置的元素是否已经使用过
# 空间最省，只要不越界。O(1)的空间
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if ((used >> i) & 1) == 0:
                    used ^= (1 << i)
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)

                    used ^= (1 << i)
                    path.pop()

        size = len(nums)
        if size == 0:
            return []
        state = 0
        res = []
        dfs(nums, size, 0, [], state, res)
        return res


# 迭代的写法
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [n] + perm[i:])  # insert n
            perms = new_perms
        return perms


# 以下为自我练习
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            new_perms = []

            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [num] + perm[i:])

            perms = new_perms
        return perms


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i, ans, res):
            # terminator
            if i == n:
                res.append(ans)
                return
            # process current row logic
            # drill down
            for j in range(i + 1):
                dfs(i + 1, ans[:j] + [nums[i]] + ans[j:], res)

            # reverse current row status if needed

        dfs(0, [], res)

        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            new_res = []
            for ans in res:
                n = len(ans)
                new_res.extend(
                    [ans[:i] + [num] + ans[i:] for i in range(n + 1)])
            res = new_res
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res = [ans[:i] + [num] + ans[i:] for ans in res for i in
                   range(len(ans) + 1)]
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res = [ans[:i] + [num] + ans[i:] for ans in res for i in range(
                len(ans) + 1)]
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res = [ans[:i] + [num] + ans[i:] for ans in res for i in range(
                len(ans) + 1)]
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res = [ans[:i] + [num] + ans[i:] for ans in res for i in range(
                len(ans) + 1)]
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res = [ans[:i] + [n] + ans[i:] for ans in res
                   for i in range(len(ans) + 1)]
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res = [ans[:i] + [n] + ans[i:] for ans in res for i in range(len(
                ans) + 1)]
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        q = [[]]
        nq = []
        for n in nums:
            for ans in q:
                for i in range(len(ans) + 1):
                    nq.append(ans[:i] + [n] + ans[i:])
            q, nq = nq, []
        return q


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        q, nq = [[]], []
        for n in nums:
            for ans in q:
                for i in range(len(ans) + 1):
                    nq.append(ans[:i] + [n] + ans[i:])
            q, nq = nq, []
        return q


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res = [ans[:i] + [n] + ans[i:] for ans in res for i in range(
                len(ans) + 1)]
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res = [ans[:i] + [n] + ans[i:] for
                   ans in res for i in range(len(ans) + 1)]
        return res


def main():
    solution = Solution()

    nums = [1, 2, 3]
    res = solution.permute(nums)
    print(res)

    nums = []
    res = solution.permute(nums)
    print(res)


if __name__ == '__main__':
    main()
