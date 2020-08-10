# 282. 给表达式添加运算符.py
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        answers = []

        def recurse(index, prev_operand, current_operand, value, string):
            if index == n:
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return
            current_operand = current_operand * 10 + int(num[index])
            str_op = str(current_operand)

            if current_operand > 0:
                recurse(index + 1, prev_operand, current_operand, value, string)

            string.append('+')
            string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand,
                    string)
            string.pop()
            string.pop()

            if string:
                string.append('-')
                string.append(str_op)
                recurse(index + 1, -current_operand, 0, value -
                        current_operand, string)
                string.pop()
                string.pop()
                string.append('*')
                string.append(str_op)
                recurse(index + 1, current_operand * prev_operand, 0, value -
                        prev_operand + (prev_operand * current_operand), string)
                string.pop()
                string.pop()

        recurse(0, 0, 0, 0, [])
        return answers


def main():
    sol = Solution()
    num = "123"
    target = 6
    res = sol.addOperators(num, target)
    print(res)


if __name__ == '__main__':
    main()
