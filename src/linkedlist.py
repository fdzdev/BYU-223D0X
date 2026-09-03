"""Singly linked list."""


class Node:
    __slots__ = ("value", "next")

    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None
        self._n = 0

    def __len__(self):
        return self._n

    def push_front(self, value):
        self.head = Node(value, self.head)
        self._n += 1

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev
