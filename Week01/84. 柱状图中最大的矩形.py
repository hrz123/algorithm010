# 84. 柱状图中最大的矩形.py
from typing import List


# 方法一：暴力
# 依次遍历柱形的高度，对于每一个高度分别向两边扩散，求出以当前高度为矩形的最大宽度为多少
# 为此，我们需要：
# 1.左边看一下，看最多能向左延伸多长，找到大于等于当前柱形高度的最左边元素的下标
# 2.右边看一下，看最多能向右延伸多长，找到大于等于当前柱形高度的最右边元素的下标
# 对于每一个位置，我们都这样操作，得到一个矩形面积，求出它们的最大值
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0

        for i in range(size):
            cur_height = heights[i]

            left = i
            while left > 0 and heights[left - 1] >= cur_height:
                left -= 1
            right = i
            while right < size - 1 and heights[right + 1] >= cur_height:
                right += 1

            res = max(res, cur_height * (right - left + 1))

        return res


# python代码不能得到通过
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)


# 方法二：以空间换时间
# 单调栈，典型
# 我们拿示例的数组[2,1,5,6,2,3]为例
# 1.一开始看到的柱形高度为2，这个时候以这个2为高度的最大面积还不能确定，我们需要继续向右遍历
# 2.然后看到高度为1的柱形，这个时候以这个柱形委高度的句型的最大面积还是不知道的。但是它之前的
#   以2为高度的最大面积的句型是可以确定的，这是因为这个1比2小，因为这个1卡在了这里，2不能再向
#   右边扩展了
#   我们计算一下以2为高度的最大矩形的面积是2。这个时候，求解这个问题的思路已经慢慢打开了。
#   遍历到高度为5的句型，同样的以当前看到柱形为高度的句型的最大面积也是不知道的，因为我们还要看
#   右边高度的情况。那么它的左右有没有可以确定的柱形呢？没有，这是因为5比1大，
#   我们看后面马上就出现了6，不管是1还是5的柱形，都可以向右边扩展
#   接下来，遍历到高度为6的柱形，同样的，以柱形1，5，6位高度的最大巨星面积还是不能确定下来
#   再接下来，遍历到高度为2的柱形
#   高度为6的柱形对应的最大矩形的面积的宽度可以确定下来，它就是夹在高度为5的柱子和高度为2的柱子
#   之间的距离，它的高度是6，宽度是1
#   接下来5对应的最大面积的矩形的宽度也可以确定下来，它是夹在高度为1和高度为2的两个柱形
#   之间的距离
#   我们发现了，只要是遇到了当前柱形的高度比它上一个柱形的高度严格小的时候
#   一定可以确定它之前的某些柱形的最大宽度，并且确定的柱形宽度的顺序是从右边向左边
#   这个现象告诉我们，在遍历的时候需要记录的信息就是遍历到的柱形的下标
#   它一左一右的两个柱形的下标的差就是这个面积最大矩形对应的最大宽度。（注意是一左一右）
#   这个时候，还需要考虑的一个细节是，在确定一个柱形的面积的时候，除了右边要比当前严格小
#   其实还蕴含了一个条件，那就是左边也要比当前高度严格小
#   那如果左边的高度和自己相等怎么办呢？我们想一想，我们之前是只要比当前严格小，我们才可以确定
#   一些柱形的最大宽度。只要是大于或者等于之前看到的那一个柱形的高度的时候，我们其实都不能确定。
#   因此我们确定当前柱形对应的宽度的左边界的时候，网回头看的时候，
#   一定要找到第一个严格小于我们要确定的那个柱形的高度的下标。
#   这个时候中间的那些相等的柱形其实就可以当做不存在一样。
#   因为它对应的最大矩形和它对应的最大矩形其实是一样的。
#   说道这里，其实思路已经慢慢清晰了。
#   我们在遍历的时候，需要记录的是下标，如果当前的高度比它之前的高度严格小于的时候，
#   就可以直接确定之前的那个高度的矩形的最大矩形的面积，为了确定这个最大矩形的左边界，我们还要找到
#   第一个严格小于它的高度的柱形，向左回退的时候，其实就可以当中间的这些助兴不存在一样。
#   这是因为我们就是想确定 6 的宽度，6 的宽度确定完了，其实我们就不需要它了，
#   这个 5 的高度和这个 5 的高度确定完了，我们也不需要它了。
#   我们在缓存数据的时候，是从左向右缓存的，我们计算出一个结果的顺序是从右向左的，
#   并且计算完成以后我们就不再需要了，符合后进先出的特点。
#   因此，我们需要的这个作为缓存的数据结构是栈。
#   当确定了一个柱形的高度的时候，我们就将它从栈顶移出，所有的柱形在栈中进栈一次，出栈一次
#   一开始栈为空，最后也一定要让栈为空，表示这个高度数组里所有的元素都考虑完了。
#   最后遍历到最后一个柱形，即高度为3的柱形。
#   接下来我们就要一次考虑还在栈里的柱形的高度。和刚才的方法一样，只不过这个时候右边
#   没有比它高度还小的柱形了，这个时候计算宽度应该假设最后边还有一个下标为len（这里为6）
#   的高度为0（或者0.5，只要比1小）的柱形
#   下标为5，高度为3的柱形，左边的下标定位4，右边的小标为6，因此宽度是6 -4 - 1 = 1
#   （两边都不算，只算中间的距离，所以减1）；算完以后，将它标为虚线
#   下标为4高度为2的柱形，左边的下标为1，右边的下标为6，因此宽度是6 - 1 - 1 = 4；算完以后
#   将它标为虚线
#   最后看下标为1，高度为1的矩形，它的左边和有伴其实都没有元素了，它就是整个柱形数组里面
#   高度最低的柱形，计算它的宽度，就是整个柱形数组的长度。
#   到此为止，所有的柱形高度对应的最大矩形的面积就都计算出来了。
#   这个算法经过一次遍历，在每一次计算最大宽度的时候，没有去遍历，而是使用了站里存放的下标信息，
#   以O(1)的时间复杂度计算最大宽度。

# 不用哨兵
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        size = len(heights)
        stack = []

        for i in range(size):
            # 只要新来的比旧的小，就有一部分最大宽度已经确定了
            while stack and heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1 if stack else i
                res = max(res, cur_height * cur_width)
            # 如果前面没有了，直接加进去
            stack.append(i)

        # 处理剩余的，以最右侧为边界
        while stack:
            cur_height = heights[stack.pop()]
            cur_width = size - stack[-1] - 1 if stack else size
            res = max(res, cur_height * cur_width)

        return res


# 左侧使用哨兵
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        size = len(heights)
        stack = [-1]

        for i in range(size):
            while len(stack) > 1 and heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)

        while len(stack) > 1:
            cur_height = heights[stack.pop()]
            cur_width = size - stack[-1] - 1
            res = max(res, cur_height * cur_width)

        return res


# 左右使用哨兵
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        res = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)

        # 这一步为还原heights
        heights.pop()
        return res


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            cur = heights[i]
            while cur < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans


# 以下为自我练习
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        res = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)

        heights.pop()
        return res


# 除了stack
# 不使用任何额外空间
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        size = len(heights)
        stack = []

        for i in range(size):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                res = max(res, h * w)
            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            w = size - stack[-1] - 1 if stack else size
            res = max(res, h * w)

        return res


def main():
    heights = [2, 1, 5, 6, 2, 3]
    sol = Solution()
    res = sol.largestRectangleArea(heights)
    print(res)


if __name__ == '__main__':
    main()
