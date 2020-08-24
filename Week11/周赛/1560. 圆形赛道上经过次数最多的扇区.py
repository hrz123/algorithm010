# 1560. 圆形赛道上经过次数最多的扇区.py
from collections import defaultdict
from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        counter = defaultdict(int)
        start = rounds[0]
        for nxt in rounds[1:]:
            if nxt < start:
                for i in range(start, n + 1):
                    counter[i] += 1
                for i in range(1, nxt + 1):
                    counter[i] += 1
            else:
                for i in range(start, nxt + 1):
                    counter[i] += 1
            start = nxt + 1
        max_count = max(counter.values())
        res = []
        for c in counter:
            if counter[c] == max_count:
                res.append(c)
        res.sort()
        return res


def main():
    pass


if __name__ == '__main__':
    main()
