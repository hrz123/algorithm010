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


def main():
    sol = Solution()
    s = "25525511135"
    res = sol.restoreIpAddresses(s)
    print(res)


if __name__ == '__main__':
    main()
