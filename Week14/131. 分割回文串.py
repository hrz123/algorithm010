# 131. 分割回文串.py
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i, pre):
            if i == n:
                res.append(pre)
                return
            for j in range(i + 1, n + 1):
                if s[i:j] == s[i:j][::-1]:
                    dfs(j, pre + [s[i:j]])

        n = len(s)
        res = []
        dfs(0, [])
        return res


def main():
    pass


if __name__ == '__main__':
    main()
