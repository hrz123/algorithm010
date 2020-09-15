# LCP 17. 速算机器人 .py


class Solution:
    def calculate(self, s: str) -> int:
        x, y = 1, 0
        for c in s:
            if c == 'A':
                x = x * 2 + y
            else:
                y = y * 2 + x
        return x + y


def main():
    pass


if __name__ == '__main__':
    main()
