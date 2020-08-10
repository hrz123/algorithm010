n = int(input())
arr = []
for _ in range(n):
    a, b, g, k = map(int, input().split())
    arr.append((a, b, g, k))
x, y = map(int, input().split())
for i in range(n - 1, -1, -1):
    if arr[i][0] <= x < arr[i][2] + arr[i][0] and arr[i][1] <= y < arr[i][1] + \
            arr[i][3]:
        print(i + 1)
        break
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
