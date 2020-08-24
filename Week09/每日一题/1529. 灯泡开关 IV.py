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


class Solution:
    def minFlips(self, target: str) -> int:
        pre = '0'
        c = 0
        for p in target:
            if p != pre:
                c += 1
            pre = p
        return c


# 以下为自我练习
class Solution:
    def minFlips(self, target: str) -> int:
        p = '0'
        s = 0
        for c in target:
            if c != p:
                s += 1
                p = c
        return s


class Solution:
    def minFlips(self, target: str) -> int:
        p = '0'
        res = 0
        for c in target:
            if c != p:
                res += 1
                p = c
        return res


def main():
    sol = Solution()

    target = "10111"
    res = sol.minFlips(target)
    print(res)
    assert res == 3

    target = "001011101"
    res = sol.minFlips(target)
    print(res)
    assert res == 5


if __name__ == '__main__':
    main()
