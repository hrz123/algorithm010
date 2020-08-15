# 18. 四数之和.py
from typing import List


# 首先这是一个回溯问题
# 可以穷举暴力做法
# 是O(n^4)复杂度的做法

# 那么我们为了减小时间复杂度，就需要剪枝
# 排序会有利于我们剪枝，不会占用很多时间复杂度
# 排好序之后
# 我们遍历i从0..n-4
# 相当于在右侧剩余的数列寻找三数之和等于target - arr[start]
# 再遍历j从 start+1 .. n-3
# 相当于在右侧剩余的数列寻找两数之和等于target - arr[start] - arr[j]
# 在有序数组上找两数之和可以使用典型的双指针夹逼办法
# 双指针夹逼方法的时间复杂度为O(n)
# 这样的时间复杂度一共是O(n^3)

# --------------------------------------------------
# 还可以提高速度的方法是，在双指针夹逼的时候，建立和到索引的哈希表
# 这样，在遍历的时候，只要索引比前面两个大，就可以加进，省去再次计算的时间

# 但是不全
# --------------------------------------------------

# 不包含重复的
# 可以在遍历的时候就排除
# 如果nums[start] == arr[start-1], start += 1，跳过这个i
# 如果nums[j] == arr[j-1], j += 1，跳过这个j
# 双指针的时候l, row, 如果nums[l] == arr[l-1]，跳过这个l
#                 如果nums[row] == arr[row+1]，跳过这个r

# 在进一步剪枝
# arr[start] + 3 * arr[j] > target: break
# arr[start] + 3 * arr[-1] < target:
#     while start < n - 4 and arr[start] == arr[start + 1]: start += 1
#     start += 1
#     continue


# arr[start] + arr[j] + 2 * arr[j + 1] > target: break
# arr[start] + arr[j] + 2 * arr[-1] < target:
#     while j < n - 3 and arr[j] == arr[j + 1]: j += 1
#     j += 1
#     continue

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        n = len(nums)
        if not nums or len(nums) < 4:
            return res

        i = 0

        while i < n - 3:
            j = i + 1
            if nums[i] + 3 * nums[j] > target:
                break
            if nums[i] + 3 * nums[-1] < target:
                while i < n - 4 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
                continue
            while j < n - 2:
                if nums[i] + nums[j] + 2 * nums[j + 1] > target:
                    break
                if nums[i] + nums[j] + 2 * nums[-1] < target:
                    while j < n - 3 and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    continue
                l, r = j + 1, n - 1
                while l < r:
                    total = nums[l] + nums[r] + nums[i] + nums[j]
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        # 只用更新这里就好，其他两个分支判断要判断l的左边界和r的右边界
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1

                j += 1
                while j < n - 2 and nums[j] == nums[j - 1]:
                    j += 1
            i += 1
            while i < n - 3 and nums[i] == nums[i - 1]:
                i += 1

        return res


# 国际站解法
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:
            return

        # solve 2-sum
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums) - N + 1):  # careful about range
                if target < nums[i] * N or target > nums[-1] * N:
                    # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i - 1] != nums[i]:
                    # recursively reduce N
                    self.findNsum(nums[i + 1:], target - nums[i], N - 1,
                                  result + [nums[i]], results)
        return


# 检查后改进
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(nums, target, N, result, results):
            if len(nums) < N \
                    or N < 2 \
                    or target < nums[0] * N \
                    or target > nums[-1] * N:  # early termination
                return
            if N == 2:  # two pointers solve sorted 2-sum problem
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        # 可以只l自加1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # recursively reduce N
                for i in range(len(nums)):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNsum(nums[i + 1:], target - nums[i], N - 1,
                                 result + [nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results


# 传指针，而非sliced list
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(l, r, N, target, result, results):
            # recursion terminator
            if r - l + 1 < N \
                    or N < 2 \
                    or target < nums[l] * N \
                    or target > nums[r] * N:
                return

            # process current row logic
            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if target == s:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif target > s:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r):
                    if i == l or nums[i] != nums[i - 1]:
                        # drill down
                        findNsum(i + 1, r, N - 1, target - nums[i], result + [
                            nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums) - 1, 4, target, [], results)
        return results


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNSum(l, r, N, target, result, results):
            if r - l + 1 < N \
                    or N < 2 \
                    or nums[l] * N > target \
                    or nums[r] * N < target:
                return

            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r):
                    if i == l or nums[i] != nums[i - 1]:
                        findNSum(i + 1, r, N - 1, target - nums[i],
                                 result + [nums[i]], results)

        nums.sort()
        results = []
        findNSum(0, len(nums) - 1, 4, target, [], results)
        return results


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNSum(l, r, N, target, result, results):
            if r - l + 1 < N \
                    or N < 2 \
                    or target < nums[l] * N \
                    or target > nums[r] * N:
                return

            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif target > s:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r):
                    if i == l or nums[i] != nums[i - 1]:
                        findNSum(i + 1, r, N - 1, target - nums[i], result + [
                            nums[i]], results)

        nums.sort()
        results = []
        findNSum(0, len(nums) - 1, 4, target, [], results)
        return results


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNSum(l, r, N, target, result, results):
            if r - l + 1 < N \
                    or N < 2 \
                    or target < nums[l] * N \
                    or target > nums[r] * N:
                return

            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r):
                    if i == l or nums[i] != nums[i - 1]:
                        findNSum(i + 1, r, N - 1, target - nums[i],
                                 result + [nums[i]], results)

        nums.sort()
        results = []
        findNSum(0, len(nums) - 1, 4, target, [], results)
        return results


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNSum(l, r, N, target, result, results):
            if r - l + 1 < N \
                    or N < 2 \
                    or nums[l] * N > target \
                    or nums[r] * N < target:
                return
            if N == 2:
                while l < r:
                    _sum = nums[l] + nums[r]
                    if _sum == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                    elif _sum < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r):
                    if i == l or nums[i] != nums[i - 1]:
                        findNSum(i + 1, r, N - 1, target - nums[i], result + [
                            nums[i]], results)

        nums.sort()
        res = []
        findNSum(0, len(nums) - 1, 4, target, [], res)
        return res


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k \
                    or k < 2 \
                    or target < nums[l] * k \
                    or target > nums[r] * k:
                return
            if k == 2:
                while l < r:
                    _sum = nums[l] + nums[r]
                    if _sum == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        # 去重
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif _sum < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r):
                    if i == l or nums[i] != nums[i - 1]:
                        findKSum(i + 1, r, k - 1, target - nums[i],
                                 result + [nums[i]], results)

        nums.sort()
        res = []
        findKSum(0, len(nums) - 1, 4, target, [], res)
        return res


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNSum(l, r, k, target, result, results):
            if r - l + 1 < k \
                    or k < 2 \
                    or target < nums[l] * k \
                    or target > nums[r] * k:
                return
            if k == 2:
                while l < r:
                    _sum = nums[l] + nums[r]
                    if _sum == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif _sum < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r):
                    if i == l or nums[i] != nums[i - 1]:
                        findNSum(i + 1, r, k - 1, target - nums[i], result + [
                            nums[i]], results)

        nums.sort()
        results = []
        findNSum(0, len(nums) - 1, 4, target, [], results)
        return results


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k \
                    or k < 2 \
                    or target < nums[l] * k \
                    or target > nums[r] * k:
                return
            if k == 2:
                while l < r:
                    _sum = nums[l] + nums[r]
                    if _sum == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif _sum < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r):
                    if i == l or nums[i] != nums[i - 1]:
                        findKSum(i + 1, r, k - 1, target - nums[i], result + [
                            nums[i]], results)

        nums.sort()
        res = []
        findKSum(0, len(nums) - 1, 4, target, [], res)
        return res


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k \
                    or k < 2 \
                    or target < nums[l] * k \
                    or target > nums[r] * k:
                return
            if k == 2:
                while l < r:
                    _sum = nums[l] + nums[r]
                    if _sum == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif target > _sum:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r):
                    if i == l or nums[i] != nums[i - 1]:
                        findKSum(i + 1, r, k - 1, target - nums[i], result + [
                            nums[i]], results)

        nums.sort()
        res = []
        findKSum(0, len(nums) - 1, 4, target, [], res)
        return res


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k \
                    or k < 2 \
                    or nums[l] * k > target \
                    or nums[r] * k < target:
                return
            if k == 2:
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r - k + 2):
                    if i == l or nums[i] != nums[i - 1]:
                        findKSum(i + 1, r, k - 1, target - nums[i],
                                 result + [nums[i]], results)

        res = []
        nums.sort()
        findKSum(0, len(nums) - 1, 4, target, [], res)
        return res


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k or k < 2 or nums[l] * k > target or nums[r] * k < \
                    target:
                return
            if k == 2:
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif total > target:
                        r -= 1
                    else:
                        l += 1
            else:
                for i in range(l, r - k + 2):
                    if i == l or nums[i] != nums[i - 1]:
                        findKSum(i + 1, r, k - 1, target - nums[i], result + [
                            nums[i]], results)

        nums.sort()
        res = []
        findKSum(0, len(nums) - 1, 4, target, [], res)
        return res


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k or k < 2 or nums[l] * k > target or nums[r] * k < \
                    target:
                return
            if k == 2:
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r - k + 2):
                    if i == l or nums[i] != nums[i - 1]:
                        findKSum(i + 1, r, k - 1, target - nums[i], result + [
                            nums[i]], results)

        nums.sort()
        res = []
        findKSum(0, len(nums) - 1, 4, target, [], res)
        return res


def main():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    sol = Solution()
    res = sol.fourSum(nums, target)
    print(res)


if __name__ == '__main__':
    main()
