# 22. 括号生成(bfs写法).py


from typing import List


# 成员函数
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.__dfs(0, 0, n, '', res)
        return res

    def __dfs(self, left, right, n, ans, res):
        # recursion terminator
        if left == n and right == n:
            res.append(ans)
            return

        # process current level logic
        # drill down
        if left < n:
            self.__dfs(left + 1, right, n, ans + '(', res)

        if right < left:
            self.__dfs(left, right + 1, n, ans + ')', res)
        # reverse current level status if needed


# 内部函数
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(ans, left, right):
            # recursion terminator
            if right == n:
                res.append(ans)
                return

            # process current level logic

            if left < n:
                dfs(ans + '(', left + 1, right)
            if right < left:
                dfs(ans + ')', left, right + 1)

        res = []
        dfs('', 0, 0)
        return res


def main():
    n = 3
    sol = Solution()
    res = sol.generateParenthesis(n)
    print(res)


if __name__ == '__main__':
    main()
