# 1514. 概率最大的路径.py
from collections import deque, defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]],
                       succProb: List[float], start: int, end: int) -> float:
        if not edges or not edges[0]:
            return 0

        g = defaultdict(list)
        for i, (s, e) in enumerate(edges):
            g[s].append((e, succProb[i]))
            g[e].append((s, succProb[i]))
        ans = 0
        queue = deque([(start, 1)])
        visited = {start: 0}
        while queue:
            cur_node, cur_prob = queue.popleft()
            for next_node, p in g[cur_node]:
                next_prob = cur_prob * p
                if next_node == end:
                    ans = max(ans, next_prob)
                    continue
                if next_prob > ans and (next_node not in visited or visited[
                    next_node] < next_prob):
                    queue.append((next_node, next_prob))
                    visited[next_node] = next_prob
        return ans


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]],
                       succProb: List[float], start: int, end: int) -> float:
        if not edges or not edges[0]:
            return 0

        # 构造节点邻接表
        st_maps = defaultdict(list)
        for i, (s, e) in enumerate(edges):
            st_maps[s].append((e, succProb[i]))
            st_maps[e].append((s, succProb[i]))

        ans = 0
        queue = deque([(start, 1)])
        visited = {start: 0}
        while queue:
            # 当前节点
            cur_node, cur_prob = queue.popleft()
            for next_node, p in st_maps[cur_node]:
                # 下一个待遍历的节点
                next_prob = cur_prob * p
                if next_node == end:
                    ans = max(ans, next_prob)
                    continue

                # 剪枝和去重：如果下一个待遍历节点的概率大于ans && (该节点为遍历过 或 遍历过该节点但是上次的概率比现在小)
                if next_prob > ans and (next_node not in visited or visited[
                    next_node] < next_prob):
                    visited[next_node] = next_prob
                    queue.append((next_node, next_prob))
        return ans


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]],
                       succProb: List[float], start: int, end: int) -> float:
        if not edges or not edges[0]:
            return 0


def main():
    pass


if __name__ == '__main__':
    main()
