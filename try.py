n = int(input())
hashmap = {}
for ind in range(n):
    a, b, g, k = map(int, input().split())
    for i in range(a, a + g):
        for j in range(b, b + k):
            hashmap[(i, j)] = ind + 1
x, y = map(int, input().split())
if (x, y) in hashmap:
    print(hashmap[x, y])
else:
    print(-1)


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
