# 973. 最接近原点的 K 个点.py
import heapq
import random
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = [(a * a + b * b, a, b) for a, b in points]
        heapq.heapify(heap)
        res = []
        for _ in range(K):
            _, a, b = heapq.heappop(heap)
            res.append([a, b])
        return res


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        l, r = 0, len(points) - 1
        while l <= r:
            pivot = self.partition(points, l, r)
            if pivot == K - 1:
                return points[:K]
            if pivot < K - 1:
                l = pivot + 1
            else:
                r = pivot - 1

    def partition(self, points, l, r):
        ran = random.randint(l, r)
        points[r], points[ran] = points[ran], points[r]
        pivot = r
        right = l
        dist_p = points[pivot][0] ** 2 + points[pivot][1] ** 2
        for i in range(l, r):
            dist_i = points[i][0] ** 2 + points[i][1] ** 2
            if dist_i <= dist_p:
                points[i], points[right] = points[right], points[i]
                right += 1
        points[right], points[pivot] = points[pivot], points[right]
        return right


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        l, r = 0, len(points) - 1
        while l <= r:
            pivot = self.partition(points, l, r)
            if pivot == K - 1:
                return points[:K]
            if pivot > K - 1:
                r = pivot - 1
            else:
                l = pivot + 1

    def partition(self, points, l, r):
        ran = random.randint(l, r)
        points[ran], points[r] = points[r], points[ran]
        pivot = r
        right = l
        pv = points[pivot][0] ** 2 + points[pivot][1] ** 2
        for i in range(l, r):
            if points[i][0] ** 2 + points[i][1] ** 2 <= pv:
                points[i], points[right] = points[right], points[i]
                right += 1
        points[right], points[pivot] = points[pivot], points[right]
        return right


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        l, r = 0, len(points) - 1
        while l <= r:
            pivot = self.partition(points, l, r)
            if pivot == K - 1:
                return points[:K]
            if pivot > K - 1:
                r = pivot - 1
            else:
                l = pivot + 1

    def partition(self, points, l, r):
        ran = random.randint(l, r)
        points[r], points[ran] = points[ran], points[r]
        pivot = r
        right = l
        pv = points[pivot][0] ** 2 + points[pivot][1] ** 2
        for i in range(l, r):
            if points[i][0] ** 2 + points[i][1] ** 2 <= pv:
                points[i], points[right] = points[right], points[i]
                right += 1
        points[right], points[pivot] = points[pivot], points[right]
        return right


def main():
    sol = Solution()

    nums = [[1, 3], [-2, 2]]
    k = 1
    res = sol.kClosest(nums, k)
    print(res)

    nums = [[-5, 4], [-6, -5], [4, 6]]
    k = 2
    res = sol.kClosest(nums, k)
    print(res)


if __name__ == '__main__':
    main()
