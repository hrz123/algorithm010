# 22. 括号生成.py
from functools import lru_cache
from typing import List


# 1.暴力法。
# 我们可以生成所有 2^{2n}个 '(' 和 ')' 字符构成的序列，
# 然后我们检查每一个是否有效即可。
# 算法
# 为了生成所有序列，我们可以使用递归。长度为 n 的序列就是在长度为 n-1 的序列前加一个'('或')'。
# 为了检查序列是否有效，我们遍历这个序列，
# 并使用一个变量 balance 表示左括号的数量减去右括号的数量。
# 如果在遍历的过程中 balance 的值小于零，或者结束时 balance 的值不为零，
# 那么该序列就是无效的，否则它是有效的。

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(li: List):
            if len(li) == 2 * n:
                if valid(li):
                    ans.append("".join(li))
            else:
                li.append('(')
                generate(li)
                li.pop()
                li.append(')')
                generate(li)
                li.pop()

        def valid(li: List):
            bal = 0
            for c in li:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        ans = []
        generate([])
        return ans


# 时间复杂度分析：O(2^2n * n)，对于2^2n个序列中的每一个，
# 我们用于建立和验证该序列的复杂度为O(n)
# 空间复杂度：O(n)。除了答案数组之外，我们所需要的空间取决于递归栈的深度。
# 每一层递归函数需要O(1)的空间，最多递归2n层，因此空间复杂度为O(n)

# 方法二：回溯法
# 思路和算法
# 方法一还有改进的余地：我们可以只在序列仍然保持有效时才添加'('或者')'，而不是像
# 方法一那样每次添加，我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点。
# 如果左括号的数量不大于n，我们可以放一个左括号。如果右括号数量闲鱼左括号的数量，
# 我们可以放一个右括号。
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                ans.append(''.join(s))
                return
            if left < n:
                s.append('(')
                backtrack(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(')')
                backtrack(s, left, right + 1)
                s.pop()

        backtrack([], 0, 0)
        return ans


# 时间复杂度：依赖于generateParenthesis中有多少个元素。这是一个卡特兰数
# 第n个卡特兰数是1/(n+1)C(2n, n)。是有4 ^ n / n sqrt(n)界定的
# O(4^n/sqrt(n))
# 空间复杂度：O(n)。栈的递归深度最多2n。


# 任何一个括号序列都一定是由 ( 开头，并且第一个 ( 一定有一个唯一与之对应的 )。这样一来，每一个括号序列可以用 (a)b 来表示，其中 a 与 b 分别是一个合法的括号序列（可以为空）。
#
# 那么，要生成所有长度为 2 * n 的括号序列，我们定义一个函数 generate(n) 来返回所有可能的括号序列。那么在函数 generate(n) 的过程中：
#
# 我们需要枚举与第一个 ( 对应的 ) 的位置 2 * i + 1；
# 递归调用 generate(i) 即可计算 a 的所有可能性；
# 递归调用 generate(n - i - 1) 即可计算 b 的所有可能性；
# 遍历 a 与 b 的所有可能性并拼接，即可得到所有长度为 2 * n 的括号序列。
# 为了节省计算时间，我们在每次 generate(i) 函数返回之前，把返回值存储起来，下次再调用 generate(i) 时可以直接返回，不需要再递归计算。


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


# 时间复杂度：O(4^n/sqrt(n))
# 空间复杂度：O(4^n/sqrt(n))。中间过程中会存储与答案数组同样数量级的临时数组。(注意有缓存)

def main():
    pass


if __name__ == '__main__':
    main()
