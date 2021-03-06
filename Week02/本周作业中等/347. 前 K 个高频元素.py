# 347. 前 K 个高频元素.py
import collections
import heapq
import random
from typing import List


# 方法1：heap
# 首先建立一个元素值对应出现频率的哈希表。在JAVA中使用HashMap，但需要手工填值。
# 在Python中提供一个字典结构用作哈希表和在collections库中的Counter方法去构建我们需要的哈希表。
# 这一步需要O(N)时间，其中N是数组中元素的个数。
# 第二步建立堆，堆中添加一个元素的复杂度是O(log2_minus_1(k))，要进行N次复杂度是O(N)
# 最后一步是输出结果，复杂度为O(klogk)
# 在python中可以使用heapq库中的nlargest方法，可以在想用时间内完成，但只需要一行代码解决。
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


# 方法2：桶排序
# 因为要排序的不会超过nums数组的长度，所以是一个有范围的数字，可以使用桶排序加快速度。
# 同样建立一个元素值对应出现频率的哈希表。
# 然后以出现频率为索引。建立size+1的数组。出现频率索引对应元素值。
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        bucket = [None] * (size + 1)
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1

        for key, value in counter.items():
            if not bucket[value]:
                bucket[value] = [key]
            else:
                bucket[value].append(key)
        res = []
        for i in range(size, -1, -1):
            if bucket[i]:
                res.extend(bucket[i])
            if len(res) >= k:
                break
        if len(res) > k:
            res = res[:k]
        return res


# 时间复杂度：
# 建立哈希表要遍历整个数组，O(N)。之后遍历哈希表建立计数排序所需数组，
# 时间复杂度与数组中不同的元素数目相关，不同元素个数小于数组大小。
# 遍历计数排序数组，O(N)。综合起来，时间复杂度是O(m)

# 空间复杂度：哈希表和计数排序数组占额外空间。O(N)


# 以下为自我练习
# 桶排序
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter = collections.defaultdict(int)
        # for num in arr:
        #     counter[num] += 1

        counter = collections.Counter(nums)
        size = len(nums)
        bucket = [[] for _ in range(size + 1)]

        for key, value in counter.items():
            bucket[value].append(key)

        res = [0 for _ in range(k)]
        start = 0
        for i in range(size, -1, -1):
            res[start: start + len(bucket[i])] = bucket[i]

            start += len(bucket[i])
            if start == k:
                return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        return heapq.nlargest(k, counter, counter.get)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.defaultdict(int)
        for n in nums:
            counter[n] += 1

        heap = []

        for num, count in counter.items():
            if len(heap) == k:
                if count > heap[0][0]:
                    heapq.heappushpop(heap, (count, num))
            else:
                heapq.heappush(heap, (count, num))
        return [elem[1] for elem in heap]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 桶排序
        buckets = [[] for _ in range(n)]

        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1
        for num, count in counter.items():
            buckets[count - 1].append(num)
        res = [0] * k
        start = 0
        for i in range(n - 1, -1, -1):
            if buckets[i]:
                res[start:start + len(buckets[i])] = buckets[i]
                start += len(buckets[i])
                if start == k:
                    return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        return heapq.nlargest(k, counter, counter.get)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c1 = collections.Counter(nums)
        c2 = [[] for _ in range(len(nums) + 1)]
        for num, count in c1.items():
            c2[count].append(num)
        res = []
        for i in range(len(nums), -1, -1):
            if c2[i]:
                res.extend(c2[i])
            if len(res) == k:
                return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c1 = collections.Counter(nums)
        c2 = [[] for _ in range(len(nums) + 1)]
        for key, val in c1.items():
            c2[val].append(key)
        res = []
        for i in range(len(nums), -1, -1):
            res.extend(c2[i])
            if len(res) == k:
                return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        val = list(counter.keys())
        l, r = 0, len(val) - 1
        while l <= r:
            pivot = self.partition(val, l, r, counter)
            if pivot == k - 1:
                return val[:k]
            if pivot > k - 1:
                r = pivot - 1
            else:
                l = pivot + 1

    def partition(self, val, l, r, counter):
        ran = random.randint(l, r)
        val[ran], val[r] = val[r], val[ran]
        pivot = r
        right = l
        for i in range(l, r):
            if counter.get(val[i]) >= counter.get(val[pivot]):
                val[i], val[right] = val[right], val[i]
                right += 1
        val[right], val[pivot] = val[pivot], val[right]
        return right


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        n = len(nums)
        c2 = [[] for _ in range(n + 1)]
        for v, c in counter.items():
            c2[c].append(v)
        res = []
        for i in range(n, -1, -1):
            res.extend(c2[i])
            if len(res) == k:
                return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1
        c2 = [[] for _ in range(len(nums) + 1)]
        for num, v in counter.items():
            c2[v].append(num)
        res = []
        for i in range(len(nums), -1, -1):
            res.extend(c2[i])
            if len(res) == k:
                return res





def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    sol = Solution()
    res = sol.topKFrequent(nums, k)
    print(res)


if __name__ == '__main__':
    main()
