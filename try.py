# n = int(input())
# arr = []
# for _ in range(n):
#     a, b, g, k = map(int, input().split())
#     arr.append((a, b, g, k))
# x, y = map(int, input().split())
# for i in range(n - 1, -1, -1):
#     if arr[i][0] <= x < arr[i][2] + arr[i][0] and arr[i][1] <= y < arr[i][1] + \
#             arr[i][3]:
#         print(i + 1)
#         break
# else:
#     print(-1)


# 定义子问题
# f(i)的解码方法
# f(i)= f(i-1) if s[i] != '0'
#  + f(i-2) if int(s[i-1:i+1])在10和26之间
# 初始化
# f(0) = 1
# f(1) = 1 or 0
# 返回值f(n)
# 优化复杂度
# 只需要两个值
import random


def jump(start, left, right, times=10 ** 5):
    go_right = 0
    go_left = 0
    for i in range(times):
        t = start
        while t != left and t != right:
            ran = random.randint(0, 1)
            if ran == 1:
                t += 1
            else:
                t -= 1
        if t == left:
            go_left += 1
        else:
            go_right += 1
        print(t == left)
    total = go_left + go_right
    return go_left / total, go_right / total


def main():
    res = jump(3, 0, 8)
    print(res)


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
