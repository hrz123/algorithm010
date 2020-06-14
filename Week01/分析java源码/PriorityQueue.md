# jdk 10 PriorityQueue解析

文档[链接](https://docs.oracle.com/javase/10/docs/api/java/util/PriorityQueue.html)


## java 优先级队列 Class
    是Queue接口的实现

### 构造函数
- 有7中构造函数
- PriorityQueue() 没有任何参数
- PriorityQueue​(int initialCapacity) 传入容量
- PriorityQueue​(int initialCapacity, Comparator<? super E> comparator) 传入容量和比较器
- PriorityQueue​(Collection<? extends E> c) 通过Collection类创建
- PriorityQueue​(Comparator<? super E> comparator) 只传入比较器
- PriorityQueue​(PriorityQueue<? extends E> c) 传入一个优先级队列
- PriorityQueue​(SortedSet<? extends E> c) 传入一个排序集合

### 主要方法
- boolean add(E e) 添加一个元素到优先级队列，容量限制抛异常
- void clear() 清除优先级队列中的所有元素
- Comparator<? super E>	comparator() 返回优先及队列的比较器
- boolean contains​(Object o) 返回true如果优先级队列包含此元素
- Iterator<E>	iterator() 返回一个队列元素的迭代器
- boolean offer​(E e) 添加一个元素到优先级队列，容量限制返回false
- boolean remove​(Object o) 删除一个指定元素，如果它存在的话
- Spliterator<E> spliterator()	在这个队列中的元素上创建一个延迟绑定和快速失效的Spliterator。（没太明白是什么意思）
- Object[]	toArray() 返回一个队列中所有元素的数组
- <T> T[]	toArray​(T[] a) 返回一个包含该队列中所有元素的数组；返回数组的运行时类型是指定数组的类型。