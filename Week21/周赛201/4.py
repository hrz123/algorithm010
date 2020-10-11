# 4.py


class Solution(object):

    def countSubgraphsForEachDiameter(self, n, edges):
        G = [[] for _ in range(n)]
        for i, j in edges:
            G[i - 1].append(j - 1)
            G[j - 1].append(i - 1)

        def maxd(mask0):
            res = 0
            for i in range(n):
                if (1 << i) & mask0:
                    mask = mask0
                    bfs, bfs2 = [i], []
                    cur = 0
                    while bfs:
                        for i in bfs:
                            mask ^= 1 << i
                            for j in G[i]:
                                if mask & (1 << j):
                                    bfs2.append(j)
                        cur += 1
                        bfs, bfs2 = bfs2, []
                    if mask:
                        return 0
                    res = max(res, cur - 1)
            return res

        res = [0] * (n - 1)
        for mask in range(1 << n):
            if mask & (mask - 1) == 0:
                continue
            d = maxd(mask)
            if d:
                res[d - 1] += 1

        return res


def main():
    pass


if __name__ == '__main__':
    main()
