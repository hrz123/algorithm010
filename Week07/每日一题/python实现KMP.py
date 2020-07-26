# python实现KMP.py


# Python program for KMP Algorithm
def get_lps(p, m):
    lps = [-1] * m
    k = -1
    for i in range(1, m):
        while k != -1 and p[k + 1] != p[i]:
            k = lps[k]
        if p[k + 1] == p[i]:
            k += 1
        lps[i] = k
    return lps


def KMPSearch(p, s):
    m = len(p)
    n = len(s)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = get_lps(p, m)

    j = 0  # index for p[]
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = lps[j - 1] + 1
        if s[i] == p[j]:
            j += 1
        if j == m:
            # print("Found pattern at index " + str(i - j + 1))
            # j = lps[j - 1] + 1
            return i - m + 1
    return -1


def main():
    s = "ABABDABACDABABCABAB"
    p = "ABABCABAB"
    res = KMPSearch(p, s)
    print(res)


if __name__ == '__main__':
    main()
