# 150. 逆波兰表达式求值.py
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        plus = lambda a, b: b + a
        sub = lambda a, b: b - a
        mul = lambda a, b: b * a
        div = lambda a, b: int(b / a)
        opt = {
            "+": plus,
            "-": sub,
            "*": mul,
            "/": div
        }
        for t in tokens:
            if t in opt:
                stack.append(opt[t](stack.pop(), stack.pop()))
            else:
                stack.append(int(t))
        return stack.pop()


def main():
    pass


if __name__ == '__main__':
    main()
