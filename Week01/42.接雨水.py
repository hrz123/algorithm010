# 42.接雨水.py

from typing import List


# 暴力法
# 直接按问题描述进行。对于数组中的每个元素，我们找出下雨后水能达到的最高位置，等于两边最大高度的较小值减去当前高度的值。

# 算法：
# 初始化 ans = 0
# 从左向右扫描数组：
#    初始化 max_Left = 0 和 max_right = 0
#    从当前元素向左扫描并更新：
#        max_left = max(max_left, height[j])
#    从当前元素向右扫描并更新：
#        max_right = max(max_right, height[j])
#    将min(max_left, max_right) - height[i] 累加到 ans

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
# 因此我们可以弹出栈顶元素并且累加答案到 \text{ans}ans 。

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
# 从动态编程方法的示意图中我们注意到，只要 right_max[i] > left_max[i]（元素 0 到元素 6），积水高度将由 left_max
# 决定，类似地 left_max[i] > right_max[i]，由right_max决定（元素 8 到元素 11）。
# 所以我们可以认为如果一端有更高的条形块（例如右端），积水的高度依赖于当前方向的高度（从左到右）。当我们发现另一侧（右侧）的条形块高度不是最高的，我们则开始从相反的方向遍历（从右到左）。
# 我们必须在遍历时维护 left_max 和 right_max ，但是我们现在可以使用两个指针交替进行，实现 1 次遍历即可完成。

# 算法：
#     初始化left指针为0，并且right指针为size-1
#     while left < right, do:
#         if height[left] < height[right]:
#             if height[left] >= left_max, 更新left_max
#             else: 累加left_max - height[left] 到 ans
#             left += 1
#         else:
#             if height[right] >= right_max，更新right_max
#             else 累加right_max - height[right] 到 ans
#             right -= 1
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


def main():
    heights = [4, 2, 3]
    s = Solution()
    res = s.trap(heights)
    print(res)


if __name__ == '__main__':
    main()
