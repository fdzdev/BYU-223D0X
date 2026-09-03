"""Separate-chaining hash map. TODO: shrink on delete."""

LOAD_FACTOR = 0.75


class HashMap:
    def __init__(self, cap=8):
        self._cap = cap
        self._n = 0
        self._buckets = [[] for _ in range(cap)]

    def __len__(self):
        return self._n

    def put(self, k, v):
        b = self._buckets[hash(k) % self._cap]
        for i, (ek, _) in enumerate(b):
            if ek == k:
                b[i] = (k, v)
                return
        b.append((k, v))
        self._n += 1
        if self._n / self._cap > LOAD_FACTOR:
            self._grow()

    def get(self, k, default=None):
        for ek, ev in self._buckets[hash(k) % self._cap]:
            if ek == k:
                return ev
        return default

    def _grow(self):
        items = [kv for b in self._buckets for kv in b]
        self._cap *= 2
        self._buckets = [[] for _ in range(self._cap)]
        self._n = 0
        for k, v in items:
            self.put(k, v)
