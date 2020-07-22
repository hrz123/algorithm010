# 647. 回文子串.py


# 回文串有三种方法
# 表格法dp
# 中间扩散法
# 马拉车法

# 中间扩散法
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        res = 0
        # 有2n-1个可扩散位置
        for i in range(2 * n - 1):
            # 如果中间位置是缝隙
            if i & 1:
                l = (i - 1) >> 1
                r = l + 1
                while l >= 0 and r < n and s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
            # 如果中间是字母
            else:
                # 本身就是
                res += 1
                l = (i >> 1) - 1
                r = l + 2
                while l >= 0 and r < n and s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
        return res


# 时间复杂度：最坏O(N^2)
# 空间复杂度：O(1)


# 表格法dp
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j, -1, -1):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
        return res


# 时间复杂度：O(N^2)，填表格
# 空间复杂度：需要O(N^2)的额外空间递推

# 时间复杂度
# 回文子串都可以采取从中间向两边扩散的写法
# 可扩散的位置有2n-1个
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(2 * n - 1):
            idx = i >> 1
            l, r = idx, idx + 1
            if i & 1:
                res = self.update_res(l, n, r, res, s)
            else:
                res += 1
                l -= 1
                res = self.update_res(l, n, r, res, s)
        return res

    def update_res(self, l, n, r, res, s):
        while l >= 0 and r < n and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res


# dp的方法
# 回文子串的dp一般是矩形对角线
# 定义子问题
# dp(i, j)是不是回文子串，包括i和j的位置
# 定义状态数组
# dp(i, j)是不是回文子串，取决于dp(i+1, j-1)是不是回文子串，且s[i] = s[j]
# 递推方程
# dp(i, j) = dp(i+1, j-1) if s[i] == s[j]
# dp(i, j) = False        else
# 初始化
# dp(i, i) = True
# dp(i，i+1) = s[i] == s[i+1]
# 返回值 sum(f(i, j)) if j >= i
# 空间优化
# 可以只使用对角线元素，然后结果数组累加
# 但是至少需要两层对角线元素
# 但是写起来比较麻烦，不建议这样写，可以第一遍用矩阵第二遍优化
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(1, n):
            dp[i][i - 1] = True
        res = n
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    res += 1
        return res


# 极简写法的dp
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        for gap in range(n):
            for i in range(n - gap):
                j = i + gap
                if s[i] == s[j] and (gap <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
        return res


def main():
    sol = Solution()

    s = "abc"
    res = sol.countSubstrings(s)
    print(res)

    s = "aaa"
    res = sol.countSubstrings(s)
    print(res)

    s = "aba"
    res = sol.countSubstrings(s)
    print(res)


if __name__ == '__main__':
    main()
