# 378. 有序矩阵中第K小的元素.py
import heapq
from typing import List


# 思路
# 矩阵每行每列按升序排列

# 暴力
# 优先队列
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        li = [e for row in matrix for e in row]
        heap = [-e for e in li[:k]]
        heapq.heapify(heap)
        for i in range(k, len(li)):
            if li[i] < -heap[0]:
                heapq.heappushpop(heap, -li[i])
        return -heap[0]


# 二分查找
# 1.找出二维矩阵中最小的数left，最大的数right，那么第k小的数必定在left~right之间
# 2.mid=(r+r) / 2；在二维矩阵中寻找小于等于mid的元素个数count
# 3.若这个count小于k，表明第k小的数在右半部分且不包含mid，
# 即left=mid+1, r=r，又保证了第k小的数在left~right之间
# 4.若这个count大于k，表明第k小的数在左半部分且可能包含mid，
# 即left=r, r=mid，又保证了第k小的数在left~right之间
# 5.因为每次循环中都保证了第k小的数在left~right之间，当left==right时，第k小的数即被找出，等于right
#
# 注意：这里的left mid right是数值，不是索引位置。
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        left = matrix[0][0]
        right = matrix[row - 1][col - 1]
        while left < right:
            # 每次循环都保证第K小的数在start~end之间，当start==end，第k小的数就是start
            mid = left + (right - left) // 2
            # 找出二维矩阵中<=mid的元素总个数
            count = self.findNotBiggerThanMid(matrix, mid, row, col)
            if count < k:
                # 第k小的数在右半部分，且不包含mid
                left = mid + 1
            else:
                # 第k小的数在左半部分，可能包含mid
                right = mid
        return right

    def findNotBiggerThanMid(self, matrix, mid, row, col):
        # 以列为单位找，找到每一列最后一个<=mid的数即知道每一列有多少个数<=mid
        i = row - 1
        j = 0
        count = 0
        while i >= 0 and j < col:
            if matrix[i][j] <= mid:
                # 第j列有i+1个元素<=mid
                count += i + 1
                j += 1
            else:
                # 第j列目前的数大于mid，需要继续在当前列往上找
                i -= 1
        return count


# 以下为自我练习
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            for e in row:
                if len(heap) == k:
                    if e < -heap[0]:
                        heapq.heappushpop(heap, -e)
                else:
                    heapq.heappush(heap, -e)
        return -heap[0]


# 对数做二分查找
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]
        while left < right:
            mid = left + ((right - left) >> 1)
            if self.findNotBiggerThanMid(matrix, mid, n) < k:
                left = mid + 1
            else:
                right = mid
        return left

    def findNotBiggerThanMid(self, matrix, mid, n):
        i, j, count = n - 1, 0, 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                count += i + 1
                j += 1
            else:
                i -= 1
        return count


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[n - 1][n - 1]
        while left < right:
            mid = left + ((right - left) >> 1)
            if self.findNotNBiggerThanMid(matrix, mid, n) < k:
                left = mid + 1
            else:
                right = mid
        return left

    def findNotNBiggerThanMid(self, matrix, mid, n):
        i, j, count = n - 1, 0, 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                count += i + 1
                j += 1
            else:
                i -= 1
        return count


# 第一种方法，变成一维数组，对所有的数做直接排序，这个一维数组的第k个数就是答案
# 时间复杂度 O(n^2logn)
# 空间复杂度：一维数组存这个矩阵O(n^2)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # sum(iterable[, start])语法，
        # iterable -- 可迭代对象，如：列表、元组、集合。
        # start -- 指定相加的参数，如果没有设置这个值，默认为0。
        rec = sorted(sum(matrix, []))
        return rec[k - 1]


# 第二种方法，堆，小顶堆，先将第1列放进去，pop（k-1)次，每次将pop元素的右侧元素放入
# 因为只有这个元素有可能比堆中所有元素小，pop元素的上方和左侧元素一定都被pop出去了
# 在元素的8个相邻方向上，只有左下和右上的元素与该元素的相对关系无法确定
# 而从左侧的一列遍历，左下的元素已经被考虑过了，唯一可能比当前堆顶元素小的，就是pop元素的右边
# 所以每次pop之后 ，push这个已经pop出去的元素右方元素
# 时间复杂度：O(klogn)
# 空间：堆占用了一列的元素O(n)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
        return heapq.heappop(pq)[0]


# 第三种方法，利用这个矩阵的性质，只有斜着方向（左下、右上方向的元素无法确定相对大小）
# 我们可以在O(n)时间复杂度内找到任何一个元素在矩阵的元素中有多少不大于它，或者小于它
# 我们首先初始化计数器为0，用指针i, j（行列）指向左下角，
# 如果比该元素大，count += start + 1， j += 1 (跳到下一列）
# 因为测试元素比这个元素大，比这个元素的下方元素小，它一定比这个元素的右下方的元素小，
# 而与这个元素右边的元素的相对大小未知
# 否则i -= 1 ，跳到下一行，下一行中可能找到一个比测试元素小的元素
# 循环条件是 while start >= 0 and j < w
# 这就启示我们可以用二分法
# 最小值为左上角，最大值为右下角
# 每次O(n)时间找到不大于中点元素的个数，比如说是i
# 如果小于k，那么中点元素（如果在矩阵中）是第i小元素，比k小，目标元素一定比mid大
# 如果大于等于k，那么可能从第k到最后第i个都相等，且都等于mid，这时mid就是目标元素，
# 当然也有可能mid比第k和元素大，所以两边收敛的时候要将右侧收敛到mid
# r = mid + 1
# r = mid
# 由于我们的中点每次取的是偏左的那个，假如l到r之间是偶数个，这样一定会收敛
# 比如right = r + 1
# mid = r
# 更新之后要么
# r = mid + 1 = r + 1 = r
# 要么
# r = mid = r
# 都会达到循环终止条件
# 试想中点每次取的都是右边那个，这时假如
# r = r + 1
# mid = r
# 更新之后要么
# r = mid + 1 = r + 1，这时会收敛
# 要么
# r = mid = r，这时永远不会达到终止条件
# 什么时候会走到right = mid呢
# 当小于右侧元素的矩阵元素一直大于等于k的时候
# 所以我们在写二分的时候注意，r = mid + 1, r = mid是可以收敛的
# 时间复杂度：二分法是O(r-l)的，二分法内部查找是O(n)，总共是O(nlog(r-l))
# 空间复杂度：O(1)，没用到额外空间
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n - 1][n - 1]
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if self.findNotBiggerThanMid(matrix, mid, n) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def findNotBiggerThanMid(self, matrix, mid, n):
        i, j = n - 1, 0
        count = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                count += i + 1
                j += 1
            else:
                i -= 1
        return count


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n - 1][n - 1]
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            count = self._count(matrix, n, mid)
            if count < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def _count(self, matrix, n, mid):
        i, j = n - 1, 0
        c = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                c += i + 1
                j += 1
            else:
                i -= 1
        return c


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n - 1][n - 1]
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if self.count(matrix, n, mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def count(self, matrix, n, mid):
        c = 0
        i, j = n - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                c += i + 1
                j += 1
            else:
                i -= 1
        return c


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n - 1][n - 1]
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if self.count(mid, matrix, n) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def count(self, t, matrix, n):
        i, j = n - 1, 0
        c = 0
        while i >= 0 and j < n:
            if t >= matrix[i][j]:
                c += i + 1
                j += 1
            else:
                i -= 1
        return c


def main():
    sol = Solution()

    matrix = [
        [1, 2],
        [1, 3]
    ]
    k = 3
    res = sol.kthSmallest(matrix, k)
    print(res)
    assert res == 2

    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    res = sol.kthSmallest(matrix, k)
    print(res)


if __name__ == '__main__':
    main()
