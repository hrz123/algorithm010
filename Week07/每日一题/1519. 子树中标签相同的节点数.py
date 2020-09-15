# 1519. 子树中标签相同的节点数.py
from collections import defaultdict, Counter
from typing import List


# 用edges构造节点指向字典，用以表示有方向的边，然后，从0开始进行深度搜索。
# 当遍历到一个节点时，递归遍历它的所有子节点，然后整合从子节点传上来的字符统计数据，再加上当前节点的字符，就可以得到字符数了。
# 遍历时要去重，去重方式有两种，一种是定义全局visited；一种是定义pre节点。


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> \
            List[int]:
        # 邻接表
        edge_map = defaultdict(list)
        for edge in edges:
            edge_map[edge[0]].append(edge[1])
            edge_map[edge[1]].append(edge[0])

        def _dfs(i):
            visited.add(i)
            # 字符数字典
            data = Counter({labels[i]: 1})
            for nxt in edge_map[i]:
                if nxt in visited:
                    continue  # 去重
                # 整合子树的字符数
                data += _dfs(nxt)
            # 设置当前节点的结果字符数
            ans[i] = data[labels[i]]
            return data

        visited = set()
        ans = [1] * n
        _dfs(0)
        return ans


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> \
            List[int]:

        edge_map = defaultdict(list)
        for edge in edges:
            edge_map[edge[0]].append(edge[1])
            edge_map[edge[1]].append(edge[0])

        def _dfs(i, pre):
            # 字符数字典
            data = Counter({labels[i]: 1})
            for nxt in edge_map[i]:
                if nxt == pre:  # 去重
                    continue
                # 整合子树的字符数
                data += _dfs(nxt, i)

            # 设置当前节点的结果字符数
            ans[i] = data[labels[i]]
            return data

        ans = [1] * n
        _dfs(0, 0)
        return ans


# 以下为自我练习
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> \
            List[int]:
        edge_map = defaultdict(list)

        for edge in edges:
            edge_map[edge[0]].append(edge[1])
            edge_map[edge[1]].append(edge[0])

        def _dfs(i, pre):
            # 字符数字典
            data = Counter({labels[i]: 1})
            for nxt in edge_map[i]:
                if nxt != pre:
                    # 更新字符数字典
                    data += _dfs(nxt, i)
            ans[i] = data[labels[i]]
            return data

        ans = [1] * n
        _dfs(0, 0)
        return ans


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> \
            List[int]:
        edge_map = defaultdict(list)
        for e in edges:
            edge_map[e[0]].append(e[1])
            edge_map[e[1]].append(e[0])

        ans = [1] * n

        def dfs(i, pre):
            data = Counter({labels[i]: 1})
            for nxt in edge_map[i]:
                if nxt != pre:
                    data += dfs(nxt, i)
            ans[i] = data[labels[i]]
            return data

        dfs(0, 0)
        return ans


# 定义一个子函数
# 这个函数计算每一个节点为根的子树，所有标记的计数
# 因为用邻接表表示的边，我们为了防止边的重复访问，需要记录访问节点
# 因为没有环，所以我们只要记住前一个节点，在访问下一个节点的相邻节点的时候
# 不访问这个节点就可以了
# 参数为dfs(start, pre)， i就是这个节点的编号，pre就是前一个节点的编号
# 终止条件就是这个点的相邻节点都访问过了
# 这样我们在全局的一个数组变量中，更新相应的i的值即可
# 最后我们返回这个数组变量就是所求
# 利用了python中Counter有加法的api
# 我们可以简化代码
# 否则我们如果用字典，我们要遍历字典，把存在于本层的加上，不存在于本层的添加进来即可
# 稍微麻烦点
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> \
            List[int]:
        edge_map = defaultdict(list)
        for e in edges:
            edge_map[e[0]].append(e[1])
            edge_map[e[1]].append(e[0])
        ans = [1] * n

        def dfs(i, pre):
            data = {labels[i]: 1}
            for nxt in edge_map[i]:
                if nxt != pre:
                    for k, v in dfs(nxt, i).items():
                        if k == labels[i]:
                            data[k] += v
                        else:
                            data[k] = v
            ans[i] = data[labels[i]]
            return data

        dfs(0, None)
        return ans


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> \
            List[int]:
        edge_map = defaultdict(list)
        for e in edges:
            edge_map[e[0]].append(e[1])
            edge_map[e[1]].append(e[0])
        ans = [1] * n

        def dfs(i, pre):
            data = Counter({labels[i]: 1})
            for nxt in edge_map[i]:
                if nxt != pre:
                    data += dfs(nxt, i)
            ans[i] = data[labels[i]]
            return data

        dfs(0, None)
        return ans


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) \
            -> List[int]:
        edge_list = defaultdict(list)
        for e in edges:
            edge_list[e[0]].append(e[1])
            edge_list[e[1]].append(e[0])
        ans = [1] * n

        def dfs(i, pre):
            data = Counter({labels[i]: 1})
            for nxt in edge_list[i]:
                if nxt != pre:
                    data += dfs(nxt, i)
            ans[i] = data[labels[i]]
            return data

        dfs(0, None)
        return ans


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) \
            -> List[int]:
        edge_list = defaultdict(list)
        for e in edges:
            edge_list[e[0]].append(e[1])
            edge_list[e[1]].append(e[0])
        ans = [1] * n

        def dfs(i, pre):
            data = {labels[i]: 1}
            for nxt in edge_list[i]:
                if nxt != pre:
                    for k, v in dfs(nxt, i).items():
                        data[k] = data.get(k, 0) + v
            ans[i] = data[labels[i]]
            return data

        dfs(0, None)
        return ans


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) \
            -> List[int]:
        edge_map = defaultdict(list)
        for e in edges:
            edge_map[e[0]].append(e[1])
            edge_map[e[1]].append(e[0])
        ans = [1] * n

        def dfs(i, pre):
            data = {labels[i]: 1}
            for j in edge_map[i]:
                if j != pre:
                    for k, v in dfs(j, i).items():
                        data[k] = data.get(k, 0) + v
            ans[i] = data[labels[i]]
            return data

        dfs(0, None)
        return ans


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]],
                      labels: str) -> List[int]:
        edge_map = defaultdict(list)
        for e in edges:
            edge_map[e[1]].append(e[0])
            edge_map[e[0]].append(e[1])
        ans = [1] * n

        def dfs(i, pre):
            data = {labels[i]: 1}
            for j in edge_map[i]:
                if j != pre:
                    for k, v in dfs(j, i).items():
                        if k in data:
                            data[k] += v
                        else:
                            data[k] = v
            ans[i] = data[labels[i]]
            return data

        dfs(0, None)
        return ans


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]],
                      labels: str) -> List[int]:
        def dfs(i, pre):
            data = {labels[i]: 1}
            for nxt in neigh[i]:
                if nxt != pre:
                    for k, v in dfs(nxt, i).items():
                        if k in data:
                            data[k] += v
                        else:
                            data[k] = v
            ans[i] = data[labels[i]]
            return data

        ans = [1] * n
        neigh = defaultdict(list)
        for x, y in edges:
            neigh[x].append(y)
            neigh[y].append(x)
        dfs(0, None)
        return ans


def main():
    sol = Solution()

    n = 7
    edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    labels = "abaedcd"
    res = sol.countSubTrees(n, edges, labels)
    print(res)


if __name__ == '__main__':
    main()
