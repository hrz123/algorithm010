# 面试题 16.18. 模式匹配.py


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        cnta, cntb, n = 0, 0, len(value)  # 计算a和b的个数，n为value长度
        for ch in pattern:
            if ch == 'a':
                cnta += 1
            else:
                cntb += 1

        if n == 0:  # 判断各种边界情况，pattern或者value为空
            return cnta * cntb == 0
        else:
            if cnta == 0 and cntb == 0:
                return False
            elif cnta == 0 or cntb == 0:  # 判断pattern全是a或者全是b的情况
                if cnta == 0:
                    cnta, cntb = cntb, cnta  # 如果cnta为0，两者调换一下
                if n % cnta != 0:  # 不能整除的情况
                    return False
                d, judge = n // cnta, set()  # 用集合来判断是否有第二种字符串出现
                for i in range(cnta):
                    judge.add(value[i * d:i * d + d - 1])
                    if len(judge) > 1: break
                return len(judge) == 1  # 如果自始至终只有一种字符串，那么就是True

        for i in range(0, n // cnta + 1):  # 一般情况
            if (n - i * cnta) % cntb == 0:  # 只判断能整除的情况
                j = (n - i * cnta) // cntb
                cur, judge = 0, set()
                for ch in pattern:  # 用集合来判断是否有第三种字符串出现
                    if ch == 'a':
                        judge.add(value[cur:cur + i])
                        cur += i
                    else:
                        judge.add(value[cur:cur + j])
                        cur += j
                    if len(judge) > 2: break
                if len(judge) == 2: return True  # 如果自始至终只有两种字符串，那么就是True
        return False


def main():
    pass


if __name__ == '__main__':
    main()
