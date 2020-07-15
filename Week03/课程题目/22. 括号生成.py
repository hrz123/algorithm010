# 22. 括号生成(bfs写法).py
from collections import deque
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
            # process logic in current level

            # drill down
            if left < n:
                helper(ans + '(', left + 1, right)
            if right < left:
                helper(ans + ')', left, right + 1)

            # reverse the current level status if needed

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

            # process current level logic
            # drill down
            if left < n:
                helper(ans + '(', left + 1, right)

            if right < left:
                helper(ans + ')', left, right + 1)

            # reverse current level status if needed

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


def main():
    s = Solution()
    res = s.generateParenthesis(3)
    print(res)


if __name__ == '__main__':
    main()
