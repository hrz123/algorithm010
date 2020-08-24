# 415. 字符串相加.py


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = []
        carry = 0
        i, j = m - 1, n - 1
        while i >= 0 or j >= 0:
            _sum = (ord(num1[i]) - ord('0') if i >= 0 else 0) + \
                   (ord(num2[j]) - ord('0') if j >= 0 else 0) + carry
            carry, mod = divmod(_sum, 10)
            res.append(str(mod))
            i -= 1
            j -= 1
        if carry:
            res.append('1')
        return ''.join(reversed(res))


# 以下为自我练习
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = []
        carry = 0
        i, j = m - 1, n - 1
        while i >= 0 or j >= 0:
            val1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            val2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            _sum = val1 + val2 + carry
            carry, mod = divmod(_sum, 10)
            res.append(str(mod))
            i -= 1
            j -= 1
        if carry:
            res.append('1')
        return ''.join(reversed(res))


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(reversed(num1))
        num2 = list(reversed(num2))
        m, n = len(num1), len(num2)
        i, j = 0, 0
        res = []
        carry = 0
        while i < m or j < n:
            n1 = ord(num1[i]) - ord('0') if i < m else 0
            n2 = ord(num2[j]) - ord('0') if j < n else 0
            carry, mod = divmod(n1 + n2 + carry, 10)
            res.append(str(mod))
            i += 1
            j += 1
        if carry:
            res.append('1')
        return ''.join(reversed(res))


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = []
        zero = ord('0')
        i, j = m - 1, n - 1
        carry = 0
        while i >= 0 or j >= 0:
            n1 = ord(num1[i]) - zero if i >= 0 else 0
            n2 = ord(num2[j]) - zero if j >= 0 else 0
            total = n1 + n2 + carry
            carry, mod = divmod(total, 10)
            res.append(str(mod))
            i -= 1
            j -= 1
        if carry:
            res.append('1')
        return ''.join(res[::-1])


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        i, j = m - 1, n - 1
        zero = ord('0')
        carry = 0
        res = []
        while i >= 0 or j >= 0:
            n1 = ord(num1[i]) - zero if i >= 0 else 0
            n2 = ord(num2[j]) - zero if j >= 0 else 0
            carry, mod = divmod(n1 + n2 + carry, 10)
            res.append(str(mod))
            i -= 1
            j -= 1
        if carry:
            res.append('1')
        return ''.join(reversed(res))


def main():
    sol = Solution()

    num1 = '999'
    num2 = '1'
    res = sol.addStrings(num1, num2)
    print(res)


if __name__ == '__main__':
    main()
