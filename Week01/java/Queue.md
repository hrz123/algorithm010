# java.util.Queue解析
java中 Queue 是一个接口，继承自java.util.Collection

```java
public interface Queue<E> extends Collection<E>
```
E为泛型的类型

包含如下几个方法要实现：
```java
boolean add(E e); // 入队一个元素，如果因为容量限制会throw exception
// IllegalStateException if the element cannot be added at this
// time due to capacity restrictions

boolean offer(E e); // 入队一个元素，如果因为容量限制会返回false

E remove(); // 出队一个元素，@throws NoSuchElementException if this queue is empty

E poll(); // 出队一个元素，@return the head of this queue, or <tt>null</tt> if this queue is empty

E element(); // 返回队头元素，但是不删除。@throws NoSuchElementException if this queue is empty

E peek(); // 返回队头元素，但是不删除。@return the head of this queue, or <tt>null</tt> if this queue is empty
```

