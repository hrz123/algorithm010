# 332. 重新安排行程.py
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)  # 邻接表
        for f, t in tickets:
            d[f].append(t)  # 路径存进邻接表
        for f in d:
            d[f].sort()  # 邻接表排序
        ans = []

        def dfs(f):  # 深搜函数
            while d[f]:
                dfs(d[f].pop(0))  # 路径检索
            ans.insert(0, f)  # 放在最前

        dfs('JFK')
        return ans


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(f):
            while d[f]:
                dfs(d[f].pop())
            ans.append(f)

        d = defaultdict(list)
        for f, t in tickets:
            d[f].append(t)
        for f in d:
            d[f].sort(reverse=True)
        ans = []
        dfs('JFK')
        return ans[::-1]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(f):
            while neigh[f]:
                dfs(heapq.heappop(neigh[f]))
            res.append(f)

        neigh = defaultdict(list)
        for f, t, in tickets:
            neigh[f].append(t)
        for f in neigh:
            heapq.heapify(neigh[f])
        res = []
        dfs("JFK")
        return res[::-1]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        neigh = defaultdict(list)
        for f, t, in tickets:
            neigh[f].append(t)
        for f in neigh:
            heapq.heapify(neigh[f])
        stack = ["JFK"]
        res = []
        while stack:
            while neigh[stack[-1]]:
                stack.append(heapq.heappop(neigh[stack[-1]]))
            res.append(stack.pop())
        return res[::-1]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        neigh = defaultdict(list)
        for f, t in tickets:
            neigh[f].append(t)
        for f in neigh:
            heapq.heapify(neigh[f])
        stack = ["JFK"]
        res = []
        while stack:
            while neigh[stack[-1]]:
                stack.append(heapq.heappop(neigh[stack[-1]]))
            res.append(stack.pop())
        return res[::-1]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(f):
            while neigh[f]:
                dfs(heapq.heappop(neigh[f]))
            res.append(f)

        neigh = defaultdict(list)
        for f, t in tickets:
            neigh[f].append(t)
        for f in neigh:
            heapq.heapify(neigh[f])
        res = []
        dfs("JFK")
        return res[::-1]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        neigh = defaultdict(list)
        for f, t in tickets:
            neigh[f].append(t)
        for f in neigh:
            heapq.heapify(neigh[f])
        stack = ["JFK"]
        res = []
        while stack:
            while neigh[stack[-1]]:
                stack.append(heapq.heappop(neigh[stack[-1]]))
            res.append(stack.pop())
        return res[::-1]


def main():
    sol = Solution()

    li = [["JFK", "SFO"]]
    res = sol.findItinerary(li)
    print(res)

    li = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"],
          ["ATL", "SFO"]]
    res = sol.findItinerary(li)
    print(res)

    li = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"],
          ["ATL", "SFO"]]
    res = sol.findItinerary(li)
    print(res)


if __name__ == '__main__':
    main()
