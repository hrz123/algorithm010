# 278. 第一个错误的版本.py
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = l + ((r - l) >> 1)
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l


# 以下为自我练习
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = l + ((r - l) >> 1)
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = l + ((r - l) >> 1)
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = l + ((r - l) >> 1)
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = l + ((r - l) >> 1)
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = l + (r - l >> 1)
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l


def main():
    pass


if __name__ == '__main__':
    main()
