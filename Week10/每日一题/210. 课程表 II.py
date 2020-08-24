# 210. 课程表 II.py
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses, prerequisites):
        dic = {i: set() for i in range(numCourses)}
        neigh = defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        # queue stores the courses which have no prerequisites
        queue = deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []


class Solution:
    def findOrder(self, numCourses, prerequisites):
        dic = defaultdict(set)
        neigh = defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in range(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        # 入度图
        dic = defaultdict(set)
        # 出度图
        neigh = defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        # 将没有入度的加入栈中
        stack = [i for i in range(numCourses) if not dic[i]]
        res = []
        while stack:
            # 随机拿出一个没有入度的顶点
            node = stack.pop()
            # 加入到结果集当中
            res.append(node)
            # 遍历它的出度点
            for i in neigh[node]:
                # 对于它的出度点，删除它们的node的入度
                dic[i].remove(node)
                # 如果删除之后，该顶点没有入度了，我们就将它加入到栈中
                if not dic[i]:
                    stack.append(i)
            # 将node从入度图中删掉
            dic.pop(node)
        return res if not dic else []


class Solution:
    def findOrder(self, numCourses, prerequisites):
        dic = defaultdict(set)
        neigh = defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            dic[j].add(i)
        queue = deque([i for i in dic if not dic[i]])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if len(res) == numCourses else []


class Solution:
    def findOrder(self, numCourses, prerequisites):
        neigh = defaultdict(list)
        in_degree = [0] * numCourses
        for i, j in prerequisites:
            neigh[j].append(i)
            in_degree[i] += 1
        queue = deque([i for i in range(numCourses) if not in_degree[i]])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for i in neigh[node]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
        return res if len(res) == numCourses else []


class Solution:
    def findOrder(self, numCourses, prerequisites):
        in_degree = [0] * numCourses
        neigh = defaultdict(list)
        for i, j in prerequisites:
            neigh[j].append(i)
            in_degree[i] += 1
        stack = [i for i in range(numCourses) if not in_degree[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    stack.append(i)
        return res if len(res) == numCourses else []


class Solution:
    def findOrder(self, numCourses, prerequisites):
        neigh = defaultdict(list)
        in_degree = [0] * numCourses
        for i, j in prerequisites:
            neigh[j].append(i)
            in_degree[i] += 1
        stack = [i for i in range(numCourses) if in_degree[i] == 0]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    stack.append(i)
        return res if len(res) == numCourses else []


class Solution:
    def findOrder(self, numCourses, prerequisites):
        neigh = defaultdict(list)
        in_degree = [0] * numCourses
        for i, j in prerequisites:
            neigh[j].append(i)
            in_degree[i] += 1
        stack = [i for i in range(numCourses) if in_degree[i] == 0]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for j in neigh[node]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    stack.append(j)
        return res if len(res) == numCourses else []


def main():
    pass


if __name__ == '__main__':
    main()
