# 857. 雇佣 K 名工人的最低成本.py
import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int],
                             K: int) -> float:

        v = list(zip(quality, wage))

        v.sort(key=lambda t: t[1] / t[0])
        priority_queue = []
        ans = float('inf')
        total = 0

        for q, w in v:
            total += q
            heapq.heappush(priority_queue, -q)
            if len(priority_queue) > K:
                total += heapq.heappop(priority_queue)
            if len(priority_queue) == K:
                ans = min(ans, total * w / q)

        return ans


# 给工资的钱取决于两点，与最大的工资质量比成正比，这些人的质量总和成正比
# 我们要同时减小这两个元素
# 我们沿着工资质量比，和这些人总体的质量这条曲线的边界，找最小值
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int],
                             K: int) -> float:
        v = list(zip(quality, wage))
        v.sort(key=lambda e: e[1] / e[0])
        heap = []
        res = float('inf')
        _sum_q = 0
        for q, w in v:
            _sum_q += q
            heapq.heappush(heap, -q)
            if len(heap) == K:
                res = min(res, _sum_q * w / q)
                _sum_q += heapq.heappop(heap)
        return res


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int],
                             K: int) -> float:
        zv = list(zip(quality, wage))
        zv.sort(key=lambda x: x[1] / x[0])
        heap = []
        res = float('inf')
        q_sum = 0
        for q, w in zv:
            q_sum += q
            heapq.heappush(heap, -q)
            if len(heap) == K:
                res = min(res, q_sum * w / q)
                q_sum += heapq.heappop(heap)
        return res


def main():
    sol = Solution()

    quality = [10, 20, 5]
    wage = [70, 50, 30]
    K = 2
    res = sol.mincostToHireWorkers(quality, wage, K)
    print(res)

    quality = [3, 1, 10, 10, 1]
    wage = [4, 8, 2, 2, 7]
    K = 3
    res = sol.mincostToHireWorkers(quality, wage, K)
    print(res)


if __name__ == '__main__':
    main()
