# 亚马逊面试题.py
import heapq
from collections import defaultdict
from typing import List


class Solution(object):
    def findCompetitors(
            self,
            numCompetitors: int,
            topNCompetitors: int,
            competitors: List[str],
            numReviews: int,
            reviews: List[str]
    ) -> List[str]:
        # 用来计数
        counter = defaultdict(int)
        # hashset方便查找
        competitors = set(competitors)
        # 计数，出现在同一review中多次视为1次
        for review in reviews:
            visited = set()
            for word in review.split():
                if word in competitors and word not in visited:
                    counter[word] += 1
                    visited.add(word)
        # 取数目前topNCompetitors个，堆
        # return heapq.nlargest(topNCompetitors, counter, counter.build)
        # 或者手动，size为k的小顶堆，大于小顶堆顶部的就加入并pop顶部元素
        res = []
        for k, v in counter.items():
            if len(res) == topNCompetitors:
                heapq.heappushpop(res, (v, k))
            else:
                heapq.heappush(res, (v, k))
        return [ans[1] for ans in res]


def main():
    a = 5
    b = 2
    c = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
    d = 3
    e = ["Best services provided by anacell",
         "betacellular has great services",
         "anacell provides much better services than all other"]
    sol = Solution()
    res = sol.findCompetitors(a, b, c, d, e)
    print(res)

    a = 5
    b = 2
    c = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
    d = 5
    e = ["I love anacell Best services provided by anacell in the town",
         "betacellular has great services",
         "deltacellular provides much better services that betacellular",
         "cetracular is worse than eurocell",
         "betacellular is better than deltacellular"]
    res = sol.findCompetitors(a, b, c, d, e)
    print(res)


if __name__ == '__main__':
    main()
