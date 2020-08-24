# 818. 赛车.py
import heapq


# 最短路径算法
class Solution:
    def racecar(self, target):
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = [float('inf')] * ((barrier << 1) + 1)
        dist[target] = 0

        while pq:
            steps, targ = heapq.heappop(pq)
            if dist[targ] > steps:
                continue
            for k in range(K + 1):
                walk = (1 << k) - 1
                steps2, targ2 = steps + k + 1, walk - targ
                if walk == targ:
                    steps2 -= 1  # No "R" command if already exact
                if abs(targ2) <= barrier and steps2 < dist[targ2]:
                    heapq.heappush(pq, (steps2, targ2))
                    dist[targ2] = steps2
        return dist[0]


# 动态规划
# 我们可以使用动态规划来找到最短的指令长度
# 假设我们需要到达位置x，且2^k-1<=x<2^k。
# 我们用dp[x]表示到达位置x的最短指令长度。
# 如果t=2^k-1，那么我们只需要用A^k即可。否则我们需要考虑两种情况：
#  我们首先用A^k-1到达位置2^(k-1)-1，随后折返并使用A^j，这样我们到达了位置 2^(k-1)-2^j,
#  j < k-1
#  使用的指令为A^(k-1)RA^jR，长度为k-1+j+2，剩余的距离为x-(2^(k-1)-2^j)<x;
#  我们首先使用A^k到达位置2^k-1，随后仅使用折返指令，
#  此时我们已经超过了终点并且速度方向朝向终点，使用的指令为A^kR，长度为k+1
#  剩余的距离为(2^k)-1-x<x。
class Solution(object):
    def racecar(self, target):
        dp = [0] + [float('inf')] * target
        for t in range(1, target + 1):
            k = t.bit_length()
            if t == 2 ** k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                dp[t] = min(dp[t],
                            dp[t - 2 ** (k - 1) + 2 ** j] + k - 1 + j + 2)
            if 2 ** k - 1 - t < t:
                dp[t] = min(dp[t], dp[2 ** k - 1 - t] + k + 1)
        return dp[target]


class Solution:
    dp = {0: 0}

    def racecar(self, t):
        if t in self.dp:
            return self.dp[t]
        n = t.bit_length()
        if 2 ** n - 1 == t:
            self.dp[t] = n
        else:
            self.dp[t] = self.racecar(2 ** n - 1 - t) + n + 1
            for m in range(n - 1):
                self.dp[t] = min(self.dp[t], self.racecar(
                    t - 2 ** (n - 1) + 2 ** m) + n + m + 1)
        return self.dp[t]


class Solution:
    def racecar(self, target):
        dp = [0] + [float('inf')] * target
        for t in range(1, target + 1):
            n = t.bit_length()
            if t == (1 << n) - 1:
                dp[t] = n
            else:
                dp[t] = dp[2 ** n - 1 - t] + n + 1
                for k in range(n - 1):
                    dp[t] = min(dp[t],
                                dp[t - 2 ** (n - 1) + 2 ** k] + n + k + 1)
        return dp[target]


# 定义子问题
# 距离为i时的最小指令长度
# 第一次可以超过去
# n = t.bit_length()
# 2 ** n - 1
# A^nR
# 这时指令长度是 n + 1
# 现在我们的位置超过终点并且方向向着终点
# 还剩长度是 2**n-1 - t < t
# 或者不超过去
# 2 ** (n-1) - 1
# 1个R
# 然后向回走了2^j
# 指令是A^(n-1)RA^jR
# 走过的长度是2**(n-1)-2^j
# j < n
# 长度是n+j+1
# 还剩下的长度是t-2**(n-1)+2^j < t
# 所以递推方程
# f(i) = min(f(2**n-1-t) + n+ 1, f(t - (2**(n-1)-2^j)) + n+j+1), 0<=j < n
# 初始化
# f(0) = 0
# f(1) = 1
# 因为我们要求最小值，所以其他值设为一个大值
# 且f(2**n-1) == n
# 返回值f(target)
# 优化空间复杂度：不需要
class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] + [float('inf')] * target
        n = target.bit_length()
        if target == 2 ** n - 1:
            return n
        for i in range(1, target + 1):
            n = i.bit_length()
            right = 2 ** n - 1
            if i == right:
                dp[i] = n
            else:
                dp[i] = dp[right - i] + n + 1
                for j in range(n):
                    dp[i] = min(dp[i], dp[i - 2 ** (n - 1) + 2 ** j] +
                                n + j + 1)
        return dp[target]


# 我们来分析这个问题
# 我们定义f(i)为距离终点为i时所需的指令大小
# 如果i == 2 ** n - 1，指令的长度就为n
# 如果i != 2 ** n - 1，我们有两种走法
# 假设 2**(n-1) -1 < i < 2 **n - 1
# 这样n就等于i的bit_length
# 一种是走到 j = 2 ** n - 1
# 我们的指令是A^nR，指令长度为n+1，我们到终点的距离是 j-i，一定小于i
# 一种是走到 j = 2 ** (n-1) - 1, j < i
# 然后我们又往回走了 p = 2 ** k - 1, 现在我们的位置是 2 ** (n-1) - 2 ** k
# 指令长度是 A^(n-1)RA^kR n+k+1，我们现在距离终点 i - 2 **(n-1) + 2 ** k ,是小于i的
# 这样我们就得出了我们的递推公式
# f(i) = n if i == 2 ** n - 1
# f(i) = min(f(2**n -1 - i)+n+1, f(i-2**(n-1)+2**k)+n+k+1 k < n-1)
# 初始化和边界条件f(0) = 0，注意向会回走的k不会大于等于n-1，因为等于n-1时就走到0了
# 返回值f(target)
# 优化复杂度
class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] + [float('inf')] * target
        for i in range(1, target + 1):
            n = i.bit_length()
            if i == (1 << n) - 1:
                dp[i] = n
            else:
                dp[i] = dp[(1 << n) - 1 - i] + n + 1
                for k in range(n - 1):
                    dp[i] = min(dp[i],
                                dp[i - (1 << (n - 1)) + (1 << k)] + n + k + 1)
        return dp[target]


# f(i)为指令长度
# f(i) = n if  == 2 ** n -1
# 1 i < 2**n-1
# A^nR指令长度n+1，距离终点f(2**n-1-i)
# 2 i > 2**(n-1)+1
# A^(n-1)RA^kR 指令长度n + k + 1
# 距离终点i - (2**(n-1)-1 - 2**k + 1)= i - 2**(n-1) + 2**k
# 两者之间求最小值
# 初始化f(0)= 0，其他求最小按说可以用正无穷初始化，但是因为我们会先赋值f(2**n-1-i) + n-1
# 所以初始化成什么无所谓
# 返回值
# f(target)
# 优化复杂度
# 无法优化
class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)
        for i in range(1, target + 1):
            n = i.bit_length()
            if i == (1 << n) - 1:
                dp[i] = n
            else:
                dp[i] = dp[(1 << n) - 1 - i] + n + 1
                for k in range(n - 1):
                    dp[i] = min(dp[i],
                                dp[i - (1 << (n - 1)) + (1 << k)] + n + k + 1)
        return dp[target]


# 定义子问题
# f(i)为到达i所需要的最小指令数
# 令n为i的bit数
# i == 2 ** n - 1
# f(i) = n
# 先走到 2 ** n - 1 再调转方向
# 指令为A*nR，距离终点2**n - 1 - i
# f(i) = n+1 + f(2**n-1-i)
# 先走到 2**(n-1) - 1
# 往回走
# 2 ** k - 1
# 指令为 A^(n-1)RA^kR，距离终点为f(i - 2 ** (n-1)+2**k)
# 指令长度为n+k+1
# f(i) = n+k+1+f(i-2**(n-1)+2**k)
# k = 0..n-2
# 初始化和边界条件
# f(0) = 0
# 返回值f(target)
# 优化复杂度
class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)
        for i in range(1, target + 1):
            n = i.bit_length()
            if i == (1 << n) - 1:
                dp[i] = n
            else:
                dp[i] = dp[(1 << n) - 1 - i] + n + 1
                for k in range(0, n - 1):
                    dp[i] = min(dp[i],
                                dp[i - (1 << n - 1) + (1 << k)] + n + k + 1)
        return dp[target]


class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)
        for i in range(1, target + 1):
            n = i.bit_length()
            if i == (1 << n) - 1:
                dp[i] = n
            else:
                dp[i] = dp[(1 << n) - 1 - i] + n + 1
                for k in range(n - 1):
                    dp[i] = min(dp[i],
                                n + k + 1 + dp[i - (1 << n - 1) + (1 << k)])
        return dp[target]


def main():
    sol = Solution()

    n = 3
    res = sol.racecar(n)
    print(res)
    assert res == 2

    n = 6
    res = sol.racecar(n)
    print(res)
    assert res == 5

    n = 4
    res = sol.racecar(n)
    print(res)
    assert res == 5


if __name__ == '__main__':
    main()
