# 学习笔记

note: 数据结构与算法目前是抄的学长的。在期末之前会自己重新总结一份。


数组和链表是数据结构最基础的两种数据结构，可以说其他的数据结构都是由这两种数据结构为基础。

数组的题较为多样，需要勤加练习。

链表的题目想法简单，但是实现比较考验细节，需要反复练习增加记忆

## 数组：
    O(1)的随机访问
    平均O(n)的插入和删除
    可被缓存加速访问

## 链表
	单向链表
		不支持随机访问
		O(1)插入和删除
		O(n)访问某个元素
		比数组占用更多存储空间
	双向链表
		每个节点多了指向前一个节点的指针
	循环链表
		尾节点指针指向头节点
	静态链表
		用数组描述的链表

## 跳表
    跳表出现的时间较平衡二叉树晚一些
    插入、删除、查找以及迭代输出有序序列，平衡二叉树和跳表一样，实现起来都是O(logn)的时间复杂度
    跳表额外可以做到快速按照区间查找数据。O(logn)的时间复杂度定位区间的起点，然后在原始链表中顺序向后遍历就可以。
    redis的有序集合是通过跳表来实现的

## 栈
    特点
        后进先出
        O(1)入栈出栈
    应用
        浏览器前进后退
        括号匹配
        表达式计算
## 队列
    普通队列
        特点
            先进先出
            O(1)入队出队
        应用
            LRU Cache
            操作有限资源
    双边队列
        入口和出口都可以入队和出队
    优先级队列
        根据优先级出队
