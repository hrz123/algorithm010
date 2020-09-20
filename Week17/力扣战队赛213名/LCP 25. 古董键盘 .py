# LCP 25. 古董键盘 .py
from functools import lru_cache


class Solution(object):
    def keyboard(self, k, n):
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(n, t):
            if n == 1:
                return sum(state[1:])
            res = 0
            for i in range(1, k + 1):
                if state[i]:
                    state[i] -= 1
                    state[i - 1] += 1
                    res += dfs(n - 1, tuple(state)) * (state[i] + 1)
                    state[i] += 1
                    state[i - 1] -= 1
            return res % mod

        state = [0] * k
        state.append(26)
        return dfs(n, tuple(state)) % mod


def main():
    sol = Solution()
    res = sol.keyboard(1, 2)
    print(res)

    res = sol.keyboard(1, 1)
    print(res)

    res = sol.keyboard(2, 2)
    print(res)

    res = sol.keyboard(5, 130)
    print(res)


if __name__ == '__main__':
    main()
