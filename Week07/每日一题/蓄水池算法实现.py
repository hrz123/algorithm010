# 蓄水池算法实现.py
import random


class ReservoirSampling(object):
    def sample(self, node, k):
        data = []
        # 计数器
        counter = 0
        while node:
            counter += 1
            # 前k个元素直接放入
            if counter <= k:
                data.append(node)
            else:
                # 判断第j个元素是否留下
                if random.randint(1, counter) <= k:
                    # 判断替换掉哪个元素
                    removed_idx = random.randint(0, k - 1)
                    # 替换该元素，放入新元素
                    data[removed_idx] = node
                # 如果不留下，就继续
            # 访问下一个node
            node = node.next
        return data


class ReservoirSampling(object):
    def sample(self, node, k):
        # 计数器
        count = 0
        data = []
        while node:
            count += 1
            if count <= k:
                data.append(node)
            else:
                # 每一个元素被放进去的概率是k/j
                if random.randint(1, count) <= k:
                    # 被移除的索引
                    removed_index = random.randint(0, k - 1)
                    # 替换掉
                    data[removed_index] = node
            node = node.next
        return data


def main():
    class ListNode(object):
        def __init__(self, val):
            self.val = val
            self.next = None

    head = ListNode(0)
    cur = head
    for i in range(1, 100):
        cur.next = ListNode(i)
        cur = cur.next
    rs = ReservoirSampling()
    res = rs.sample(head, 10)
    for node in res:
        print(node.val)


if __name__ == '__main__':
    main()
