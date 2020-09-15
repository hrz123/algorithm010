# 85. 最大矩形.py
from typing import List


# 方法1：暴力解法
# 方法2：动态规划 - 使用柱状图的优化暴力方法
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue

                # compute the maximum width and update dp with it
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

                # compute the maximum area rectangle
                # with a lower r corner at [start, j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i - k + 1))
        return maxarea


# 方法3：动态规划+柱状图单调栈算法
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                dp[i][j] = dp[i][j - 1] + 1 if j else 1
        res = 0
        for j in range(len(dp[0])):
            stack = []
            for i in range(len(dp)):
                while stack and dp[stack[-1]][j] > dp[i][j]:
                    h = dp[stack.pop()][j]
                    w = i - (stack[-1] if stack else -1) - 1
                    res = max(res, h * w)
                stack.append(i)
            while stack:
                h = dp[stack.pop()][j]
                w = len(dp) - (stack[-1] if stack else -1) - 1
                res = max(res, h * w)
        return res


# 优秀的国际站解法
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans


# 方法4.动态规划-每个点的最大高度
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n  # initialize m as the leftmost boundary possible
        right = [n] * n  # initialize r as the rightmost boundary possible
        height = [0] * n

        maxarea = 0

        for i in range(m):
            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            # update m
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update r
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))
        return maxarea


# 以下为自我练习
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        res = 0
        for row in matrix:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            stack = [-1]
            for k in range(n + 1):
                while stack and heights[stack[-1]] > heights[k]:
                    h = heights[stack.pop()]
                    w = k - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(k)
        return res


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        res = 0
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            stack = [-1]
            for k in range(n + 1):
                while stack and heights[stack[-1]] > heights[k]:
                    h = heights[stack.pop()]
                    w = k - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(k)
        return res


# 方法四里的 m[j] = 0 和 r[j] = m 我觉得有点难懂。
# 写一点我自己的理解：当matrix[start][j]是0的时候，height[j]是0，所以面积肯定是0了，
# m[j]和right[j]并不影响这个位置的面积的计算。
# 但是如果我们不更新left[j]和right[j]，
# 到下一行时，代码还以为上一行这个位置的矩形最多只能在left[j]和right[j]之间，
# 但实际上上一行这个位置并没有构成矩形。
# 所以left[j] = 0 和 r[j] = n是为了在计算下一行时
# 保证上一行无效的left[j]和right[j]被丢弃，即重置。
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        left = [0] * n
        right = [n] * n
        heights = [0] * n
        _max_area = 0
        for i in range(m):
            cur_left, cur_right = 0, n
            # 更新heights
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                _max_area = max(_max_area, heights[j] * (right[j] - left[j]))
        return _max_area


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        left = [0] * n
        right = [n] * n
        res = 0
        for i in range(m):
            cur_left, cur_right = 0, n
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                res = max(res, heights[j] * (right[j] - left[j]))
        return res


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        res = 0
        for row in matrix:
            stack = [-1]
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            for i in range(n + 1):
                while heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        res = 0
        for row in matrix:
            stack = [-1]
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            for i in range(n + 1):
                while heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        res = 0
        for row in matrix:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            stack = [-1]
            for j in range(len(heights)):
                while heights[stack[-1]] > heights[j]:
                    h = heights[stack.pop()]
                    w = j - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(j)
        return res


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        res = 0
        for row in matrix:
            for i in range(n):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            stack = [-1]
            for i, h in enumerate(heights):
                while heights[stack[-1]] > h:
                    t = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, t * w)
                stack.append(i)
        return res


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        res = 0
        for row in matrix:
            stack = [-1]
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            for i, h in enumerate(heights):
                while heights[stack[-1]] > h:
                    t = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, t * w)
                stack.append(i)
        return res


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        height = [0] * (n + 1)
        res = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i, h in enumerate(height):
                while height[stack[-1]] > h:
                    tmp = height[stack.pop()]
                    res = max(res, tmp * (i - stack[-1] - 1))
                stack.append(i)
        return res


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        height = [0] * (n + 1)
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i, h in enumerate(height):
                while height[stack[-1]] > h:
                    tmp = height[stack.pop()]
                    res = max(res, tmp * (i - stack[-1] - 1))
                stack.append(i)
        return res


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        height = [0] * (n + 1)
        res = 0
        for row in matrix:
            stack = [-1]
            for i in range(n):
                if row[i] == '1':
                    height[i] += 1
                else:
                    height[i] = 0
            for i, h in enumerate(height):
                while stack and height[stack[-1]] > h:
                    tmp = height[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, tmp * w)
                stack.append(i)
        return res


def main():
    sol = Solution()

    nums = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    res = sol.maximalRectangle(nums)
    print(res)


if __name__ == '__main__':
    main()
