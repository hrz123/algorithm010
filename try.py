m, n, x, y = map(int, input().split())
obs = {(x + dx, y + dy) for dx, dy in ((1, 2), (1, -2), (-1, 2), (-1, -2),
                                       (2, 1), (2, -1), (-2, 1), (-2, -1),
                                       (0, 0))}
m += 1
n += 1

dp = [0, 1] + [0] * (n - 1)
for i in range(m):
    for j in range(n):
        dp[j + 1] = dp[j] + dp[j + 1] if (i, j) not in obs else 0
print(dp[n])


def main():
    pass


if __name__ == '__main__':
    main()

# Output:
# Vertex tDistance from Source
# 0 t 0
# 1 t 4
# 2 t 12
# 3 t 19
# 4 t 21
# 5 t 11
# 6 t 9
# 7 t 8
# 8 t 14
