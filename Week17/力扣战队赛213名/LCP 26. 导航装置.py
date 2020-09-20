# LCP 26. 导航装置.py


# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def navigation(self, root):
        G = []

        def dfs(root, pre):
            if not root:
                return
            while root.val >= len(G):
                G.append(set())
            if pre:
                G[root.val].add(pre)
                G[pre].add(root.val)
            dfs(root.left, root.val)
            dfs(root.right, root.val)

        dfs(root, 0)

        for a in range(len(G)):
            if len(G[a]) == 2:
                b, c = list(G[a])
                G[b].remove(a)
                G[c].remove(a)
                G[b].add(c)
                G[c].add(b)
                G[a] = set()
        count = collections.Counter()

        res = 0
        for a in range(len(G)):
            if len(G[a]) == 1:
                pa = G[a].pop()
                count[pa] += 1
                if count[pa] > 1:
                    res += 1
        return max(res, 1)


def main():
    pass


if __name__ == '__main__':
    main()
