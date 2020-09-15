# 剑指 Offer 51. 数组中的逆序对.py
from typing import List


# 暴力法：枚举i枚举j，O(m^2)
# 归并排序，分治法，使用归并排序的思想 O(nlogn)
# 树状数组:O(nlogn)

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid + 1, r)
        return self.merge(nums, l, mid, r) + left + right

    def merge(self, nums, l, mid, r):
        ans = 0  # 增加
        res = [0] * (r - l + 1)
        i, j, k = l, mid + 1, 0
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                res[k] = nums[i]
                i += 1
            else:
                # 注意这里加上所有当前i和到mid之间的数，mid-start+1
                ans += (mid - i + 1)  # 增加
                res[k] = nums[j]
                j += 1
            k += 1
        if i <= mid:
            res[k:] = nums[i:mid + 1]
        else:
            res[k:] = nums[j:r + 1]
        nums[l:r + 1] = res
        return ans  # 增加


# 以下为自我练习
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid + 1, r)
        return left + right + self.merge(nums, l, mid, r)

    def merge(self, nums, l, mid, r):
        cnt = 0
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - i + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - i + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - i + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - i + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - i + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - i + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0 for _ in range(r - l + 1)]
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - i + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - i + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - i + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - i + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + (r - l >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - i + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)
    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + (r - l >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, c = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - i + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


def main():
    sol = Solution()

    nums = [7, 5, 6, 4]
    res = sol.reversePairs(nums)
    print(res)
    # 5

    nums = [1, 3, 2, 3, 1]
    res = sol.reversePairs(nums)
    print(res)
    # 4

    nums = [2, 4, 3, 5, 1]
    res = sol.reversePairs(nums)
    print(res)
    # 5


if __name__ == '__main__':
    main()
