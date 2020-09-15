# 1091. 二进制矩阵中的最短路径.py
import heapq
from typing import List


# dp的方法
# dp(start,j) = min(dp(_i, _j)) + 1 全部方向 else
# dp(start, j) = max_value if grid[start][j] == 1
# 不好做
# dp(m-1, m-1) = 1
# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         if not grid or not grid[0]:
#             return -1
#         if grid[0][0] or grid[-1][-1]:
#             return -1
#         if m <= 2:
#             return m
#         max_value = float('inf')
#         dp = [[max_value] * m for _ in range(m)]
#
#         dp[m - 1][m - 1] = 1
#
#         for start in range(m - 1, -1, -1):
#             for j in range(m - 1, -1, -1):
#                 if grid[start][j]:
#                     dp[start][j] = max_value
#                 else:
#                     for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1),
#                                    (1, -1), (-1, -1), (-1, 1)):
#                         _i, _j = start + dx, j + dy
#                         if -1 < _i < m and -1 < _j < m:
#                             dp[start][j] = min(dp[start][j])
#         return -1 if dp[0][0] == max_value else dp[0][0]


# bfs
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid or not grid[0]:
            return -1
        if grid[0][0] or grid[-1][-1]:
            return -1
        if n <= 2:
            return n
        bq, eq, nq = {(0, 0)}, {(n - 1, n - 1)}, set()
        pos = set((i, j) for i in range(n) for j in range(n) if not grid[i][j])
        res = 1
        while bq:
            pos -= bq
            res += 1
            for i, j in bq:
                for dx, dy in (
                        (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1),
                        (-1, -1), (-1, 1)):
                    _i, _j = i + dx, j + dy
                    if (_i, _j) in pos:
                        if (_i, _j) in eq:
                            return res
                        nq.add((_i, _j))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


# A*
class PriorityQueue:
    def __init__(self, iterable=[]):
        self.heap = []
        for value in iterable:
            heapq.heappush(self.heap, (0, value))

    def add(self, value, priority=0):
        heapq.heappush(self.heap, (priority, value))

    def pop(self):
        priority, value = heapq.heappop(self.heap)
        return value

    def __len__(self):
        return len(self.heap)


def reconstruct_path(came_from, start, end):
    reverse_path = [end]
    while end != start:
        end = came_from[end]
        reverse_path.append(end)
    return reverse_path[::-1]


def a_star_graph_search(
        start,
        goal_function,
        successor_function,
        heuristic
):
    visited = set()
    came_from = dict()
    distance = {start: 0}
    frontier = PriorityQueue()
    frontier.add(start)
    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        if goal_function(node):
            return reconstruct_path(came_from, start, node)
        visited.add(node)
        for successor in successor_function(node):
            frontier.add(
                successor,
                priority=distance[node] + 1 + heuristic(successor)
            )
            if (successor not in distance
                    or distance[node] + 1 < distance[successor]):
                distance[successor] = distance[node] + 1
                came_from[successor] = node
    return None


def get_goal_function(grid):
    m, n = len(grid), len(grid[0])

    def is_bottom_right(cell):
        return cell == (m - 1, n - 1)

    return is_bottom_right


def get_successor_function(grid):
    m, n = len(grid), len(grid[0])

    def get_clear_adjacent_cells(cell):
        i, j = cell
        res = []
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1),
                       (-1, -1), (-1, 1)):
            _i, _j = i + dx, j + dy
            if -1 < _i < m and -1 < _j < n and grid[_i][_j] == 0:
                res.append((_i, _j))
        return res

    return get_clear_adjacent_cells


def get_heuristic(grid):
    m, n = len(grid), len(grid[0])
    a, b = goal_cell = (m - 1, n - 1)

    def get_clear_path_distance_from_goal(cell):
        (i, j) = cell
        return max(abs(a - i), abs(b - j))

    return get_clear_path_distance_from_goal


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        shortest_path = a_star_graph_search(
            start=(0, 0),
            goal_function=get_goal_function(grid),
            successor_function=get_successor_function(grid),
            heuristic=get_heuristic(grid)
        )
        if shortest_path is None or grid[0][0] == 1:
            return -1
        print(shortest_path)
        return len(shortest_path)


# 以下为自我练习
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return -1
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        if n <= 2:
            return n
        bq, eq, nq, res = {(0, 0)}, {(n - 1, n - 1)}, set(), 1
        pos = set((i, j) for i in range(n) for j in range(n) if not grid[i][j])
        while bq:
            pos -= bq
            res += 1
            for i, j in bq:
                for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1),
                               (1, -1), (-1, -1), (-1, 1)):
                    _i, _j = i + dx, j + dy
                    if (_i, _j) in pos:
                        if (_i, _j) in eq:
                            return res
                        nq.add((_i, _j))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


# 以下为自我练习
# 双向bfs
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 防止起点或终点无法访问到
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        # 防止起点就是终点
        if n == 1:
            return 1
        # 双向bfs所需，从开始的队列，从结尾的队列，下一个队列，记录访问集合
        bq, eq, nq, visited, res = {(0, 0)}, {(n - 1, n - 1)}, set(), set(), 1

        while bq:
            visited |= bq
            res += 1
            for i, j in bq:
                for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1),
                               (1, -1), (-1, -1), (-1, 1)):
                    _i, _j = i + dx, j + dy
                    # 没访问过，且不是障碍
                    if -1 < _i < n and -1 < _j < n \
                            and (_i, _j) not in visited \
                            and not grid[_i][_j]:
                        if (_i, _j) in eq:
                            return res
                        nq.add((_i, _j))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        if n == 1:
            return 1
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1),
                (-1, 1))
        bq, eq, nq, res, visited = {(0, 0)}, {(n - 1, n - 1)}, set(), 0, {
            (0, 0), (n - 1, n - 1)}
        while bq:
            res += 1
            for x, y in bq:
                for dx, dy in dirs:
                    _x, _y = x + dx, y + dy
                    if (_x, _y) in eq:
                        return res + 1
                    if -1 < _x < n and -1 < _y < n \
                            and not grid[_x][_y] \
                            and (_x, _y) not in visited:
                        visited.add((_x, _y))
                        nq.add((_x, _y))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1
        if n == 1:
            return 1
        bq, eq, nq, res = {(0, 0)}, {(n - 1, n - 1)}, set(), 1
        visited = set()
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1),
                (-1, -1))
        while bq:
            visited |= bq
            res += 1
            for x, y in bq:
                for dx, dy in dirs:
                    _x, _y = x + dx, y + dy
                    if -1 < _x < n and -1 < _y < n and (_x, _y) not in visited \
                            and not grid[_x][_y]:
                        if (_x, _y) in eq:
                            return res
                        nq.add((_x, _y))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1
        if n == 1:
            return 1
        bq, eq, nq, res, visited = {(0, 0)}, {(n - 1, n - 1)}, set(), 1, set()
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1),
                (-1, -1))
        while bq:
            visited |= bq
            res += 1
            for x, y in bq:
                for dx, dy in dirs:
                    _x, _y = x + dx, y + dy
                    if -1 < _x < n and -1 < _y < n and (_x, _y) not in visited \
                            and not grid[_x][_y]:
                        if (_x, _y) in eq:
                            return res
                        nq.add((_x, _y))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        if n == 1:
            return 1
        bq, eq, nq, res = {(0, 0)}, {(n - 1, n - 1)}, set(), 1
        visited = set()
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1),
                (-1, -1))
        while bq:
            visited |= bq
            res += 1
            for i, j in bq:
                for di, dj in dirs:
                    _i, _j = i + di, j + dj
                    if -1 < _i < n and -1 < _j < n and (_i, _j) not in \
                            visited and not grid[_i][_j]:
                        if (_i, _j) in eq:
                            return res
                        nq.add((_i, _j))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        if n == 1:
            return 1
        bq, eq, nq, visited, res = {(0, 0)}, {(n - 1, n - 1)}, set(), set(), 1
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1),
                (-1, 1))
        while bq:
            visited |= bq
            res += 1
            for x, y in bq:
                for dx, dy in dirs:
                    _x, _y = x + dx, y + dy
                    if -1 < _x < n and -1 < _y < n and (_x, _y) not in visited \
                            and not grid[_x][_y]:
                        if (_x, _y) in eq:
                            return res
                        nq.add((_x, _y))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        if n == 1:
            return 1
        bq, eq, nq, visited, res = {(0, 0)}, {(n - 1, n - 1)}, set(), set(), 1
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1),
                (-1, 1))
        while bq:
            visited |= bq
            res += 1
            for x, y in bq:
                for dx, dy in dirs:
                    _x, _y = x + dx, y + dy
                    if -1 < _x < n and -1 < _y < n and (_x, _y) not in visited \
                            and not grid[_x][_y]:
                        if (_x, _y) in eq:
                            return res
                        nq.add((_x, _y))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        if n == 1:
            return 1
        bq, eq, nq, visited, res = {(0, 0)}, {(n - 1, n - 1)}, set(), set(), 1
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1),
                (-1, 1))
        while bq:
            visited |= bq
            res += 1
            for x, y in bq:
                for dx, dy in dirs:
                    _x, _y = x + dx, y + dy
                    if -1 < _x < n and -1 < _y < n and grid[_x][_y] == 0:
                        if (_x, _y) not in visited:
                            if (_x, _y) in eq:
                                return res
                            nq.add((_x, _y))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


def main():
    sol = Solution()

    grid = [[0]]
    res = sol.shortestPathBinaryMatrix(grid)
    print(res)
    assert res == 1

    grid = [[0, 1], [1, 0]]
    res = sol.shortestPathBinaryMatrix(grid)
    print(res)

    grid = [[0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 1],
            [0, 0, 1, 0, 0, 0, 0]]
    res = sol.shortestPathBinaryMatrix(grid)
    print(res)

    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 1, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0]]
    res = sol.shortestPathBinaryMatrix(grid)
    print(res)

    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    res = sol.shortestPathBinaryMatrix(grid)
    print(res)


if __name__ == '__main__':
    main()
