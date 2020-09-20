# 5520. 拆分字符串使唯一子字符串的数目最大 .py


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        n = len(s)

        def dfs(i):
            if i == n:
                return 0
            res = 1
            for j in range(i + 1, n + 1):
                if s[i:j] not in seen and s[j:] not in seen and s[i:j] != s[j:]:
                    seen.add(s[i:j])
                    res = max(res, 1 + dfs(j))
                    seen.remove(s[i:j])
            return res

        return dfs(0)


def main():
    sol = Solution()
    s = "aa"
    res = sol.maxUniqueSplit(s)
    print(res)


if __name__ == '__main__':
    main()
