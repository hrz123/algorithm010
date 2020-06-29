# 22. 括号生成.py
from typing import List

# 上周预习题，这周默写

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(ans, left, right):
            # recursion terminator
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


def main():
    s = Solution()
    res = s.generateParenthesis(3)
    print(res)


if __name__ == '__main__':
    main()
