# 20. 有效的括号.py


# 遍历
# 因为满足后进先出的特性，所以用stack做缓存
# 用一个hashmap存储对应关系
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s:
            if ch not in hashmap:
                stack.append(ch)
            else:
                if not stack or stack.pop() != hashmap[ch]:
                    return False
        return not stack


# 以下为自我练习
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in hashmap:
                if not stack or stack.pop() != hashmap[c]:
                    return False
            else:
                stack.append(c)
        return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in hashmap:
                if not stack or stack.pop() != hashmap[c]:
                    return False
            else:
                stack.append(c)
        return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in hashmap:
                if not stack or stack.pop() != hashmap[c]:
                    return False
            else:
                stack.append(c)
        return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in hashmap:
                if not stack or stack.pop() != hashmap[c]:
                    return False
            else:
                stack.append(c)
        return not stack


def main():
    sol = Solution()

    s = "()[]{}"
    res = sol.isValid(s)
    print(res)

    s1 = "([)]"
    res = sol.isValid(s1)
    print(res)

    s2 = "(]"
    res = sol.isValid(s2)
    print(res)

    s3 = "()[]{([])}("
    res = sol.isValid(s3)
    print(res)
    s4 = "[[([[)(()"
    res = sol.isValid(s4)
    print(res)
    s5 = "    "
    res = sol.isValid(s5)
    print(res)
    s6 = ""
    res = sol.isValid(s6)
    print(res)


if __name__ == '__main__':
    main()
