# 493. 翻转对.py
from typing import List


# 暴力解法：两层循环，指定前一个元素，看下一个元素是否是nums[start] > 2*arr[j]
# 时间复杂度O(m^2)
# 分治
# 分为两个数组，假设我们已经解决该问题，左侧的翻转对我们已经求出，右侧的翻转对我们也已经求出
# 那么新增的翻转对只能是左侧相对于右侧的
# 求解的方法是与归并其实相同，只不过为了保持数组有序，还要再算做一次归并

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
        # 找翻转对的代码
        ans = 0
        i, j = l, mid + 1
        while i <= mid and j <= r:
            if (nums[i] + 1) >> 1 > nums[j]:
                ans += (mid - i + 1)
                j += 1
            else:
                i += 1
        nums[l:r + 1] = sorted(nums[l:r + 1])
        return ans


# 调用了系统的sorted，使得整个程序的时间复杂度变为了O(m*logn*logn)
# 可以看递归树，每一层变成了，m/k(log(m/k) * k  = m(logn - logk) k时每一层被分成的份数
# k最大为n最小为1
# 平均下来是1/2 nlogn

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
        # 找翻转对的代码
        ans = 0
        i, j = l, mid + 1
        while i <= mid and j <= r:
            if (nums[i] + 1) >> 1 > nums[j]:
                ans += (mid - i + 1)
                j += 1
            else:
                i += 1
        # 归并的代码
        cache = [0] * (r - l + 1)
        i, j, k = l, mid + 1, 0
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                cache[k] = nums[i]
                i += 1
            else:
                cache[k] = nums[j]
                j += 1
            k += 1
        if i <= mid:
            cache[k:] = nums[i:mid + 1]
        else:
            cache[k:] = nums[j:r + 1]
        nums[l:r + 1] = cache

        return ans


# 严格的nlogn，逆序对的统计
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
        ans = 0
        cache = [0] * (r - l + 1)
        i, t, c = l, l, 0
        for j in range(mid + 1, r + 1):
            # i这个指针指的一直都是刚刚大于2倍nums[j]的元素，因为j所在的nums[mid+1, r]有序
            # 所以我们可以记录上一次的i，这样i最多也只从l到mid遍历一次
            while i <= mid and (nums[i] + 1) >> 1 <= nums[j]:
                i += 1
            while t <= mid and nums[t] < nums[j]:
                cache[c] = nums[t]
                c += 1
                t += 1
            cache[c] = nums[j]
            c += 1
            ans += mid - i + 1
        while t <= mid:
            cache[c] = nums[t]
            c += 1
            t += 1
        nums[l:r + 1] = cache
        return ans


# 以下为自我练习
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, t, c = l, l, 0
        for j in range(mid + 1, r + 1):
            while t <= mid and (nums[t] + 1) >> 1 <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - t + 1
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
        i, c, t = l, 0, l
        for j in range(mid + 1, r + 1):
            while t <= mid and (nums[t] + 1) >> 1 <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - t + 1
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
        i, c, t = l, 0, l
        for j in range(mid + 1, r + 1):
            while t <= mid and (nums[t] + 1) >> 1 <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - t + 1
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
        i, c, t = l, 0, l
        for j in range(mid + 1, r + 1):
            while t <= mid and (nums[t] + 1) >> 1 <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - t + 1
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
        i, c, t = l, 0, l
        for j in range(mid + 1, r + 1):
            while t <= mid and (nums[t] + 1 >> 1) <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - t + 1
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
        i, c, t = l, 0, l
        for j in range(mid + 1, r + 1):
            while t <= mid and (nums[t] + 1 >> 1) <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - t + 1
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
        i, c, t = l, 0, l
        for j in range(mid + 1, r + 1):
            while t <= mid and (nums[t] + 1) >> 1 <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - t + 1
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
        i, c, t = l, 0, l
        for j in range(mid + 1, r + 1):
            while t <= mid and (nums[t] + 1) >> 1 <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - t + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l: r + 1] = cache
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
        i, c, t = l, 0, l
        for j in range(mid + 1, r + 1):
            while t <= mid and (nums[t] + 1) >> 1 <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - t + 1
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
        i, c, t = l, 0, l
        for j in range(mid + 1, r + 1):
            while t <= mid and nums[t] + 1 >> 1 <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - t + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l: r + 1] = cache
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
        i, c, t = l, 0, l
        for j in range(mid + 1, r + 1):
            while t <= mid and (nums[t] + 1) >> 1 <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - t + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


def main():
    sol = Solution()

    nums = [1, 3, 2, 3, 1]
    res = sol.reversePairs(nums)
    print(res)
    # 2

    nums = [2, 4, 3, 5, 1]
    res = sol.reversePairs(nums)
    print(res)
    # 3


if __name__ == '__main__':
    main()
