# 2.py
class Solution:
    """
    @param n: The folding times
    @return: the 01 string
    """

    def getString(self, n):
        # Write your code here
        def printProcess(i, N, down):
            if i > N:
                return
            printProcess(i + 1, N, True)
            if down is True:
                res.append('0')
            else:
                res.append('1')
            printProcess(i + 1, N, False)

        res = []
        printProcess(1, n, True)
        return "".join(res)


#
#
# def printAllFolds(N):
#     printProcess(1, N, True)
#     print()
#
#
# def printProcess(i, N, down):
#     if i > N:
#         return
#     printProcess(i + 1, N, True)
#     if down is True:
#         print('down', end=' ')
#     else:
#         print('up', end=' ')
#     printProcess(i + 1, N, False)


# 简单测试
if __name__ == '__main__':
    sol = Solution()
    res = sol.getString(3)
    print(res)
