# 796. 旋转字符串.py


# 1. 穷举法
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        n = len(A)
        if n == 0:
            return True
        for i in range(n):
            if all(A[(i + j) % n] == B[j] for j in range(n)):
                return True
        return False


# 时间复杂度：O(n^2), n为字符串长度
# 空间复杂度：O(n)，临时字符串都等于A的大小


# 2. 判断子串
# A+A包含了所有可以通过旋转操作从A得到的字符串，因此我们只需要判断B是否为A+A的子串
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and (A + A).find(B) != -1


# 方法三：Rabin-Karp 字符串哈希
# 先计算出A[0:N], A[1:N+1]等的哈希，如果哈希与B相同，再判断
# 求哈希值时因为是连续求，所以第一步算出hash值是O(N)的，之后都是O(1)的操作
# 时间O(n)
# 空间O(n)

# 方法四：KMP 算法
# 判断一个串是否为另一个串的子串的最优时间复杂度的算法是 KMP 算法。
# 和方法二相同，我们只需要用 KMP 算法判断 B 是否为 A + A 的子串即可。KMP
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        N = len(A)
        if N != len(B):
            return False
        if N == 0:
            return True

        # Compute shift table
        shifts = [1] * (N + 1)
        left = -1
        for right in range(N):
            while left >= 0 and B[left] != B[right]:
                left -= shifts[left]
            shifts[right + 1] = right - left
            left += 1

        # Find match of B in A+A
        match_len = 0
        for char in A + A:
            while match_len >= 0 and B[match_len] != char:
                match_len -= shifts[match_len]

            match_len += 1
            if match_len == N:
                return True

        return False


# 时间O(n)
# 空间O(n)

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        N = len(A)
        if N != len(B):
            return False
        if N == 0:
            return True

        lps = self.get_lps(B, N)
        j = 0
        A += A
        for i in range(N * 2):
            while j != 0 and A[i] != B[j]:
                j = lps[j - 1] + 1
            if A[i] == B[j]:
                j += 1
            if j == N:
                return True
        return False

    def get_lps(self, p, m):
        lps = [-1] * m
        k = -1
        for i in range(1, m):
            while k != -1 and p[i] != p[k + 1]:
                k = lps[k]
            if p[i] == p[k + 1]:
                k += 1
            lps[i] = k
        return lps


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        return (A + A).find(B) != -1


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and (A + A).find(B) != -1


def main():
    sol = Solution()
    A = 'abcde'
    B = 'cdeab'
    res = sol.rotateString(A, B)
    print(res)

    A = ''
    B = ''
    res = sol.rotateString(A, B)
    print(res)


if __name__ == '__main__':
    main()
