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

def main():
    s = "abc"
    sol = Solution()
    res = sol.countSubstrings(s)
    print(res)

    s = "aaa"
    res = sol.countSubstrings(s)
    print(res)


if __name__ == '__main__':
    main()
