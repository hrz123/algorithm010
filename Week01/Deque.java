package com.example;

import java.util.Deque;
import java.util.LinkedList;

public class MyDeque {
  public static void main(String[] args) {
    Deque<String> deque = new LinkedList<String>();

    deque.offerLast("a");
    deque.offerLast("b");
    deque.offerLast("c");

    System.out.println(deque); // [a, b, c]


    String str = deque.peekLast();
    System.out.println(str); // c
    System.out.println(deque); // [a, b, c]

    // 像栈一样使用双端队列
    while (deque.size() > 0) {
      System.out.println(deque.pollLast()); // c -> b -> a
    }

    System.out.println(deque); // []
  }
}
