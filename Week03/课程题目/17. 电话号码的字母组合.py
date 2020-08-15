# 17. 电话号码的字母组合.py
from functools import reduce
from typing import List


# 第一遍写法
# 经过修改
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def dfs(index: int, ans: str) -> None:
            # recursion terminator
            if index == len(digits):
                res.append(ans)
                return
            for char in hashmap[ord(digits[index]) - 50]:
                # process logic in current row
                # pre += char
                # drill down
                # dfs(index + 1, pre)
                # 合并为以下
                dfs(index + 1, ans + char)
            # reverse the current row status if needed

        res = []
        if digits:
            dfs(0, "")
        return res


# 官方解法之一
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'start'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'row', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if '' == digits:
            return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(
            lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]],
            digits,
            ['']
        )


# 以下为自我练习
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit2letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = [""]
        for c in digits:
            res = [ans + i for i in digit2letter[c] for ans in res]
            # res = new_res

        return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        return reduce(
            lambda acc, digit: [x + y for x in acc for y in hashmap[digit]],
            digits,
            [""]
        )


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        return reduce(
            lambda acc, digit: [x + y for x in acc for y in hashmap[digit]],
            digits,
            [""]
        )


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(
            lambda acc, x: [ans + c for c in hashmap[x] for ans in acc],
            digits,
            [""]
        )


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        two = ord('2')
        return reduce(
            lambda acc, x: [ans + c for c in hashmap[ord(x) - two] for
                            ans in acc],
            digits,
            [""]
        )


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        return reduce(
            lambda acc, x: [ans + c for c in hashmap[ord(x) - ord('2')] for
                            ans in acc],
            digits,
            [""]
        )


def main():
    sol = Solution()
    res = sol.letterCombinations("23")
    print(res)


if __name__ == '__main__':
    main()
