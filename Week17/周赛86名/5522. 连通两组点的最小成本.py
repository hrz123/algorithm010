# 5522. 连通两组点的最小成本.py
from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:

        ans = [float('inf')]

        n, m = len(cost), len(cost[0])

        def argmin(a):
            minv, mini = float('inf'), -1
            for i, v in enumerate(a):
                if v < minv:
                    minv = v
                    mini = i

            return mini

        mina = [argmin(x) for x in cost]
        minb = [argmin(x) for x in
                [[cost[r][c] for r in range(n)] for c in range(m)]]

        def dfs(index, vis, pre):
            if index >= n:
                if len(vis) == m:
                    ans[0] = min(ans[0], pre)
                else:
                    for i in range(m):
                        if i not in vis:
                            j = minb[i]
                            pre += cost[j][i]
                    ans[0] = min(ans[0], pre)
                return

            if pre > ans[0]:
                return

            x = [(cost[index][i], i) for i in range(m)]
            x.sort()
            for c, i in x:
                dfs(index + 1, vis | {i}, pre + c)

        dfs(0, set(), 0)

        return ans[0]


def main():
    sol = Solution()
    cost = [[15, 96],
            [36, 2]]
    res = sol.connectTwoGroups(cost)
    print(res)
    cost = [[1, 3, 5],
            [4, 1, 1],
            [1, 5, 3]]
    res = sol.connectTwoGroups(cost)
    print(res)
    cost = [[25, 60, 37, 24],
            [2, 30, 29, 63],
            [8, 76, 58, 76],
            [12, 43, 50, 72],
            [100, 77, 83, 34],
            [24, 0, 51, 74],
            [2, 28, 49, 35],
            [62, 38, 56, 55],
            [55, 43, 26, 33],
            [91, 54, 24, 18],
            [59, 97, 55, 38],
            [16, 80, 56, 7]]
    res = sol.connectTwoGroups(cost)
    print(res)

    cost = [[44, 91, 93, 34, 50], [100, 92, 72, 86, 24], [72, 62, 91, 74, 19],
            [37, 64, 9, 16, 13], [99, 55, 23, 21, 16], [34, 34, 14, 70, 49],
            [99, 44, 13, 86, 38], [32, 74, 97, 24, 3], [97, 7, 24, 37, 78],
            [8, 29, 40, 13, 51], [94, 12, 53, 52, 80], [53, 93, 55, 66, 45]]
    res = sol.connectTwoGroups(cost)
    print(res)

    cost = [[67, 78, 95, 100, 45, 90, 7], [30, 46, 36, 42, 41, 71, 44],
            [86, 20, 35, 63, 0, 48, 7], [16, 38, 99, 42, 74, 59, 81],
            [29, 13, 83, 45, 18, 15, 21], [17, 28, 71, 64, 32, 46, 71],
            [43, 61, 73, 85, 37, 94, 87], [99, 91, 47, 41, 50, 1, 32],
            [26, 54, 29, 38, 91, 78, 56], [64, 23, 59, 23, 42, 79, 37],
            [31, 70, 70, 23, 41, 22, 66], [10, 30, 30, 3, 53, 79, 18]]
    res = sol.connectTwoGroups(cost)
    print(res)


if __name__ == '__main__':
    main()
