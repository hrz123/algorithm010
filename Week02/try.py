# try.py
class Ugly(object):

    def __init__(self):
        self.nums = nums = [1]
        i2 = i3 = i5 = 0
        for _ in range(1, 1690):
            tmp2 = nums[i2] * 2
            tmp3 = nums[i3] * 3
            tmp5 = nums[i5] * 5
            ugly = min(tmp2, tmp3, tmp5)
            nums.append(ugly)

            if ugly == tmp2:
                i2 += 1
            if ugly == tmp3:
                i3 += 1
            if ugly == tmp5:
                i5 += 1


class Solution:
    u = Ugly()

    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n - 1]


def main():
    pass


if __name__ == '__main__':
    main()
