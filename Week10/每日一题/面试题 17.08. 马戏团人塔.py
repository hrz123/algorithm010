# 面试题 17.08. 马戏团人塔.py
import bisect
from typing import List


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        zv = list(zip(height, weight))
        zv.sort(key=lambda x: [x[0], -x[1]])
        stack = []
        for _, w in zv:
            if not stack or w > stack[-1]:
                stack.append(w)
            loc = bisect.bisect_left(stack, w)
            stack[loc] = w
        return len(stack)


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        dp = []
        for a, b in sorted(zip(height, weight), key=lambda x: [x[0], -x[1]]):
            pos = bisect.bisect_left(dp, b)
            dp[pos:pos + 1] = [b]
        return len(dp)


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        stack = []
        for a, b in sorted(zip(height, weight), key=lambda x: [x[0], -x[1]]):
            loc = bisect.bisect_left(stack, b)
            stack[loc:loc + 1] = [b]
        return len(stack)


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        stack = []
        for h, w in sorted(zip(height, weight), key=lambda x: [x[0], -x[1]]):
            loc = bisect.bisect_left(stack, w)
            stack[loc:loc + 1] = [w]
        return len(stack)


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        stack = []
        for a, b in sorted(zip(height, weight), key=lambda x: [x[0], -x[1]]):
            loc = bisect.bisect_left(stack, b)
            stack[loc:loc + 1] = [b]
        return len(stack)


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        stack = []
        for a, b in sorted(zip(height, weight), key=lambda x: [x[0], -x[1]]):
            loc = bisect.bisect_left(stack, b)
            stack[loc:loc + 1] = [b]
        return len(stack)


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        stack = []
        for a, b in sorted(zip(height, weight), key=lambda x: [x[0], -x[1]]):
            loc = bisect.bisect_left(stack, b)
            stack[loc:loc + 1] = [b]
        return len(stack)


def main():
    pass


if __name__ == '__main__':
    main()
