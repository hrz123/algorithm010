from typing import List


# 600
class Solution:
    def partition(self, s: str) -> List[int]:
        res = []
        n = len(s)

        def dfs(i, pre):
            if i == n:
                res.append(pre[1:])
                return
            for j in range(i + 1, min(i + 3, n) + 1):
                if 0 <= int(s[i:j]) <= 600 and s[i] != '0':
                    dfs(j, pre + '|' + s[i:j])

        dfs(0, "")
        return res


def main():
    sol = Solution()
    res = sol.partition("012034")
    print(res)


if __name__ == '__main__':
    main()
