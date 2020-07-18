# 125. 验证回文串.py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


def main():
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    res = sol.isPalindrome(s)
    print(res)

    s = "race a car"
    res = sol.isPalindrome(s)
    print(res)


if __name__ == '__main__':
    main()
