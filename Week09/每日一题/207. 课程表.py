# 207. 课程表.py
from collections import defaultdict
from collections import deque
from functools import lru_cache
from typing import List


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        edge_map = defaultdict(list)
        for p in prerequisites:
            edge_map[p[0]].append(p[1])

        @lru_cache(None)
        def dfs(i):
            if i == numCourses:
                return True
            for k in range(numCourses):
                if k not in visited:
                    flag = True
                    for pre in edge_map[k]:
                        if pre not in visited:
                            flag = False
                            break
                    visited.add(k)
                    if flag and dfs(i + 1):
                        return True
                    visited.remove(k)
            return False

        for i in range(numCourses):
            if not edge_map[i]:
                visited = {i}
                if dfs(1):
                    return True
        return False


# 本题可约化为： 课程安排图是否是 有向无环图(DAG)。
# 即课程间规定了前置条件，但不能构成任何环路，否则课程前置条件将不成立。
# 思路是通过 拓扑排序 判断此课程安排图是否是 有向无环图(DAG) 。
# 拓扑排序原理： 对 DAG 的顶点进行排序，使得对每一条有向边 (u,v)，
# 均有 u（在排序记录中）比 v 先出现。
# 亦可理解为对某点 v 而言，只有当 v 的所有源点均出现了，v 才能出现。
# 通过课程前置条件列表 prerequisites 可以得到课程安排图的 邻接表 adjacency，
# 以降低算法时间复杂度，以下两种方法都会用到邻接表。

# 1.统计课程安排图中弄每个节点的入度，生成入度表indegrees
# 2.借助一个队列queue，将所有入度为0的节点入队。
# 3.当queue非空时，依次将队首节点出队，在课程安排图中删除此节点pre：
#    并不是真正从邻接表中删除此节点pre，而是将此节点对应所有邻接节点cur的入度-1
#    即indegrees[cur] -= 1.
#    当入度-1后邻接节点cur的入度为0，说明cur所有的前驱节点已经被"删除"，此时将cur入队。
# 4.在每次pre出队时，执行numCourses--;
#    若整个课程安排图是有向无环图（即可以安排），则所有节点一定都入队并出队过，即完成拓扑排序。
#    换个角度说，若课程安排图中存在环，一定有节点的入度始终不为0。
#    因此，拓扑排序出队次数等于课程个数，返回numCourses==0判断课程是否可以成功安排
# 时间复杂度 O(N+M)： 遍历一个图需要访问所有节点和所有临边，N 和 M 分别为节点数量和临边数量；
# 空间复杂度 O(N+M)： 为建立邻接表所需额外空间，adjacency 长度为 N ，并存储 M 条临边的数据。
class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)
        # BFS TopSort.
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses


# 原理是通过DFS判断图中是否有环
# 算法流程
# 1.借助一个标志列表flags，用于判断每个节点i（课程）的状态：
#    1.未被DFS访问：start==0
#    2.已被其他节点启动的DFS访问：start==-1
#    3.已被当前节点启动的DFS访问：start==1。
# 2.对numCourses个节点一次执行DFS，判断每个节点起步DFS是否存在换，若存在直接放回False
#    DFS流程
#    1.终止条件：
#      当flag[start] == -1，说明当前访问节点已被其他节点启动的DFS访问，
#      无需再重复搜索，直接返回True
#      当flag[start] == 1，说明在本轮DFS搜索中节点i被第2次访问，即课程安排图有环，直接返回False
#    2.将当前访问节点i对应flag[start]置1，即标记其本轮被DFS访问过；
#    3.递归访问当前节点i的所有邻接节点j，当发现环直接返回False；
#    4.当前节点所有邻接节点已被遍历，并没有发现环，则将当前节点flag置为-1并返回True
# 3.若整个图DFS结束并未发现环，返回True
class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False
        return True


# 以下为自我练习
class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacent = [[] for _ in range(numCourses)]
        deq = deque()

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacent[pre].append(cur)

        for i in range(len(indegrees)):
            if not indegrees[i]:
                deq.append(i)

        while deq:
            pre = deq.popleft()
            numCourses -= 1
            for cur in adjacent[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    deq.append(cur)

        return not numCourses


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for nxt in adjacency[i]:
                if not dfs(nxt, adjacency, flags):
                    return False
            flags[i] = -1
            return True

        flags = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        flags = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)

        def dfs(i, adjacency, flags):
            if flags[i] == 1:
                return False
            if flags[i] == -1:
                return True
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False
            flags[i] = -1
            return True

        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        flags = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)

        def dfs(i, adjacency, flags):
            if flags[i] == 1:
                return False
            if flags[i] == -1:
                return True
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False
            flags[i] = -1
            return True

        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        edge_map = defaultdict(list)
        for e in prerequisites:
            edge_map[e[1]].append(e[0])
        flags = [0] * numCourses

        def dfs(i):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for n in edge_map[i]:
                if not dfs(n):
                    return False
            flags[i] = -1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        flags = [0] * numCourses
        edge_map = defaultdict(list)
        for e in prerequisites:
            edge_map[e[1]].append(e[0])

        def dfs(i):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in edge_map[i]:
                if not dfs(j):
                    return False
            flags[i] = -1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        flags = [0] * numCourses
        edge_map = defaultdict(list)
        for e in prerequisites:
            edge_map[e[1]].append(e[0])

        def dfs(i):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in edge_map:
                if not dfs(j):
                    return False
            flags[i] = -1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        edge_map = defaultdict(list)
        for e in prerequisites:
            edge_map[e[1]].append(e[0])
        flags = [0] * numCourses

        def dfs(i):
            if flags[i] == 1:
                return False
            if flags[i] == -1:
                return True
            flags[i] = 1
            for j in edge_map[i]:
                if not dfs(j):
                    return False
            flags[i] = -1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        edge_map = defaultdict(list)
        for e in prerequisites:
            edge_map[e[1]].append(e[0])
        flags = [0] * numCourses

        def dfs(i):
            if flags[i] == 1:
                return False
            if flags[i] == -1:
                return True
            flags[i] = 1
            for j in edge_map[i]:
                if not dfs(j):
                    return False
            flags[i] = -1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        edge_map = defaultdict(list)
        for e in prerequisites:
            edge_map[e[1]].append(e[0])
        flags = [0] * numCourses

        def dfs(i):
            if flags[i] == 1:
                return False
            if flags[i] == -1:
                return True
            flags[i] = 1
            for j in edge_map[i]:
                if not dfs(j):
                    return False
            flags[i] = -1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        flags = [0] * numCourses
        neigh = defaultdict(list)
        for i, j in prerequisites:
            neigh[j].append(i)

        def dfs(i):
            if flags[i] == 1:
                return False
            if flags[i] == -1:
                return True
            flags[i] = 1
            for j in neigh[i]:
                if not dfs(j):
                    return False
            flags[i] = -1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        flags = [0] * numCourses
        neigh = defaultdict(list)
        for i, j in prerequisites:
            neigh[j].append(i)

        def dfs(i):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in neigh[i]:
                if not dfs(j):
                    return False
            flags[i] = -1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            if flags[i] == 1:
                return False
            if flags[i] == -1:
                return True
            flags[i] = 1
            for j in neigh[i]:
                if not dfs(j):
                    return False
            flags[i] = -1
            return True

        flags = [0] * numCourses
        neigh = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            neigh[j].append(i)
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


class Solution:
    def canFinish(self, n: int,
                  prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            if flags[i] == 1:
                return False
            if flags[i] == -1:
                return True
            flags[i] = 1
            for j in neigh[i]:
                if not dfs(j):
                    return False
            flags[i] = -1
            return True

        neigh = defaultdict(list)
        for x, y in prerequisites:
            neigh[y].append(x)
        flags = [0] * n
        for i in range(n):
            if not dfs(i):
                return False
        return True


def main():
    sol = Solution()

    n = 2
    p = [[1, 0]]
    res = sol.canFinish(n, p)
    print(res)

    n = 2
    p = [[1, 0], [0, 1]]
    res = sol.canFinish(n, p)
    print(res)


if __name__ == '__main__':
    main()
