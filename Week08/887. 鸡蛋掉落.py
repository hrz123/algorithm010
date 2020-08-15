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


# f(i, j)还剩i个鸡蛋，k层楼，最少需要的次数
# 距离f(2, 100) 2个鸡蛋100层楼
# 选了25层，碎了，没碎
#        max(f(i-1, k-1) , f(i, j-k))
# f(i, j) = min(max(f(i-1, k-1), f(i, j-k))) + 1 for k in 1..j
# 初始化和边界条件
# f(i,1) = 1,一层只需要一次，只要鸡蛋数大于等于1
# f(1,j) = j,一个鸡蛋只能从最低层一个一个实验
# 层数加上一个哨兵0，这样访问索引即是层数，并且当k等于1时，递推到f(i, 0)为0
# 在一层碎了，f(i, 0) = 0
# 返回值，f(K,N)
# 优化复杂度
# 我们的k不用从1开始，随着j的增加，最合适的k层也是在增加的，对于每一个i，我们都重新开始计k
# 在这一轮中，k从上一次最佳开始，最佳的时候f(i-1, k-1) >= f(i, j-k)
# 我们取f(i-1, k-1)，更新f(i, j) = f(i-1,k-1)+1
# 可降低时间复杂度为O(KN)
# 空间复杂度，我们可以使用两个数组滚动
# 一个代表i-1个鸡蛋时，一个表示i个鸡蛋时
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = list(range(N + 1))
        ndp = [0] * (N + 1)
        for i in range(2, K + 1):
            k = 1
            for j in range(1, N + 1):
                while k <= j and dp[k - 1] < ndp[j - k]:
                    k += 1
                ndp[j] = dp[k - 1] + 1
            dp, ndp = ndp, dp
        return dp[N]


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = list(range(N + 1))
        ndp = [0] * (N + 1)
        for i in range(2, K + 1):
            k = 1
            for j in range(1, N + 1):
                while k <= j and dp[k - 1] < ndp[j - k]:
                    k += 1
                ndp[j] = dp[k - 1] + 1
            dp, ndp = ndp, dp
        return dp[N]


# 定义子问题
# 还剩i个鸡蛋，j层楼要检测，一定找到，最少需要多少次
# f(i,j)
# 示例， 100层 25楼 碎了       没碎
# f(i, j) = max(f(i-1, k-1), f(i, j-k)) + 1, 取这些的最小值
# 初始化
# f(1, j) = j,一个鸡蛋只能一个一个试
# f(i, 0) = 0, 0层楼不用试
# 返回值
# f(i, j)
# 优化复杂度
# 我们需要i-1和i两个数组来回滚动
# 时间上，我们不需要每次从1开始求k
# 随着j的递增，k也是在递增的，我们对于i这个鸡蛋数的这一轮，只需要记住k就好
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = list(range(N + 1))
        ndp = [0 for _ in range(N + 1)]
        for i in range(2, K + 1):
            k = 1
            for j in range(1, N + 1):
                while k <= j and dp[k - 1] < ndp[j - k]:
                    k += 1
                ndp[j] = dp[k - 1] + 1
            dp, ndp = ndp, dp
        return dp[N]


# 定义子问题
# f(i,j)为i个鸡蛋，j层楼我们最少需要试多少次
# 100层 25层
# f(i, j) = max(f(i-1, k-1), f(i, j-k)) + 1
# 初始化
# f(1, j) = j
# f(i, 0) = 0
# 返回值f(K,N)
# 优化复杂度
# 我们需要两个数组来回滚动
# 我们不需要每次从1开始找k
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = list(range(N + 1))
        ndp = [0] * (N + 1)
        for i in range(2, K + 1):
            k = 1
            for j in range(1, N + 1):
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
