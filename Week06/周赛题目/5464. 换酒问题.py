# 5464. 换酒问题.py


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        res += numBottles
        empty = numBottles
        while empty >= numExchange:
            div, empty = divmod(empty, numExchange)
            res += div
            empty += div
        return res


class Solution:
    def numWaterBottles(self, b: int, e: int) -> int:
        res = 0
        a = 0
        while True:
            if b == 0 and a < e:
                break
            res += b
            a += b
            b = a // e
            a -= b * e

        return res


def main():
    sol = Solution()

    numBottles = 9
    numExchange = 3
    res = sol.numWaterBottles(numBottles, numExchange)
    print(res)

    numBottles = 15
    numExchange = 4
    res = sol.numWaterBottles(numBottles, numExchange)
    print(res)

    numBottles = 5
    numExchange = 5
    res = sol.numWaterBottles(numBottles, numExchange)
    print(res)

    numBottles = 2
    numExchange = 3
    res = sol.numWaterBottles(numBottles, numExchange)
    print(res)


if __name__ == '__main__':
    main()
