# 93. 复原IP地址.py
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def dfs(i, k, pre):
            if i == n and k == 4:
                res.append(pre[:-1])
                return
            if k > 4:
                return
            for j in range(1, 4):
                if i + j <= n and 0 <= int(s[i:i + j]) <= 255:
                    if j != 1 and s[i] == '0':
                        continue
                    dfs(i + j, k + 1, pre + s[i:i + j] + '.')

        dfs(0, 0, '')

        return res


# 以下为自我练习
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def dfs(i, j, pre):
            if i >= n or j >= 4:
                if i == n and j == 4:
                    res.append(pre[:-1])
                return
            for k in range(1, 4):
                if i + k <= n and 0 <= int(s[i:i + k]) <= 255:
                    if s[i] == '0' and k != 1:
                        continue
                    dfs(i + k, j + 1, pre + s[i:i + k] + '.')

        dfs(0, 0, "")
        return res


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def dfs(i, k, pre):
            if i == n and k == 4:
                res.append(pre)
                return
            for j in range(i, min(i + 3, n)):
                if int(s[i:j + 1]) <= 255 and (j == i or s[i] != '0'):
                    if k == 3:
                        dfs(j + 1, k + 1, pre + s[i:j + 1])
                    elif k < 3:
                        dfs(j + 1, k + 1, pre + s[i:j + 1] + '.')

        dfs(0, 0, '')
        return res


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def dfs(i, k, pre):
            if i == n and k == 4:
                res.append(pre)
                return
            for j in range(i, min(i + 3, n)):
                if int(s[i:j + 1]) <= 255 and (j == i or s[i] != '0'):
                    if k < 3:
                        dfs(j + 1, k + 1, pre + s[i:j + 1] + '.')
                    if k == 3:
                        dfs(j + 1, k + 1, pre + s[i:j + 1])

        dfs(0, 0, '')
        return res


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def dfs(i, k, pre):
            if i == n and k == 4:
                res.append(pre)
                return
            for j in range(i + 1, min(i + 3, n) + 1):
                if int(s[i:j]) <= 255 and (j == i + 1 or s[i] != '0'):
                    if k == 3:
                        dfs(j, 4, pre + s[i:j])
                    elif k < 3:
                        dfs(j, k + 1, pre + s[i:j] + '.')

        dfs(0, 0, '')
        return res


def main():
    sol = Solution()
    s = "25525511135"
    res = sol.restoreIpAddresses(s)
    print(res)

    s = "0000"
    res = sol.restoreIpAddresses(s)
    print(res)


if __name__ == '__main__':
    main()
