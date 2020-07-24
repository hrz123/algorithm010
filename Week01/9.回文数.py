# 9.回文数.py


# 国际站解法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special cases:
        # When x < 0, x is not a palindrome.
        # Also if the last digit of the number is 0, in order to be a palindrome,
        # the first digit of the number also needs to be 0.
        # Only 0 satisfy this property.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        # since the middle digit doesn't matter in palindrome (it will always equal to itself), we can simply getrid of it.
        return x == revertedNumber or x == revertedNumber // 10


# 我的解法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special cases:
        # When x < 0, x is not a palindrome.
        # Also if the last digit of the number is 0, in order to be a palindrome,
        # the first digit of the number also needs to be 0.
        # Only 0 satisfy this property.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            x, mod = divmod(x, 10)
            revertedNumber *= 10
            revertedNumber += mod

        # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        # since the middle digit doesn't matter in palindrome (it will always equal to itself), we can simply getrid of it.
        return x == revertedNumber or x == revertedNumber // 10


# 以下为自我练习
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            x, mod = divmod(x, 10)

            reverted_number *= 10
            reverted_number += mod

        return x == reverted_number or x == reverted_number // 10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:
            x, mod = divmod(x, 10)
            rev *= 10
            rev += mod
        return rev == x or rev // 10 == x


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 and (not x % 10 and x != 0):
            return False
        rev = 0
        while x > rev:
            x, mod = divmod(x, 10)
            rev *= 10
            rev += mod
        return x == rev or x == rev // 10


def main():
    s = Solution()
    res = s.isPalindrome(121)
    print(res)
    res = s.isPalindrome(123)
    print(res)
    res = s.isPalindrome(-121)
    print(res)
    res = s.isPalindrome(0)
    print(res)


if __name__ == '__main__':
    main()
