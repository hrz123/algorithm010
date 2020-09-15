# 841. 钥匙和房间.py
from typing import List


class Solution:
    def canVisitAllRooms(self, neigh: List[List[int]]) -> bool:
        n = len(neigh)
        if n == 1:
            return True
        visited = [True] + [False] * (n - 1)
        target = n - 1
        q, nq = neigh[0], []
        while q:
            for node in q:
                if not visited[node]:
                    visited[node] = True
                    target -= 1
                    nq.extend(neigh[node])
            if target == 0:
                return True
            q, nq = nq, []
        return False


def main():
    pass


if __name__ == '__main__':
    main()
