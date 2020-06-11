   1: /*
   2:  * Written by Doug Lea with assistance from members of JCP JSR-166
   3:  * Expert Group and released to the public domain, as explained at
   4:  * http://creativecommons.org/licenses/publicdomain
   5:  */
   6:
   7: package java.util;
   8:
   9: /**
  10:  * A collection designed for holding elements prior to processing.
  11:  * Besides basic {@link java.util.Collection Collection} operations,
  12:  * queues provide additional insertion, extraction, and inspection
  13:  * operations.  Each of these methods exists in two forms: one throws
  14:  * an exception if the operation fails, the other returns a special
  15:  * value (either <tt>null</tt> or <tt>false</tt>, depending on the
  16:  * operation).  The latter form of the insert operation is designed
  17:  * specifically for use with capacity-restricted <tt>Queue</tt>
  18:  * implementations; in most implementations, insert operations cannot
  19:  * fail.
  20:  *
  21:  * <p>
  22:  * <table BORDER CELLPADDING=3 CELLSPACING=1>
  23:  *  <tr>
  24:  *    <td></td>
  25:  *    <td ALIGN=CENTER><em>Throws exception</em></td>
  26:  *    <td ALIGN=CENTER><em>Returns special value</em></td>
  27:  *  </tr>
  28:  *  <tr>
  29:  *    <td><b>Insert</b></td>
  30:  *    <td>{@link #add add(e)}</td>
  31:  *    <td>{@link #offer offer(e)}</td>
  32:  *  </tr>
  33:  *  <tr>
  34:  *    <td><b>Remove</b></td>
  35:  *    <td>{@link #remove remove()}</td>
  36:  *    <td>{@link #poll poll()}</td>
  37:  *  </tr>
  38:  *  <tr>
  39:  *    <td><b>Examine</b></td>
  40:  *    <td>{@link #element element()}</td>
  41:  *    <td>{@link #peek peek()}</td>
  42:  *  </tr>
  43:  * </table>
  44:  *
  45:  * <p>Queues typically, but do not necessarily, order elements in a
  46:  * FIFO (first-in-first-out) manner.  Among the exceptions are
  47:  * priority queues, which order elements according to a supplied
  48:  * comparator, or the elements' natural ordering, and LIFO queues (or
  49:  * stacks) which order the elements LIFO (last-in-first-out).
  50:  * Whatever the ordering used, the <em>head</em> of the queue is that
  51:  * element which would be removed by a call to {@link #remove() } or
  52:  * {@link #poll()}.  In a FIFO queue, all new elements are inserted at
  53:  * the <em> tail</em> of the queue. Other kinds of queues may use
  54:  * different placement rules.  Every <tt>Queue</tt> implementation
  55:  * must specify its ordering properties.
  56:  *
  57:  * <p>The {@link #offer offer} method inserts an element if possible,
  58:  * otherwise returning <tt>false</tt>.  This differs from the {@link
  59:  * java.util.Collection#add Collection.add} method, which can fail to
  60:  * add an element only by throwing an unchecked exception.  The
  61:  * <tt>offer</tt> method is designed for use when failure is a normal,
  62:  * rather than exceptional occurrence, for example, in fixed-capacity
  63:  * (or &quot;bounded&quot;) queues.
  64:  *
  65:  * <p>The {@link #remove()} and {@link #poll()} methods remove and
  66:  * return the head of the queue.
  67:  * Exactly which element is removed from the queue is a
  68:  * function of the queue's ordering policy, which differs from
  69:  * implementation to implementation. The <tt>remove()</tt> and
  70:  * <tt>poll()</tt> methods differ only in their behavior when the
  71:  * queue is empty: the <tt>remove()</tt> method throws an exception,
  72:  * while the <tt>poll()</tt> method returns <tt>null</tt>.
  73:  *
  74:  * <p>The {@link #element()} and {@link #peek()} methods return, but do
  75:  * not remove, the head of the queue.
  76:  *
  77:  * <p>The <tt>Queue</tt> interface does not define the <i>blocking queue
  78:  * methods</i>, which are common in concurrent programming.  These methods,
  79:  * which wait for elements to appear or for space to become available, are
  80:  * defined in the {@link java.util.concurrent.BlockingQueue} interface, which
  81:  * extends this interface.
  82:  *
  83:  * <p><tt>Queue</tt> implementations generally do not allow insertion
  84:  * of <tt>null</tt> elements, although some implementations, such as
  85:  * {@link LinkedList}, do not prohibit insertion of <tt>null</tt>.
  86:  * Even in the implementations that permit it, <tt>null</tt> should
  87:  * not be inserted into a <tt>Queue</tt>, as <tt>null</tt> is also
  88:  * used as a special return value by the <tt>poll</tt> method to
  89:  * indicate that the queue contains no elements.
  90:  *
  91:  * <p><tt>Queue</tt> implementations generally do not define
  92:  * element-based versions of methods <tt>equals</tt> and
  93:  * <tt>hashCode</tt> but instead inherit the identity based versions
  94:  * from class <tt>Object</tt>, because element-based equality is not
  95:  * always well-defined for queues with the same elements but different
  96:  * ordering properties.
  97:  *
  98:  *
  99:  * <p>This interface is a member of the
 100:  * <a href="{@docRoot}/../technotes/guides/collections/index.html">
 101:  * Java Collections Framework</a>.
 102:  *
 103:  * @see java.util.Collection
 104:  * @see LinkedList
 105:  * @see PriorityQueue
 106:  * @see java.util.concurrent.LinkedBlockingQueue
 107:  * @see java.util.concurrent.BlockingQueue
 108:  * @see java.util.concurrent.ArrayBlockingQueue
 109:  * @see java.util.concurrent.LinkedBlockingQueue
 110:  * @see java.util.concurrent.PriorityBlockingQueue
 111:  * @since 1.5
 112:  * @author Doug Lea
 113:  * @param <E> the type of elements held in this collection
 114:  */
 115: public interface Queue<E> extends Collection<E> {
 116:     /**
 117:      * Inserts the specified element into this queue if it is possible to do so
 118:      * immediately without violating capacity restrictions, returning
 119:      * <tt>true</tt> upon success and throwing an <tt>IllegalStateException</tt>
 120:      * if no space is currently available.
 121:      *
 122:      * @param e the element to add
 123:      * @return <tt>true</tt> (as specified by {@link Collection#add})
 124:      * @throws IllegalStateException if the element cannot be added at this
 125:      *         time due to capacity restrictions
 126:      * @throws ClassCastException if the class of the specified element
 127:      *         prevents it from being added to this queue
 128:      * @throws NullPointerException if the specified element is null and
 129:      *         this queue does not permit null elements
 130:      * @throws IllegalArgumentException if some property of this element
 131:      *         prevents it from being added to this queue
 132:      */
 133:     boolean add(E e);
 134: 
 135:     /**
 136:      * Inserts the specified element into this queue if it is possible to do
 137:      * so immediately without violating capacity restrictions.
 138:      * When using a capacity-restricted queue, this method is generally
 139:      * preferable to {@link #add}, which can fail to insert an element only
 140:      * by throwing an exception.
 141:      *
 142:      * @param e the element to add
 143:      * @return <tt>true</tt> if the element was added to this queue, else
 144:      *         <tt>false</tt>
 145:      * @throws ClassCastException if the class of the specified element
 146:      *         prevents it from being added to this queue
 147:      * @throws NullPointerException if the specified element is null and
 148:      *         this queue does not permit null elements
 149:      * @throws IllegalArgumentException if some property of this element
 150:      *         prevents it from being added to this queue
 151:      */
 152:     boolean offer(E e);
 153: 
 154:     /**
 155:      * Retrieves and removes the head of this queue.  This method differs
 156:      * from {@link #poll poll} only in that it throws an exception if this
 157:      * queue is empty.
 158:      *
 159:      * @return the head of this queue
 160:      * @throws NoSuchElementException if this queue is empty
 161:      */
 162:     E remove();
 163: 
 164:     /**
 165:      * Retrieves and removes the head of this queue,
 166:      * or returns <tt>null</tt> if this queue is empty.
 167:      *
 168:      * @return the head of this queue, or <tt>null</tt> if this queue is empty
 169:      */
 170:     E poll();
 171: 
 172:     /**
 173:      * Retrieves, but does not remove, the head of this queue.  This method
 174:      * differs from {@link #peek peek} only in that it throws an exception
 175:      * if this queue is empty.
 176:      *
 177:      * @return the head of this queue
 178:      * @throws NoSuchElementException if this queue is empty
 179:      */
 180:     E element();
 181: 
 182:     /**
 183:      * Retrieves, but does not remove, the head of this queue,
 184:      * or returns <tt>null</tt> if this queue is empty.
 185:      *
 186:      * @return the head of this queue, or <tt>null</tt> if this queue is empty
 187:      */
 188:     E peek();
 189: }
