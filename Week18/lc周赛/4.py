# 4.py
import collections
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def legal(code):
            cnt = collections.defaultdict(int)
            total = 0
            for i, (L, R) in enumerate(requests):
                if (1 << i) & code:
                    cnt[L] += 1
                    cnt[R] -= 1
                    total += 1
            if any(cnt.values()):
                return 0
            else:
                return total

        return max(legal(code) for code in range((1 << len(requests))))


def main():
    sol = Solution()
    # n = 5
    # requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]
    # res = sol.maximumRequests(n, requests)
    # print(res)

    n = 3
    requests = [[2, 2], [2, 0], [1, 1], [2, 1], [1, 1], [2, 2], [1, 0], [0, 2],
                [1, 2]]
    res = sol.maximumRequests(n, requests)
    print(res)

    # n = 4
    # requests = [[0, 0], [1, 3], [1, 3], [2, 3], [1, 0], [2, 2], [1, 2], [2, 1],
    #             [1, 3],
    #             [0, 2], [3, 0], [3, 1], [2, 2], [3, 0], [0, 3], [3, 1]]
    # res = sol.maximumRequests(n, requests)
    # print(res)


if __name__ == '__main__':
    main()
