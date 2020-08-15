# 67. 二进制求和.py
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        if m < n:
            a, b = b, a
            m, n = n, m
        j = n - 1
        carry = "0"
        res = []
        for i in range(m - 1, -1, -1):
            a_i = a[i]
            if j < 0:
                b_j = "0"
            else:
                b_j = b[j]
            if a_i == "1" and b_j == "1" and carry == "1":
                carry = "1"
                res.append("1")
            elif a_i == "0" and b_j == "0" and carry == "0":
                carry = "0"
                res.append("0")
            elif (a_i, b_j, carry) in {("1", "0", "0"), ("0", "1", "0"),
                                       ("0", "0", "1")}:
                carry = "0"
                res.append("1")
            else:
                carry = "1"
                res.append("0")
            j -= 1
        # 注意如果还有carry，要在首位添加1
        if carry == "1":
            res.append("1")

        return "".join(reversed(res))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            total = carry
            total += ord(a[i]) - ord('0') if i >= 0 else 0
            total += ord(b[j]) - ord('0') if j >= 0 else 0
            res.append(total & 1)
            carry = total >> 1

            i -= 1
            j -= 1

        if carry == 1:
            res.append(1)

        return "".join([str(e) for e in res[::-1]])


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b:
            return a or b

        a, b, ans = a[::-1], b[::-1], []
        # carry: 进位
        i = j = carry = 0
        while i < len(a) or j < len(b) or carry:
            n1 = int(a[i]) if i < len(a) else 0
            n2 = int(b[j]) if j < len(b) else 0
            carry, cur = divmod(n1 + n2 + carry, 2)
            ans.append(str(cur))
            i += 1
            j += 1
        return ''.join(ans[::-1])


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b:
            return a or b
        a, b, res = a[::-1], b[::-1], []
        i = j = carry = 0
        while i < len(a) or j < len(b) or carry:
            n1 = int(a[i]) if i < len(a) else 0
            n2 = int(b[j]) if j < len(b) else 0
            _sum = n1 + n2 + carry
            carry = _sum >> 1
            res.append(str(_sum & 1))
            i += 1
            j += 1
        return ''.join(reversed(res))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b:
            return a or b
        a, b, res = a[::-1], b[::-1], []
        i = j = carry = 0
        while i < len(a) or j < len(b) or carry:
            n1 = ord(a[i]) - ord('0') if i < len(a) else 0
            n2 = ord(b[j]) - ord('0') if j < len(b) else 0
            _sum = n1 + n2 + carry
            carry = _sum >> 1
            res.append(str(_sum & 1))
            i += 1
            j += 1
        return ''.join(res[::-1])


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b:
            return a or b
        a, b, carry = a[::-1], b[::-1], 0
        i, j = 0, 0
        m, n = len(a), len(b)
        res = []
        while i < m or j < n:
            n1 = ord(a[i]) - ord('0') if i < m else 0
            n2 = ord(b[j]) - ord('0') if j < n else 0
            _sum = n1 + n2 + carry
            carry = _sum >> 1
            res.append(str(_sum & 1))
            i += 1
            j += 1
        if carry:
            res.append('1')
        return ''.join(reversed(res))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        i, j = m - 1, n - 1
        res = []
        carry = 0
        zero = ord('0')
        while i >= 0 or j >= 0:
            n1 = ord(a[i]) - zero if i >= 0 else 0
            n2 = ord(b[j]) - zero if j >= 0 else 0
            total = carry + n1 + n2
            carry = total >> 1
            res.append(str(total & 1))
            i -= 1
            j -= 1
        if carry:
            res.append('1')
        return ''.join(reversed(res))


def main():
    s = Solution()
    res = s.addBinary("1010", "1011")
    print(res)


if __name__ == '__main__':
    main()
