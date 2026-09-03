"""Dynamic array with amortized O(1) append."""


class DynArray:
    def __init__(self, growth=2):
        self._n = 0
        self._cap = 4
        self._growth = growth
        self._buf = [None] * self._cap

    def __len__(self):
        return self._n

    def __getitem__(self, i):
        if not 0 <= i < self._n:
            raise IndexError(i)
        return self._buf[i]

    def append(self, value):
        if self._n == self._cap:
            self._resize(self._cap * self._growth)
        self._buf[self._n] = value
        self._n += 1

    def _resize(self, cap):
        new = [None] * cap
        for i in range(self._n):
            new[i] = self._buf[i]
        self._buf, self._cap = new, cap
