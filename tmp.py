# tmp.py


class Solution:
    """
    @param num: sequence
    @return: The longest valley sequence
    """

    def valley(self, A):
        # write your code here
        N = len(A)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and A[end] > A[end + 1]:  # if base is a
                # left-boundary
                # set end to the peak of this potential mountain
                while end + 1 < N and A[end] > A[end + 1]:
                    end += 1
                if end + 1 < N and A[end] != A[end + 1]:
                    base = end + 1
                    continue
                end += 1
                if end + 1 < N and A[end] < A[end + 1]:
                    # if end is really a peak.
                    # set 'end' to right-boundary of mountain
                    while end + 1 < N and A[end] < A[end + 1]:
                        end += 1
                    # record candidate answer
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans


def main():
    sol = Solution()
    arr = [5,4,3,2,1,2,3,4,5]
    res = sol.valley(arr)
    print(res)


if __name__ == '__main__':
    main()
