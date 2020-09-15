# 1316. 不同的循环子字符串.py


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)

        mod, base = 10 ** 9 + 7, 31
        pre, mul = [0] * (n + 1), [1] + [0] * n
        for i in range(1, n + 1):
            pre[i] = (pre[i - 1] * base + ord(text[i - 1])) % mod
            mul[i] = mul[i - 1] * base % mod

        def get_hash(l, r):
            return (pre[r + 1] - pre[l] * mul[r - l + 1] % mod + mod) % mod

        seen = {x: set() for x in range(n)}
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                l = j - i
                if j + l <= n:
                    hash_left = get_hash(i, j - 1)
                    if hash_left not in seen[l - 1] and hash_left == get_hash(j,
                                                                              j + l - 1):
                        ans += 1
                        seen[l - 1].add(hash_left)
        return ans


def main():
    pass


if __name__ == '__main__':
    main()
