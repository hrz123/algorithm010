# 43. 字符串相乘.py


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = n2 = 0
        for c in num1:
            n1 = n1 * 10 + ord(c) - ord('0')
        for c in num2:
            n2 = n2 * 10 + ord(c) - ord('0')
        return str(n1 * n2)


def main():
    sol = Solution()
    num1 = "2"
    num2 = "3"
    res = sol.multiply(num1, num2)
    print(res)


if __name__ == '__main__':
    main()
