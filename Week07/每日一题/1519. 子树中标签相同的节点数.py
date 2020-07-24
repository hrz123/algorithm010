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


def main():
    sol = Solution()

    n = 7
    edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    labels = "abaedcd"
    res = sol.countSubTrees(n, edges, labels)
    print(res)


if __name__ == '__main__':
    main()
