# 860. 柠檬水找零.py


# 暴力
# 模拟情景
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


def main():
    bills = [5, 5, 5, 10, 20]
    sol = Solution()
    res = sol.lemonadeChange(bills)
    print(res)


if __name__ == '__main__':
    main()
