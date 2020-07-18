# 403. 青蛙过河.py
import bisect
from functools import lru_cache
from typing import List


# 暴力解法
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        def dfs(cur_pos, jump_size):
            # recursion terminator
            if cur_pos == n - 1:
                return True
            # process current level logic
            for i in range(cur_pos + 1, n):
                gap = stones[i] - stones[cur_pos]
                if jump_size - 1 <= gap <= jump_size + 1:
                    # drill down
                    # 有一种走法能到就结束返回True
                    if dfs(i, gap):
                        return True
            # merge
            return False

        return dfs(0, 0)


# 超时


# 暴力解法加上记忆化搜索
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        @lru_cache(None)
        def dfs(cur_pos, jump_size):
            if cur_pos == n - 1:
                return True
            for i in range(cur_pos + 1, n):
                gap = stones[i] - stones[cur_pos]
                if jump_size - 1 <= gap <= jump_size + 1:
                    if dfs(i, gap):
                        return True
            return False

        return dfs(0, 0)


# AC

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        @lru_cache(None)
        def dfs(cur_pos, jump_size):
            if cur_pos == n - 1:
                return True
            for i in range(cur_pos + 1, n):
                gap = stones[i] - stones[cur_pos]
                if jump_size - 1 <= gap <= jump_size + 1:
                    if dfs(i, gap):
                        return True
                # 剪枝
                elif gap > jump_size + 1:
                    break
            return False

        return dfs(0, 0)


# 时间复杂度： n^2的递归，每次递归需要O(n)的时间找到下次递归的位置
# 空间复杂度：O(N^2)，递归


# 前20%-50%

# 加入二分法
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        @lru_cache(None)
        def dfs(cur_pos, jump_size):
            if cur_pos == n - 1:
                return True
            # 找到当前大于stones[cur_pos] + jumpsize - 1的最小的值的索引
            l_bound = bisect.bisect_left(stones, stones[cur_pos] + jump_size -
                                         1, cur_pos + 1)
            # 找到当前小于stones[cur_pos] + jumpsize + 1的最大的值的索引 + 1
            r_bound = bisect.bisect(stones, stones[cur_pos] + jump_size + 1,
                                    l_bound)
            for i in range(l_bound, r_bound):
                if dfs(i, stones[i] - stones[cur_pos]):
                    return True
            return False

        return dfs(0, 0)


# 时间复杂度：
# 空间复杂度：O(n^2)


# 更快了一些 超过了80%多

# dp
# Suppose we want to know if the frog can reach stone 2 (S2)
# and we know the frog must come from S1
# dist(S1 --> S2) = 1 - 0 = 1, and we know the frog is able to make a jump of
# size 1 at S1.
# Hence, the frog is able  to reach S2, and the next jump would be 0, 1,
# or 2 units.

# Then, we want to know if the frog can reach stone 3 (S3),
# we jnow the frog must be at either S1 or S2 before reaching S3.

# If the frog comes from S1, then
# dist(S3 --> S1) = 3 - 0 = 3, and we know frog couldn't make a jump of size
# 3 at S1.
# So it is not possible the frog can jump from S1 to S3.

# If the frog comes from S2, then
# we know dist(S2 --> S3) = 3 - 1 = 2, and we know frog could make a jump of
# size 2 at S2.
# Hence the frog is able to reach S3, and the next jump could be 1, 2, 3, units.

# If we repeat doing this for the rest stones, we'll end up with something
# like below:
# Example 1
# index:        0   1   2   3   4   5   6   7
# stone pos:    0   1   3   5   6   8   12  17
# next jump:    1   0   1   1   0   1   3   4
#                   1   2   2   1   2   4   5
#                   2   3   3   2   3   5   6
#                               3   4
#                               4

# 子问题和状态
# dp(i) denote a set containing all next jump sizes at stone i.

# recurrence relation:
# for any j < i:
# dist = stones[j] - stones[i]
# if dist in dp(j)
#     put dist - 1, dist, dist + 1 into dp(i)

# now let make this approach more efficient.
# Because
# 1. The number of stones is >= 2 and is <1,100.
# 2. The frog is on first stone and assume the first jump must be 1 unit.
# 3. If the frog's last jump was k units, then its next jump must be either k
# - 1, k, or k + 1 units.

# The maximum jump size the frog can make at stone if possible is shown as
# followings:
# stones:        0, 1, 2, 3, 4, 5, ...
# jump size:     1, 2, 3, 4, 5, 6, ...(suppose frog made jump with k + 1 at
# each stone)

# So instead of creating a hash set for lookup for each stone,
# we can create a boolean array with size of N + 1 (N is the number of stones).
# Like in the given example, at stone 2 , the next jump could be 1, 2, or 3.
# We can use a bool array to represent this like
# index:    0  1  2  3  4  5 ...
# value:   [0  1  1  1  0  0 ...]
# index is jump size, boolean value represent if the frog can make this jump.

# Then the 2D array will be something like below:

# index:            0   1   2   3   4   5   6   7
# stone pos:        0   1   3   5   6   8   12  17
# next jump:    0   0   1   0   0   1   0   0   0
#               1   1   1   1   1   1   1   0   0
#               2   0   1   1   1   1   1   0   0
#               3   0   0   1   1   1   1   1   0
#               4   0   0   0   0   1   1   1   1
#               5   0   0   0   0   0   0   1   1
#               6   0   0   0   0   0   0   0   1
#               7   0   0   0   0   0   0   0   0


# sub-problem and state

# let dp[i][j] denote at stone i, the frog can or cannot make jump of size j
# recurrence relation
# for and j < i,
# dist = stones[i] - stones[j]
# if dp[j][dist]:
#     dp[i][dist - 1] = true
#     dp[i][dist] = true
#     dp[i][dist + 1] = true


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False] * n for _ in range(n)]
        dp[0][1] = True
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                dist = stones[i] - stones[j]
                # 判断越界
                if dist < n and dp[j][dist]:
                    dp[i][dist - 1] = True
                    dp[i][dist] = True
                    if dist + 1 < n:
                        dp[i][dist + 1] = True
        return any(dp[n - 1])


# 时间复杂度：O(n^2)，但是反而变慢了，leetcode 上只超过了30%


# dfs, using memo
# 将stones变成set，检查下一步的candidate是否在stones中，变成了O(1)的操作
class Solution(object):
    def __init__(self):
        self.memo = set()

    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        stones = set(stones)

        return self.bt(stones, 1, 1, target)

    def bt(self, stones, cur, speed, target):
        # check memo
        if (cur, speed) in self.memo:
            return False

        if cur == target:
            return True

        if cur > target or cur < 0 or speed <= 0 or cur not in stones:
            return False
        # dfs
        candidate = [speed - 1, speed, speed + 1]
        for c in candidate:
            if (cur + c) in stones:
                if self.bt(stones, cur + c, c, target):
                    return True

        self.memo.add((cur, speed))
        return False


# 以下为自我练习
class Solution(object):
    def __init__(self):
        self.memo = set()

    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        stones = set(stones)
        return self.__bt(stones, 1, 1, target)

    def __bt(self, stones, cur, speed, target):
        # check memo
        if (cur, speed) in self.memo:
            return False

        if cur == target:
            return True

        if cur < 0 or cur > target or speed <= 0 or cur not in stones:
            return False

        # dfs
        candidates = [speed - 1, speed, speed + 1]
        for c in candidates:
            if cur + c in stones:
                if self.__bt(stones, cur + c, c, target):
                    return True

        self.memo.add((cur, speed))
        return False


def main():
    sol = Solution()

    stones = [0, 1, 3, 5, 6, 8, 12, 17]
    res = sol.canCross(stones)
    print(res)

    stones = [0, 1, 2, 3, 4, 8, 9, 11]
    res = sol.canCross(stones)
    print(res)


if __name__ == '__main__':
    main()
