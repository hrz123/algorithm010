# 42.接雨水.py

from typing import List


# 暴力法
# 直接按问题描述进行。对于数组中的每个元素，我们找出下雨后水能达到的最高位置，等于两边最大高度的较小值减去当前高度的值。

# 算法：
# 初始化 pre = 0
# 从左向右扫描数组：
#    初始化 max_Left = 0 和 max_right = 0
#    从当前元素向左扫描并更新：
#        max_left = max(max_left, height[j])
#    从当前元素向右扫描并更新：
#        max_right = max(max_right, height[j])
#    将min(max_left, max_right) - height[start] 累加到 pre

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        size = len(height)

        for i in range(1, size - 1):
            max_left = max_right = 0
            for j in range(i, -1, -1):
                max_left = max(max_left, height[j])
            for j in range(i, size):
                max_right = max(max_right, height[j])
            ans += min(max_left, max_right) - height[i]

        return ans


# 时间复杂度： O(n^2)
# 空间复杂度： O(1)
# leetcode 超出时间限制


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        ans = 0
        size = len(height)

        left_max = [0] * size
        right_max = [0] * size

        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i - 1])
        right_max[size - 1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans


# 复杂度分析
# 时间复杂度：O(n)
#   存储最大高度数组，需要两次遍历，每次O(n)
#   最终使用存储的数据更新ans，O(n)
#   所以总共是O(n)
# 空间复杂度：O(n)
# 使用额外O(n)的空间来放置left_max和right_max数组

# 使用栈的解法
# 我们可以不用像方法 2 那样存储最大高度，而是用栈来跟踪可能储水的最长的条形块。
# 使用栈就可以在一次遍历内完成计算。

# 我们在遍历数组时维护一个栈。如果当前的条形块小于或等于栈顶的条形块，我们将条形块的索引入栈，
# 意思是当前的条形块被栈中的前一个条形块界定。如果我们发现一个条形块长于栈顶，
# 我们可以确定栈顶的条形块被当前条形块和栈的前一个条形块界定，
# 因此我们可以弹出栈顶元素并且累加答案到 \text{pre}pre 。

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        current = 0
        stack = []
        size = len(height)

        while current < size:
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break

                distance = current - stack[-1] - 1
                bounded_height = min(height[current],
                                     height[stack[-1]]) - height[top]
                ans += distance * bounded_height

            stack.append(current)
            current += 1
        return ans


# 时间复杂度： O(n)
# 单词遍历O(n)，每个条形块最多访问两次（栈的弹入和弹出），并且出栈和入栈都是O(1)
# 空间复杂度：O(n)
# 栈最多在阶梯型或者平坦型条形块结构中占用O(n)的空间


# 和方法 2 相比，我们不从左和从右分开计算，我们想办法一次完成遍历。
# 从动态编程方法的示意图中我们注意到，只要 right_max[start] > left_max[start]（元素 0 到元素 6），积水高度将由 left_max
# 决定，类似地 left_max[start] > right_max[start]，由right_max决定（元素 8 到元素 11）。
# 所以我们可以认为如果一端有更高的条形块（例如右端），积水的高度依赖于当前方向的高度（从左到右）。当我们发现另一侧（右侧）的条形块高度不是最高的，我们则开始从相反的方向遍历（从右到左）。
# 我们必须在遍历时维护 left_max 和 right_max ，但是我们现在可以使用两个指针交替进行，实现 1 次遍历即可完成。

# 算法：
#     初始化left指针为0，并且right指针为size-1
#     while r < r, do:
#         if height[r] < height[r]:
#             if height[r] >= left_max, 更新left_max
#             else: 累加left_max - height[r] 到 pre
#             r += 1
#         else:
#             if height[r] >= right_max，更新right_max
#             else 累加right_max - height[r] 到 pre
#             r -= 1
class Solution:
    def trap(self, height: List[int]) -> int:
        left = right = res = 0
        i, j = 0, len(height) - 1
        while i < j:
            v_left, v_right = height[i], height[j]
            if v_left < v_right:
                if v_left >= left:
                    left = v_left
                else:
                    res += left - v_left
                i += 1

            else:
                if v_right >= right:
                    right = v_right
                else:
                    res += right - v_right
                j -= 1
        return res


# 双指针的另一种解法
class Solution:
    def trap(self, height: List[int]) -> int:
        left = right = res = 0
        i, j = 0, len(height) - 1
        while i < j:
            left, right = max(left, height[i]), max(right, height[j])
            while i < j and height[i] <= left <= right:
                res += left - height[i]
                i += 1
            while i < j and height[j] <= right <= left:
                res += right - height[j]
                j -= 1
        return res


# 以下为自我练习遍数

# 解法：
# 暴力法
# 对于任何一根不是最左和最后的柱子
# 向左向右都找到局部最高点，算出当前柱子的盛水量

# 左右指针法
# 可以这么理解，对于任何位置，需要知道其左右最大值
# 对于i位置，左侧最大值一定在0..start-1，右侧最大值一定在i+1..mask-1
# 并且决定i位置加多少水的，是左右最大值的较小者
# 用双指针法：
# l, row
# 到l位置左侧的最大值为left
# 到r位置右侧的最大值为right
# r = max(r, height[start])
# r = max(r, height[start])
# 左侧更小，左侧的边界已经确定了就是left，而右侧的最大肯定比right大
# 所以此时l处的水量可以更新
# 往后推进只要height[l]依然小于等于left
# l < row and height[l] <= r <= r
# pre += r - height[l]
# l += 1
# 右侧更小，右侧的边界已经确定了就是right，而左侧的最大肯定比left大
# 往后推进只要height[row]依然小于等于right
# l < row and height[row] <= r <= r
# pre += r - height[row]
# row -= 1

# 这两个必有一个可以满足
# 因为height[l]在一开始的时候，r = max(r, height[l])
# 所以height[l] <= r
# 同理，height[row] <= r
# 所以 相当于left<=right和right<=r
# 必然进入其中一个分支
# 而 l < row 是在 l += 1中防止越界的
# 只要height[l] <= left就可以继续
# 大于left说明此时左侧最大发生了变化，需要进行迭代，更新左侧最大
# 而在l自增的过程中left和right不会变化
# 右侧同理

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        size = len(height)

        for i in range(1, size - 1):
            max_left = max_right = 0
            for j in range(i, -1, -1):
                max_left = max(max_left, height[j])
            for j in range(i, size):
                max_right = max(max_right, height[j])
            ans += min(max_left, max_right) - height[i]

        return ans


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left = right = res = 0
        while l < r:
            left, right = max(left, height[l]), max(right, height[r])
            while l < r and height[l] <= left <= right:
                res += left - height[l]
                l += 1
            while l < r and height[r] <= right < left:
                res += right - height[r]
                r -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left = right = res = 0

        while l < r:
            left, right = max(left, height[l]), max(right, height[r])

            while l < r and height[l] <= left <= right:
                res += left - height[l]
                l += 1
            while l < r and height[r] <= right < left:
                res += right - height[r]
                r -= 1

        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left = right = res = 0

        while l < r:
            left, right = max(left, height[l]), max(right, height[r])

            while l < r and height[l] <= left <= right:
                res += left - height[l]
                l += 1

            while l < r and height[r] <= right < left:
                res += right - height[r]
                r -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        # 不断记录左右两侧的最高值
        left = right = res = 0
        while l < r:
            left, right = max(left, height[l]), max(right, height[r])

            while l < r and height[l] <= left <= right:
                res += left - height[l]
                l += 1

            while l < r and height[r] <= right <= left:
                res += right - height[r]
                r -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max = right_max = res = 0
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            while l < r and height[l] <= left_max <= right_max:
                res += left_max - height[l]
                l += 1
            while l < r and height[r] <= right_max <= left_max:
                res += right_max - height[r]
                r -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        res = 0
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            while l < r and height[l] <= left_max <= right_max:
                res += left_max - height[l]
                l += 1
            while l < r and height[r] <= right_max <= left_max:
                res += right_max - height[r]
                r -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = 0
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            while l < r and height[l] <= left_max <= right_max:
                res += left_max - height[l]
                l += 1
            while l < r and height[r] <= right_max <= left_max:
                res += right_max - height[r]
                r -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = 0
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            while l < r and height[l] <= left_max <= right_max:
                res += left_max - height[l]
                l += 1
            while l < r and height[r] <= right_max <= left_max:
                res += right_max - height[r]
                r -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = 0
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            left_max = max(height[l], left_max)
            right_max = max(height[r], right_max)
            while l < r and height[l] <= left_max <= right_max:
                res += left_max - height[l]
                l += 1
            while l < r and height[r] <= right_max <= left_max:
                res += right_max - height[r]
                r -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                tmp = height[stack.pop()]
                if stack:
                    bound = min(h, height[stack[-1]])
                    res += (bound - tmp) * (i - stack[-1] - 1)
            stack.append(i)
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = 0
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            while l < r and height[l] <= left_max <= right_max:
                res += left_max - height[l]
                l += 1
            while l < r and height[r] <= right_max <= left_max:
                res += right_max - height[r]
                r -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        for i in range(n):
            left_max[i] = max(left_max[i - 1] if i > 0 else 0, height[i])
        for i in range(n - 1, -1, -1):
            right_max[i] = max(right_max[i + 1] if i < n - 1 else 0, height[i])
        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = 0
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            while l < r and height[l] <= left_max <= right_max:
                res += left_max - height[l]
                l += 1
            while l < r and height[r] <= right_max <= left_max:
                res += right_max - height[r]
                r -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                tmp = height[stack.pop()]
                if stack:
                    bound = min(h, height[stack[-1]])
                    res += (bound - tmp) * (i - stack[-1] - 1)
            stack.append(i)
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                tmp = height[stack.pop()]
                if stack:
                    res += (min(height[stack[-1]], h) - tmp) * (
                            i - stack[-1] - 1)
            stack.append(i)
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = 0
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            while l < r and height[l] <= left_max <= right_max:
                res += left_max - height[l]
                l += 1
            while l < r and height[r] <= right_max <= left_max:
                res += right_max - height[r]
                r -= 1
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                p = height[stack.pop()]
                if stack:
                    res += (min(h, height[stack[-1]]) - p) * (i - stack[-1] - 1)
            stack.append(i)
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = 0
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            while l < r and height[l] <= left_max <= right_max:
                res += left_max - height[l]
                l += 1
            while l < r and height[r] <= right_max <= left_max:
                res += right_max - height[r]
                r -= 1
        return res


def main():
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    res = s.trap(heights)
    print(res)


if __name__ == '__main__':
    main()
