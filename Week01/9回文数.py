# 9回文数.py


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
