# 4.py
from heapq import heappush, heappop
from typing import List


class Solution:
    def busiestServers(self, ks: int, a: List[int], d: List[int]) -> List[int]:
        from sortedcontainers import SortedList
        ans = [0] * ks
        pq = []
        fu = SortedList(range(ks))
        v = 0
        for i, j in zip(a, d):
            heappush(pq, [i, 1, i + j, v])
            v += 1
        # print(pq,fu)
        while pq:
            i, k, j, num = heappop(pq)
            if k == 1 and fu:
                v = fu.bisect_left(num % ks)
                if v == len(fu):
                    v = 0
                v = fu[v]
                fu.remove(v)
                ans[v] += 1
                heappush(pq, [j, 0, v, num])
            elif k == 0:
                fu.add(j)
            # print(pq,fu)
        # print(ans)
        t = max(ans)
        return [i for i in range(ks) if ans[i] == t]


def main():
    sol = Solution()
    k = 3
    arrival = [1, 2, 3, 4, 5]
    load = [5, 2, 3, 3, 3]
    res = sol.busiestServers(k, arrival, load)
    print(res)

    k = 32820
    arrival = [*range(1, 100001)]
    load = [1] * 100000
    res = sol.busiestServers(k, arrival, load)
    print(res)


if __name__ == '__main__':
    main()
