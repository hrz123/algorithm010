# 1529. 灯泡开关 IV.py


class Solution:
    def minFlips(self, target: str) -> int:
        steps = 0
        flag = '1'
        for c in target:
            if c == flag:
                steps += 1
                flag = '0' if flag == '1' else '1'
        return steps


def main():
    sol = Solution()

    target = "10111"
    res = sol.minFlips(target)
    print(res)

    target = "001011101"
    res = sol.minFlips(target)
    print(res)


if __name__ == '__main__':
    main()
