"""Unbalanced binary search tree."""


class BST:
    class _N:
        __slots__ = ("k", "l", "r")

        def __init__(self, k):
            self.k, self.l, self.r = k, None, None

    def __init__(self):
        self.root = None

    def insert(self, k):
        self.root = self._ins(self.root, k)

    def _ins(self, n, k):
        if n is None:
            return self._N(k)
        if k < n.k:
            n.l = self._ins(n.l, k)
        elif k > n.k:
            n.r = self._ins(n.r, k)
        return n

    def inorder(self):
        out = []
        stack, cur = [], self.root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.l
            cur = stack.pop()
            out.append(cur.k)
            cur = cur.r
        return out
