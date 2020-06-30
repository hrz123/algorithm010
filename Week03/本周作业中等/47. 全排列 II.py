# 47. 全排列 II.py
from typing import List


# 使用数组记录访问的元素
# 使用这样的方法剪枝
# 首先将数组排序，
# 因为回溯时间复杂度远大于排序的时间复杂度，而剪枝带来的时间上的优化很大

# 如果当前的数值和前一个索引的数值相等，并且前一个索引的数值还没用
# if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
#     continue;
# }
# 这样能保证重复的数值按原顺序输出

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:

                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if size == 0:
            return []

        nums.sort()

        used = [False] * len(nums)
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


# 改写使用 位掩码 记录访问的元素
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return

            for i in range(size):
                if ((used >> i) & 1) == 0:
                    # -的优先级大于>>
                    if i > 0 and nums[i] == nums[i - 1] and ((used >> i - 1) &
                                                             1) == 0:
                        continue
                    used ^= (1 << i)
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)

                    used ^= (1 << i)
                    path.pop()

        size = len(nums)
        if size == 0:
            return []

        nums.sort()

        used = 0
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


def main():
    nums = [1, 1, 2]
    sol = Solution()
    res = sol.permuteUnique(nums)
    print(res)


if __name__ == '__main__':
    main()
