# 38. 外观数列.py


class Solution:
    def countAndSay(self, n: int) -> str:
        s, ns = ['1'], []
        for _ in range(n - 1):
            count, pre = 0, None
            for c in s:
                if c == pre:
                    count += 1
                else:
                    if pre is not None:
                        ns.append(str(count))
                        ns.append(str(pre))
                    pre, count = c, 1
            ns.append(str(count))
            ns.append(str(pre))
            s, ns = ns, []
        return ''.join(s)


def main():
    sol = Solution()
    n = 4
    res = sol.countAndSay(n)
    print(res)

    n = 5
    res = sol.countAndSay(n)
    print(res)

    n = 1
    res = sol.countAndSay(n)
    print(res)


if __name__ == '__main__':
    main()
