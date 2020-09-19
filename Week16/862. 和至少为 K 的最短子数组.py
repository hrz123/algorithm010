# 862. 和至少为 K 的最短子数组.py
import collections
from typing import List


class Solution(object):
    def shortestSubarray(self, A, K):
        n = len(A)
        pre = [0]
        for x in A:
            pre.append(pre[-1] + x)

        # Want smallest y-x with Py - Px >= K
        ans = n + 1  # N+1 is impossible
        monoq = collections.deque()  # opt(y) candidates, represented as indices of P
        for y, py in enumerate(pre):
            # Want opt(y) = largest x with Px <= Py - K
            while monoq and py <= pre[monoq[-1]]:
                monoq.pop()

            while monoq and py - pre[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < n + 1 else -1


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        pre = [0]
        for a in A:
            pre.append(pre[-1] + a)
        # want smallest y-x with Py - Px >= K
        ans = n + 1  # n + 1 is impossible
        deq = collections.deque()
        for y, py in enumerate(pre):
            while deq and py <= pre[deq[-1]]:
                deq.pop()
            while deq and py - pre[deq[0]] >= K:
                ans = min(ans, y - deq.popleft())
            deq.append(y)
        return -1 if ans == n + 1 else ans


def main():
    pass


if __name__ == '__main__':
    main()
