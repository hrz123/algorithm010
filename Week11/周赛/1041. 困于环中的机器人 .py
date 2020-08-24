# 1041. 困于环中的机器人 .py


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        x, y = 0, 0
        k = 0
        for c in instructions * 4:
            if c == 'G':
                x += dirs[k][0]
                y += dirs[k][1]
            elif c == 'L':
                k = (k - 1) % 4
            else:
                k = (k + 1) % 4
        if x == 0 and y == 0:
            return True
        return False


def main():
    pass


if __name__ == '__main__':
    main()
