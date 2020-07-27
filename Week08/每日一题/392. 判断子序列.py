# 392. 判断子序列.py


# 定义两个指针，i, j指向s和t的开头，
# 如果s[i] == t[j]
# i += 1 j += 1
# 如果不相等
# j+= 1
# 如果最终i == len(s)，就返回True
# 如果最终j 走到了最后也没有，j == len(t) 就返回False
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        m, n = len(s), len(t)
        i = j = 0

        while j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
            if i == m:
                return True
        return False


# 时间复杂度O(n)


# 匹配一串需要O(n)， n为t的长度。有大量的s的话，每次都要O(n)，是很耗时的
# 我们可以预处理一下t，使得对于s的每一个字符，直接就能找到下一个字符存在还是不存在，
# 存在的话在哪里
# 因为仅包含小写字母，我们可以用一个 n * 26的数组存储当前字符的下一个a-z的字符的位置
# 不存在就用-1表示，并且可以在第一位添加一个位置 (n+1)* 26的数组，
# 第一个位置存下一个a-z字符的位置
# 这样s的第一个字符就可以O(1)的时间找到了
# 建立这个数组的时候，我们考虑
# f(i,j) = f(i+1, j) if a[i+1] != chr(j)
#        = i+1       else
# 初始化
# f(n, j) = -1

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = " " + t
        n = len(t)
        dp = [[0] * 26 for _ in range(n)]
        a = ord('a')

        for j in range(26):
            p = -1
            for i in range(n - 1, -1, -1):
                dp[i][j] = p
                if t[i] == chr(a + j):
                    p = i
        start = 0
        for c in s:
            if dp[start][ord(c) - a] == -1:
                return False
            start = dp[start][ord(c) - a]
        return True


def main():
    sol = Solution()

    s = "abc"
    t = "ahbgdc"
    res = sol.isSubsequence(s, t)
    print(res)

    s = "axc"
    t = "ahbgdc"
    res = sol.isSubsequence(s, t)
    print(res)


if __name__ == '__main__':
    main()
