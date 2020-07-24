# 860. 柠檬水找零.py


# 暴力
# 模拟情景
from typing import List


class Solution(object):  # aw
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                if fives > 0:
                    fives -= 1
                    tens += 1
                else:
                    return False
            else:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True


def main():
    sol = Solution()

    bills = [5, 5, 5, 10, 20]
    res = sol.lemonadeChange(bills)
    print(res)

    bills = [5, 5, 10]
    res = sol.lemonadeChange(bills)
    print(res)

    bills = [10, 10]
    res = sol.lemonadeChange(bills)
    print(res)

    bills = [5, 5, 10, 10, 20]
    res = sol.lemonadeChange(bills)
    print(res)


if __name__ == '__main__':
    main()
