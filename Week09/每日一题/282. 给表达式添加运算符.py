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


# 以下为自我练习
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []

        def recurse(i, pre_operand, cur_operand, value, s):
            if i == n:
                if value == target and cur_operand == 0:
                    res.append(''.join(s[1:]))
                return
            cur_operand = cur_operand * 10 + int(num[i])
            str_op = str(cur_operand)
            if cur_operand > 0:
                recurse(i + 1, pre_operand, cur_operand, value, s)
            s.append('+')
            s.append(str_op)
            recurse(i + 1, cur_operand, 0, value + cur_operand, s)
            s.pop()
            s.pop()
            if s:
                s.append('-')
                s.append(str_op)
                recurse(i + 1, -cur_operand, 0, value - cur_operand, s)
                s.pop()
                s.pop()
                s.append('*')
                s.append(str_op)
                recurse(i + 1, pre_operand * cur_operand, 0, value -
                        pre_operand + (pre_operand * cur_operand), s)
                s.pop()
                s.pop()

        recurse(0, 0, 0, 0, [])
        return res


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []

        def recurse(i, pre_operand, cur_operand, value, s):
            if i == n:
                if value == target and cur_operand == 0:
                    res.append(''.join(s[1:]))
                return
            cur_operand = cur_operand * 10 + int(num[i])
            str_op = str(cur_operand)
            if cur_operand > 0:
                recurse(i + 1, pre_operand, cur_operand, value, s)
            s.append('+')
            s.append(str_op)
            recurse(i + 1, cur_operand, 0, value + cur_operand, s)
            s.pop()
            s.pop()
            if s:
                s.append('-')
                s.append(str_op)
                recurse(i + 1, -cur_operand, 0, value - cur_operand, s)
                s.pop()
                s.pop()
                s.append('*')
                s.append(str_op)
                recurse(i + 1, pre_operand * cur_operand, 0, value -
                        pre_operand + pre_operand * cur_operand, s)
                s.pop()
                s.pop()

        recurse(0, 0, 0, 0, [])
        return res


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []

        def recurse(i, pre_operand, cur_operand, val, s):
            if i == n:
                if val == target and cur_operand == 0:
                    res.append(''.join(s[1:]))
                return
            cur_operand = cur_operand * 10 + int(num[i])
            str_op = str(cur_operand)
            if cur_operand > 0:
                recurse(i + 1, pre_operand, cur_operand, val, s)
            s.append('+')
            s.append(str_op)
            recurse(i + 1, cur_operand, 0, val + cur_operand, s)
            s.pop()
            s.pop()
            if s:
                s.append('-')
                s.append(str_op)
                recurse(i + 1, -cur_operand, 0, val - cur_operand, s)
                s.pop()
                s.pop()
                s.append('*')
                s.append(str_op)
                recurse(i + 1, pre_operand * cur_operand, 0, val - pre_operand +
                        pre_operand * cur_operand, s)
                s.pop()
                s.pop()

        recurse(0, 0, 0, 0, [])
        return res


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []

        def recurse(i, pre_operand, cur_operand, value, s: list):
            if i == n:
                if value == target and cur_operand == 0:
                    res.append(''.join(s[1:]))
                return
            cur_operand = cur_operand * 10 + int(num[i])
            if cur_operand > 0:
                recurse(i + 1, pre_operand, cur_operand, value, s)
            str_op = str(cur_operand)
            s.append('+')
            s.append(str_op)
            recurse(i + 1, cur_operand, 0, value + cur_operand, s)
            s.pop()
            s.pop()
            if s:
                s.append('-')
                s.append(str_op)
                recurse(i + 1, -cur_operand, 0, value - cur_operand, s)
                s.pop()
                s.pop()
                s.append('*')
                s.append(str_op)
                recurse(i + 1, pre_operand * cur_operand, 0, value -
                        pre_operand + pre_operand * cur_operand, s)
                s.pop()
                s.pop()

        recurse(0, 0, 0, 0, [])
        return res


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []

        def recurse(i, pre_operand, cur_operand, value, s: list):
            if i == n:
                if value == target and cur_operand == 0:
                    res.append(''.join(s[1:]))
                return
            cur_operand = cur_operand * 10 + int(num[i])
            if cur_operand > 0:
                recurse(i + 1, pre_operand, cur_operand, value, s)
            str_op = str(cur_operand)
            s.append('+')
            s.append(str_op)
            recurse(i + 1, cur_operand, 0, value + cur_operand, s)
            s.pop()
            s.pop()
            if s:
                s.append('-')
                s.append(str_op)
                recurse(i + 1, -cur_operand, 0, value - cur_operand, s)
                s.pop()
                s.pop()
                s.append('*')
                s.append(str_op)
                recurse(i + 1, pre_operand * cur_operand, 0, value - pre_operand
                        + pre_operand * cur_operand, s)
                s.pop()
                s.pop()

        recurse(0, 0, 0, 0, [])
        return res


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []

        def recurse(i, pre_operand, cur_operand, value, s: list):
            if i == n:
                if value == target and cur_operand == 0:
                    res.append(''.join(s[1:]))
                return
            cur_operand = cur_operand * 10 + int(num[i])
            if cur_operand > 0:
                recurse(i + 1, pre_operand, cur_operand, value, s)
            str_op = str(cur_operand)
            s.append('+')
            s.append(str_op)
            recurse(i + 1, cur_operand, 0, value + cur_operand, s)
            s.pop()
            s.pop()
            if s:
                s.append('-')
                s.append(str_op)
                recurse(i + 1, -cur_operand, 0, value - cur_operand, s)
                s.pop()
                s.pop()
                s.append('*')
                s.append(str_op)
                recurse(i + 1, pre_operand * cur_operand, 0, value -
                        pre_operand + pre_operand * cur_operand, s)
                s.pop()
                s.pop()

        recurse(0, 0, 0, 0, [])
        return res


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []

        def recurse(i, pre_operand, cur_operand, value, s: list):
            if i == n:
                if value == target and cur_operand == 0:
                    res.append(''.join(s[1:]))
                return
            cur_operand = cur_operand * 10 + int(num[i])
            if cur_operand > 0:
                recurse(i + 1, pre_operand, cur_operand, value, s)
            str_op = str(cur_operand)
            s.append('+')
            s.append(str_op)
            recurse(i + 1, cur_operand, 0, value + cur_operand, s)
            s.pop()
            s.pop()
            if s:
                s.append('-')
                s.append(str_op)
                recurse(i + 1, -cur_operand, 0, value - cur_operand, s)
                s.pop()
                s.pop()
                s.append('*')
                s.append(str_op)
                recurse(i + 1, pre_operand * cur_operand, 0, value -
                        pre_operand + pre_operand * cur_operand, s)
                s.pop()
                s.pop()

        recurse(0, 0, 0, 0, [])
        return res


def main():
    sol = Solution()

    num = "123"
    target = 6
    res = sol.addOperators(num, target)
    print(res)

    num = "105"
    target = 5
    res = sol.addOperators(num, target)
    print(res)


if __name__ == '__main__':
    main()
