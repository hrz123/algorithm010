# 4.py
import bisect
import heapq
from typing import List


class TreeSet(object):
    """
    Binary-tree set like java Treeset.
    Duplicate elements will not be added.
    When added new element, TreeSet will be sorted automatically.
    """

    def __init__(self, elements):
        self._treeset = []
        self.addAll(elements)

    def addAll(self, elements):
        for element in elements:
            if element in self: continue
            self.add(element)

    def add(self, element):
        if element not in self:
            bisect.insort(self._treeset, element)

    def ceiling_index(self, e, exclusive=False):
        index = bisect.bisect_right(self._treeset, e)
        if exclusive:
            return index
        if index > 0 and self[index - 1] == e:
            return index - 1
        return index

    def floor_index(self, e, exclusive=False):
        index = bisect.bisect_left(self._treeset, e)
        if exclusive:
            return index - 1
        if index < len(self) and self[index] == e:
            return index
        return index - 1

    def ceiling(self, e, exclusive=False):
        index = self.ceiling_index(e, exclusive)
        if 0 <= index < len(self):
            return self[index]
        return None

    def floor(self, e, exclusive=False):
        index = self.floor_index(e, exclusive)
        if 0 <= index < len(self):
            return self[index]
        return None

    def __getitem__(self, num):
        return self._treeset[num]

    def __len__(self):
        return len(self._treeset)

    def clear(self):
        """
        Delete all elements in TreeSet.
        """
        self._treeset = []

    def clone(self):
        """
        Return shallow copy of self.
        """
        return TreeSet(self._treeset)

    def remove(self, element):
        """
        Remove element if element in TreeSet.
        """
        try:
            self._treeset.remove(element)
        except ValueError:
            return False
        return True

    def __iter__(self):
        """
        Do ascending iteration for TreeSet
        """
        for element in self._treeset:
            yield element

    def pop(self, index):
        return self._treeset.pop(index)

    def __str__(self):
        return str(self._treeset)

    def __eq__(self, target):
        if isinstance(target, TreeSet):
            return self._treeset == target.treeset
        elif isinstance(target, list):
            return self._treeset == target

    def __contains__(self, e):
        """
        Fast attribution judgment by bisect
        """
        try:
            return e == self._treeset[bisect.bisect_left(self._treeset, e)]
        except:
            return False


class Solution:
    def busiestServers(self, k: int, arrival: List[int],
                       load: List[int]) -> List[int]:
        count = [0 for _ in range(k)]
        ts = TreeSet(list(range(k)))
        h = []
        for i, a in enumerate(arrival):
            l = load[i]
            while h and h[0][0] <= a:
                ts.add(h[0][1])
                heapq.heappop(h)
            idx = i % k
            t = ts.ceiling(idx)
            if t is None:
                t = ts.ceiling(-1)
            if t is not None:
                ts.remove(t)
                heapq.heappush(h, (a + l, t))
                count[t] += 1
        m = max(count)
        return [i for i, c in enumerate(count) if c == m]


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
