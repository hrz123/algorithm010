# 1025. 除数博弈.py


# 思路：
# 我们先推几个
# 我们知道N=1时，先拿的人没有选择，一定为False
# N = 2时，开始的人选1，剩下1，先拿的人一定赢。
# 这里已经看出一些端倪了
# 我们再看3，先拿的人没有选择，留下2，先拿的人已经输了
# 到了4，先拿的人想赢，给后面的人留下3就可以了
# 所以看起来是偶数一定赢，奇数一定输
# 是如此吗？
# 证明：
# 因为两个都想赢
# 如果先手拿到偶数，就减1，那么给到后手一定是奇数，这时 a*b = 奇数，a和b都为奇数，
# (a-1)b和b(a-1)都是偶数，所以给到先手必须是偶数
# 只要先手不停减一，最后后手拿到1，必定输
# 如果先手拿到奇数，给到后手必定是偶数，根据上面讨论，偶数必赢
# 所以，偶数先手赢，奇数先手输
# 证明完毕
class Solution:
    def divisorGame(self, N: int) -> bool:
        return not N & 1


# 以下为自我练习
class Solution:
    def divisorGame(self, N: int) -> bool:
        return not N & 1


class Solution:
    def divisorGame(self, N: int) -> bool:
        return not N & 1


class Solution:
    def divisorGame(self, N: int) -> bool:
        return not N & 1


def main():
    pass


if __name__ == '__main__':
    main()
