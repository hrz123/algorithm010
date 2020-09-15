# 315. 计算右侧小于当前元素的个数.py
from typing import List


# 暴力解法
# O(m^2)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n - 1):
            count = 0
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    count += 1
            res[i] = count
        return res


# 归并排序
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]

        tmp = [None for _ in range(size)]
        indexes = [i for i in range(size)]
        res = [0 for _ in range(size)]

        self.__helper(nums, 0, size - 1, tmp, indexes, res)

        return res

    def __helper(self, nums, left, right, tmp, indexes, res):
        # merge
        if left == right:
            return
        mid = left + ((right - left) >> 1)

        # drill down
        self.__helper(nums, left, mid, tmp, indexes, res)
        self.__helper(nums, mid + 1, right, tmp, indexes, res)

        # 两边已经排好序了
        if nums[indexes[mid]] <= nums[indexes[mid + 1]]:
            return
        # 否则做归并排序中的归并
        self.__sort_and_count_smaller(nums, left, mid, right, tmp,
                                      indexes, res)

    def __sort_and_count_smaller(self, nums, left, mid, right, tmp, indexes,
                                 res):
        # [r, mid]前有序数组
        # [mid+1, r]后有序数组
        # 先拷贝，再合并
        for i in range(left, right + 1):
            tmp[i] = indexes[i]

        l = left
        r = mid + 1
        for i in range(left, right + 1):
            # 如果l用完了，就拼命使用r
            # [1,2,3,4],[5,6,7,8]
            if l > mid:
                indexes[i] = tmp[r]
                r += 1

            # 如果r用完了，就拼命使用l
            # [5,6,7,8],[1,2,3,4]
            elif r > right:
                indexes[i] = tmp[l]
                l += 1
                # 注意：此时前面剩下的数，比后面所有的数都大
                res[indexes[i]] += (right - mid)
            elif nums[tmp[l]] <= nums[tmp[r]]:
                # [3,5,7,9],[4,6,8,10]
                indexes[i] = tmp[l]
                l += 1
                # 注意
                res[indexes[i]] += (r - mid - 1)
            else:
                # assert arr[tmp[m]] > arr[tmp[row]]
                # 上面两种情况只在其中一种统计就可以了
                # [3,5,7,9],[4,6,8,10]
                indexes[i] = tmp[r]
                r += 1


# 时间复杂度：O(nlogn)
# 空间复杂度：O(m)


# 树状数组解法
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        class FenwickTree:
            def __init__(self, n):
                self.size = n
                self.tree = [0 for _ in range(n + 1)]

            def __lowbit(self, index):
                return index & (-index)

            # 单点更新：将 index 这个位置 + 1
            def update(self, index, delta):
                # 从下到上，最多到 mask，可以等于 mask
                while index <= self.size:
                    self.tree[index] += delta
                    index += self.__lowbit(index)

            # 区间查询：查询小于等于 index 的元素个数
            # 查询的语义是"前缀和"
            def query(self, index):
                res = 0
                # 从上到下，最少到 1，可以等于 1
                while index > 0:
                    res += self.tree[index]
                    index -= self.__lowbit(index)
                return res

        # 特判
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]

        # 去重，方便离散化
        s = list(set(nums))

        s_len = len(s)

        # 离散化，借助堆
        import heapq
        heapq.heapify(s)

        rank_map = dict()
        rank = 1
        for _ in range(s_len):
            num = heapq.heappop(s)
            rank_map[num] = rank
            rank += 1

        fenwick_tree = FenwickTree(s_len)

        # 从后向前填表
        res = [None for _ in range(size)]
        # 从后向前填表
        for index in range(size - 1, -1, -1):
            # 1、查询排名
            rank = rank_map[nums[index]]
            # 2、在树状数组排名的那个位置 + 1
            fenwick_tree.update(rank, 1)
            # 3、查询一下小于等于“当前排名 - 1”的元素有多少
            res[index] = fenwick_tree.query(rank - 1)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, \
                       len(nums), []
        BITree = [0] * (N + 1)

        def update(i):
            while i <= N:
                BITree[i] += 1
                i += (i & -i)

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s

        for x in reversed(nums):
            res += getSum(rank[x] - 1),
            print((getSum(rank[x] - 1),))
            print(res)
            update(rank[x])
        return res[::-1]


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {val: i + 1 for i, val in enumerate(sorted(nums))}
        n = len(nums)
        res = []

        BITree = [0] * (n + 1)

        def update(i, k=1):
            while i <= n:
                BITree[i] += k
                i += (i & -i)

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s

        for x in reversed(nums):
            res.append(getSum(rank[x] - 1))
            update(rank[x])
        return res[::-1]


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {val: i + 1 for i, val in enumerate(sorted(nums))}
        n = len(nums)
        res = []

        BITree = [0] * (n + 1)

        def update(i, k=1):
            while i <= n:
                BITree[i] += k
                i += i & -i

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= i & -i
            return s

        for num in reversed(nums):
            res.append(getSum(rank[num] - 1))
            update(rank[num])

        return res[::-1]


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {val: i + 1 for i, val in enumerate(sorted(nums))}
        size = len(nums)
        BITree = [0] * (size + 1)

        def update(i, k=1):
            while i <= size:
                BITree[i] += k
                i += i & -i

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= i & -i
            return s

        res = []
        for num in reversed(nums):
            res.append(getSum(rank[num] - 1))
            update(rank[num])
        return res[::-1]


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {val: i + 1 for i, val in enumerate(sorted(nums))}
        size = len(nums)
        BITree = [0] * (size + 1)

        def update(i, k=1):
            while i <= size:
                BITree[i] += k
                i += i & -i

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= i & -i
            return s

        res = []
        for n in reversed(nums):
            update(rank[n])
            res.append(getSum(rank[n] - 1))
        return res[::-1]


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {val: i + 1 for i, val in enumerate(sorted(nums))}
        n = len(nums)
        BITree = [0] * (n + 1)

        def update(i, k=1):
            while i <= n:
                BITree[i] += k
                i += i & -i

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= i & -i
            return s

        res = []
        for num in reversed(nums):
            res.append(getSum(rank[num] - 1))
            update(rank[num])
        return res[::-1]


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {val: i + 1 for i, val in enumerate(sorted(nums))}
        n = len(nums)
        BITree = [0] * (n + 1)

        def update(i, k=1):
            while i <= n:
                BITree[i] += k
                i += i & -i

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= i & -i
            return s

        res = []
        for num in reversed(nums):
            res.append(getSum(rank[num] - 1))
            update(rank[num])
        return res[::-1]


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {val: i + 1 for i, val in enumerate(sorted(nums))}
        n = len(nums)
        BITree = [0] * (n + 1)

        def update(i, k=1):
            while i <= n:
                BITree[i] += k
                i += i & -i

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= i & -i
            return s

        res = []
        for num in reversed(nums):
            res.append(getSum(rank[num] - 1))
            update(rank[num])
        return res[::-1]


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {val: i + 1 for i, val in enumerate(sorted(nums))}
        n = len(nums)
        BITree = [0] * (n + 1)

        def update(i, k=1):
            while i <= n:
                BITree[i] += k
                i += i & -i

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= i & -i
            return s

        res = []
        for num in reversed(nums):
            res.append(getSum(rank[num] - 1))
            update(rank[num])
        return res[::-1]


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {val: i + 1 for i, val in enumerate(sorted(nums))}
        n = len(nums)
        BITree = [0] * (n + 1)

        def update(i, k=1):
            while i <= n:
                BITree[i] += k
                i += i & -i

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= i & -i
            return s

        res = []
        for num in reversed(nums):
            res.append(getSum(rank[num] - 1))
            update(rank[num])
        return res[::-1]


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {val: i + 1 for i, val in enumerate(sorted(nums))}
        n = len(nums)
        BITree = [0] * (n + 1)

        def update(i, k=1):
            while i <= n:
                BITree[i] += k
                i += i & -i

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= i & -i
            return s

        res = []
        for num in reversed(nums):
            res.append(getSum(rank[num] - 1))
            update(rank[num])
        return res[::-1]


def main():
    solution = Solution()

    nums = [5, 2, 6, 1]
    result = solution.countSmaller(nums)
    print(result)

    nums = [5, 5, 4, 4]
    result = solution.countSmaller(nums)
    print(result)

    nums = [-1, -1]
    result = solution.countSmaller(nums)
    print(result)


if __name__ == '__main__':
    main()
