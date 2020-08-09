# 887. 鸡蛋掉落.py
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = list(range(N + 1))
        _dp = [0] * (N + 1)
        for _ in range(K - 1):
            for j in range(1, N + 1):
                _dp[j] = 1 + min(max(dp[k - 1], _dp[j - k])
                                 for k in range(1, j + 1))
            dp, _dp = _dp, dp
        return dp[N]


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[float('inf')] * (N + 1) for _ in range(K + 1)]
        for i in range(1, K + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N + 1):
            dp[1][j] = j

        for i in range(2, K + 1):
            for j in range(2, N + 1):
                for k in range(1, j + 1):
                    dp[i][j] = min(dp[i][j],
                                   1 + max(dp[i - 1][k - 1], dp[i][j - k]))
        return dp[K][N]


# 时间复杂度：O(kn^2)
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        def dfs(i, j):
            if i == 1:
                return j
            if j == 0:
                return 0
            if j == 1:
                return 1
            if (i, j) in d:
                return d[i, j]
            lo, hi = 0, j
            while lo < hi:
                mid = lo + ((hi - lo) >> 1)
                left, right = dfs(i - 1, mid - 1), dfs(i, j - mid)
                if left < right:
                    lo = mid + 1
                else:
                    hi = mid
            res = 1 + max(dfs(i - 1, lo - 1), dfs(i, j - lo))
            d[i, j] = res
            return res

        d = {}
        return dfs(K, N)


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[float('inf')] * (N + 1) for _ in range(K + 1)]
        for i in range(1, K + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N + 1):
            dp[1][j] = j

        for i in range(2, K + 1):
            k = 1
            for j in range(2, N + 1):
                while k < j + 1 and dp[i][j - k] > dp[i - 1][k - 1]:
                    k += 1
                dp[i][j] = 1 + dp[i - 1][k - 1]
        return dp[K][N]


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = range(N + 1)
        for i in range(2, K + 1):
            k = 1
            ndp = [0, 1] + [float('inf')] * (N - 1)
            for j in range(2, N + 1):
                while k < j + 1 and ndp[j - k] > dp[k - 1]:
                    k += 1
                ndp[j] = 1 + dp[k - 1]
            dp = ndp
        return dp[N]


# 以下为自我练习
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = range(N + 1)
        for i in range(2, K + 1):
            ndp = [0, 1] + [0] * (N - 1)
            k = 1
            for j in range(2, N + 1):
                while k < j + 1 and dp[k - 1] < ndp[j - k]:
                    k += 1
                ndp[j] = 1 + dp[k - 1]
            dp = ndp
        return dp[N]


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = list(range(N + 1))
        ndp = [0, 1] + [0] * (N - 1)
        for i in range(2, K + 1):
            k = 1
            for j in range(2, N + 1):
                while k < j + 1 and dp[k - 1] < ndp[j - k]:
                    k += 1
                ndp[j] = 1 + dp[k - 1]
            dp, ndp = ndp, dp
        return dp[N]


# 定义子问题
# f(i, j)还剩i个鸡蛋还剩j层楼测试，我们最少用多少次
# f(i, j)  随便找一层 k
#          碎了           没碎
#          max(f(i-1, k-1),f(i, j-k)) + 1
# 我们要取这些里面的最小值
#
# f(i, j) = min(max(f(i-1, k-1)   f(i, j-k)) + 1) k 1..j
# 初始化和边界条件
# f(1, j) = j
# f(i, 1) = 1
# k能选择的层数在1到j之间
# 返回值
# f(K,N)
# 优化空间复杂度
# 只和i-1和比j小的有关
# 我们可以只用两个j规模的数组
# 时间复杂度：O(K*N^2)
# 特殊优化
# 注意到最佳的k值随着j的增加而增加
# 我们可以记住k的值，在这一鸡蛋个数中重用
# 这样K最多从0到j，我们整体的时间复杂度下降到了
# O(K*N)
# 开始的时候f(i-1,k-1)都是小于f(i, n-k)的
# 到它们开始相等的时候，两者之间求max是最小的
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = list(range(N + 1))
        ndp = [0, 1] + [0] * (N - 1)
        for i in range(2, K + 1):
            k = 1
            for j in range(2, N + 1):
                while k <= j and dp[k - 1] < ndp[j - k]:
                    k += 1
                ndp[j] = dp[k - 1] + 1
            dp, ndp = ndp, dp
        return dp[N]


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = list(range(N + 1))
        ndp = [0, 1] + [0] * (N - 1)
        for i in range(2, K + 1):
            k = 1
            for j in range(2, N + 1):
                while k <= j and dp[k - 1] < ndp[j - k]:
                    k += 1
                ndp[j] = dp[k - 1] + 1
            dp, ndp = ndp, dp
        return dp[N]


def main():
    sol = Solution()

    K = 2
    N = 10000
    res = sol.superEggDrop(K, N)
    print(res)
    # 141

    K = 2
    N = 1
    res = sol.superEggDrop(K, N)
    print(res)
    # 1


if __name__ == '__main__':
    main()
