# 22. 括号生成(bfs写法).py
from collections import deque
from functools import lru_cache
from typing import List


# 上周预习题，这周默写
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(ans, left, right):
            # recursion terminator
            # 因为右小于左，因为left最大为n，所以只用判断右
            if right == n:
                res.append(ans)
                return
            # process logic in current row

            # drill down
            if left < n:
                helper(ans + '(', left + 1, right)
            if right < left:
                helper(ans + ')', left, right + 1)

            # reverse the current row status if needed

        res = []
        helper("", 0, 0)
        return res


# bfs
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        # 要在bfs的内容中记录一些状态
        # 当前的字符串，left和right使用情况
        deq = deque([("", (0, 0))])
        while deq:
            top = deq.popleft()
            ans = top[0]
            left = top[1][0]
            right = top[1][1]
            if right == n:
                res.append(ans)

            if left < n:
                deq.append((ans + '(', (left + 1, right)))
            if right < left:
                deq.append((ans + ')', (left, right + 1)))

        return res


# dfs
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [("", (0, 0))]

        # 要在dfs的内容中记录一些状态
        # 当前的字符串，left和right使用情况
        while stack:
            top = stack.pop()
            ans = top[0]
            left = top[1][0]
            right = top[1][1]
            if right == n:
                res.append(ans)

            if left < n:
                stack.append((ans + '(', (left + 1, right)))
            if right < left:
                stack.append((ans + ')', (left, right + 1)))

        return res


# 以下为自我练习
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(ans, left, right):
            # recursion terminator
            if right == n:
                res.append(ans)

            # process current row logic
            # drill down
            if left < n:
                helper(ans + '(', left + 1, right)

            if right < left:
                helper(ans + ')', left, right + 1)

            # reverse current row status if needed

        helper("", 0, 0)
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(ans, left, right):
            # recursion terminator
            if right == n:
                res.append(ans)
                return
            # drill down
            if left < n:
                dfs(ans + '(', left + 1, right)
            if right < left:
                dfs(ans + ')', left, right + 1)

        dfs('', 0, 0)
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, pre):
            if right == n:
                res.append(pre)
                return
            if left < n:
                dfs(left + 1, right, pre + '(')
            if right < left:
                dfs(left, right + 1, pre + ')')

        dfs(0, 0, '')
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        deq = deque([("", 0, 0)])
        while deq:
            pre, l, r = deq.popleft()
            if r == n:
                res.append(pre)
            if l < n:
                deq.append((pre + '(', l + 1, r))
            if r < l:
                deq.append((pre + ')', l, r + 1))
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        stack = [('', 0, 0)]
        while stack:
            pre, l, r = stack.pop()
            if r == n:
                res.append(pre)
            if l < n:
                stack.append((pre + '(', l + 1, r))
            if r < l:
                stack.append((pre + ')', l, r + 1))
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, pre):
            if r == n:
                res.append(pre)
                return
            if l < n:
                dfs(l + 1, r, pre + '(')
            if r < l:
                dfs(l, r + 1, pre + ')')

        dfs(0, 0, '')
        return res


class Solution:
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> int:
        if n <= 1:
            return 1
        res = 0
        for i in range(n):
            res += self.generateParenthesis(i) * self.generateParenthesis(
                n - i - 1)
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, pre):
            if r == n:
                res.append(pre)
                return
            if l < n:
                dfs(l + 1, r, pre + '(')
            if r < l:
                dfs(l, r + 1, pre + ')')

        dfs(0, 0, '')
        return res


class Solution:
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans


class Solution:
    @lru_cache(None)
    def countParen(self, n: int) -> int:
        if n <= 1:
            return 1
        res = 0
        for i in range(n):
            res += self.countParen(i) * self.countParen(n - i - 1)
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, pre):
            if r == n:
                res.append(pre)
                return
            if l < n:
                dfs(l + 1, r, pre + '(')
            if r < l:
                dfs(l, r + 1, pre + ')')

        dfs(0, 0, '')
        return res

    @lru_cache(None)
    def countParen(self, n: int) -> int:
        if n == 0:
            return 1
        res = 0
        for i in range(n):
            res += self.countParen(i) * self.countParen(n - i - 1)
        return res


def main():
    s = Solution()
    res = s.generateParenthesis(3)
    print(res)
    res = s.countParen(3)
    print(res)


if __name__ == '__main__':
    main()
