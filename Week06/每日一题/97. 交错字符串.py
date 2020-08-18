# 97. 交错字符串.py


# 思路，一次拿掉一个字符，如果s1和s2开头都是这个字符，那么就开分支
from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        @lru_cache(None)
        def dfs(i, j):
            if i == n1 and j == n2:
                return True
            if i == n1:
                return s3[i + j:] == s2[j:]
            if j == n2:
                return s3[i + j:] == s1[i:]
            if s3[i + j] != s1[i] and s3[i + j] != s2[j]:
                return False
            if s3[i + j] == s1[i] and s3[i + j] == s2[j]:
                return dfs(i + 1, j) or dfs(i, j + 1)
            elif s3[i + j] == s1[i]:
                return dfs(i + 1, j)
            return dfs(i, j + 1)

        return dfs(0, 0)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == n1 and j == n2:
                memo[(i, j)] = True
            elif i == n1:
                memo[(i, j)] = s3[i + j:] == s2[j:]
            elif j == n2:
                memo[(i, j)] = s3[i + j:] == s1[i:]
            elif s3[i + j] == s1[i] and s3[i + j] == s2[j]:
                memo[(i, j)] = dfs(i + 1, j) or dfs(i, j + 1)
            elif s3[i + j] == s1[i]:
                memo[(i, j)] = dfs(i + 1, j)
            elif s3[i + j] == s2[j]:
                memo[(i, j)] = dfs(i, j + 1)
            else:
                memo[(i, j)] = False
            return memo[(i, j)]

        return dfs(0, 0)


# 使用dfs
# 递归要找到重复性和终止条件
# dfs(start, j)
# 如果i < l1 and stack1[start] == s3[start+j] dfs(start+1,j)
# 如果j < l2 and stack2[j] == s3[start+j] dfs(start,j+1)
# 如果i == len(stack1)并且 j == len(stack2)时返回true
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False

        def dfs(i, j):
            if i == l1 and j == l2:
                return True
            if (i, j) in memo:
                return memo[i, j]
            if i < l1 and s1[i] == s3[i + j]:
                if dfs(i + 1, j):
                    memo[i, j] = True
                    return True
            if j < l2 and s2[j] == s3[i + j]:
                if dfs(i, j + 1):
                    memo[i, j] = True
                    return True
            memo[i, j] = False
            return False

        return dfs(0, 0)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        memo = set()

        def dfs(i, j):
            if i == m and j == n:
                return True
            if (i, j) in memo:
                return False
            if i < m and s3[i + j] == s1[i]:
                if dfs(i + 1, j):
                    return True
            if j < n and s3[i + j] == s2[j]:
                if dfs(i, j + 1):
                    return True
            memo.add((i, j))
            return False

        return dfs(0, 0)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if len(s3) != m + n:
            return False
        import functools
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m and j == n:
                return True
            if i < m and s3[i + j] == s1[i]:
                if dfs(i + 1, j):
                    return True
            if j < n and s3[i + j] == s2[j]:
                if dfs(i, j + 1):
                    return True
            return False

        return dfs(0, 0)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        memo = {}

        def dfs(i, j):
            if i == m and j == n:
                return True
            if (i, j) in memo:
                return memo[i, j]
            if i < m and s1[i] == s3[i + j]:
                if dfs(i + 1, j):
                    return True
            if j < n and s2[j] == s3[i + j]:
                if dfs(i, j + 1):
                    return True
            memo[i, j] = False
            return False

        return dfs(0, 0)


def main():
    sol = Solution()

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    res = sol.isInterleave(s1, s2, s3)
    print(res)

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    res = sol.isInterleave(s1, s2, s3)
    print(res)

    s1 = ""
    s2 = ""
    s3 = "a"
    res = sol.isInterleave(s1, s2, s3)
    print(res)


if __name__ == '__main__':
    main()
