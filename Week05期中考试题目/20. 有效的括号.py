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


def main():
    s = "()[]{}"
    s1 = "([)]"
    s2 = "(]"
    s3 = "()[]{([])}("
    s4 = "[[([[)(()"
    s5 = "    "
    s6 = ""
    s7 = None
    sol = Solution()
    res = sol.isValid(s)
    print(res)
    res = sol.isValid(s1)
    print(res)
    res = sol.isValid(s2)
    print(res)
    res = sol.isValid(s3)
    print(res)
    res = sol.isValid(s4)
    print(res)
    res = sol.isValid(s5)
    print(res)
    res = sol.isValid(s6)
    print(res)
    res = sol.isValid(s7)
    print(res)


if __name__ == '__main__':
    main()
