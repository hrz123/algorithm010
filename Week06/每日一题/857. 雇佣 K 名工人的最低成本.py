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


def main():
    quality = [10, 20, 5]
    wage = [70, 50, 30]
    K = 2
    sol = Solution()
    res = sol.mincostToHireWorkers(quality, wage, K)
    print(res)

    quality = [3, 1, 10, 10, 1]
    wage = [4, 8, 2, 2, 7]
    K = 3
    res = sol.mincostToHireWorkers(quality, wage, K)
    print(res)


if __name__ == '__main__':
    main()
