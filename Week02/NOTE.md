# 学习笔记

## 个人总结第一项
## Java HashMap实现，put和get方法看明白
### put方法

- put方法内部调用了putVal方法

  - 调用方式为：

    ```java
    public V put(K key, V value) {
      return putVal(hash(key), key, value, false, true);
    }
    ```

  - hash调用key这个类所有的hashCode方法。具体实现如下：

    ```java
    static final int hash(Object key) {
      int h;
      return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
    }
    ```

  - 在map中将这个特定的值与特定的键关联起来。如果map之前就有了一个对于这个键的映射，老的值会被替代。

  - 参数说明：

    - key: 要与这个特定value相关联的key
    - value：要与这个特定key相关联的value
    - return: 之前与这个key相关联的value，或者如果对于这个key没有映射就返回null。返回null也可能指示map之前将null与key相关联。

  - putVal内部实现。函数签名如下：

    ```java
    final V putVal(int hash, K key, V value, boolean onlyIfAbsent, boolean evict)
    ```

    ```java
    final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
                     boolean evict) {
        Node<K, V>[] tab;
        Node<K, V> p;
        int n, i;
        if ((tab = table) == null || (n = tab.length) == 0)
          n = (tab = resize()).length;
        if ((p = tab[i = (n - 1) & hash]) == null)
          tab[i] = newNode(hash, key, value, null);
        else {
          Node<K, V> e;
          K k;
          if (p.hash == hash &&
                  ((k = p.key) == key || (key != null && key.equals(k))))
            e = p;
          else if (p instanceof TreeNode)
            e = ((TreeNode<K, V>) p).putTreeVal(this, tab, hash, key, value);
          else {
            for (int binCount = 0; ; ++binCount) {
              if ((e = p.next) == null) {
                p.next = newNode(hash, key, value, null);
                if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                  treeifyBin(tab, hash);
                break;
              }
              if (e.hash == hash &&
                      ((k = e.key) == key || (key != null && key.equals(k))))
                break;
              p = e;
            }
          }
          if (e != null) { // existing mapping for key
            V oldValue = e.value;
            if (!onlyIfAbsent || oldValue == null)
              e.value = value;
            afterNodeAccess(e);
            return oldValue;
          }
        }
        ++modCount;
        if (++size > threshold)
          resize();
        afterNodeInsertion(evict);
        return null;
      }
    ```
    - 参数说明：
      - hash：key的哈希值
      - key：键
      - value：值
      - onlyIfAbsent：if true, don't change existing value
      - evict: if false, the table is in creation mode.
      - return: previous value, or null if none

  完整实现上，首先新建一个Node<K, V>[]数组tab。然后建立一个Node<K, V> p。

