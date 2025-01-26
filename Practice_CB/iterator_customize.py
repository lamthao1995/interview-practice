from typing import *

class IteratorInterface:
    def next(self) -> int:
        pass
    def has_next(self) -> bool:
        pass

class InvalidInputException(Exception):
    pass

class ListIterator(IteratorInterface):
    def __init__(self, list_int:List[int]):
        self.idx = 0
        self.list_integer = list_int

    def has_next(self):
        return 0 <= self.idx < len(self.list_integer)

    def next(self):
        if self.has_next() is False:
            raise StopIteration("no more data for this ListIterator")
        ans = self.list_integer[self.idx]
        self.idx += 1
        return ans

class TopDownIterator(IteratorInterface):
    def __init__(self, matrix: List[List[int]]):
        self.list_iter = [ListIterator(row) for row in matrix if row]
        self.total = self.idx = 0
        for row in matrix:
            self.total += len(row)

    def has_next(self):
        return self.total > 0

    def next(self):
        if self.has_next() is False:
            raise StopIteration("no more data for this TopDownIterator")
        ans = self.list_iter[self.idx].next()
        self.total -= 1
        self.idx = (1 + self.idx) % len(self.list_iter)
        if self.total > 0:
            self._come_to_valid_row()

        return ans

    def _come_to_valid_row(self):
        while self.list_iter[self.idx].has_next() is False:
            self.idx = (self.idx + 1) % len(self.list_iter)

class ZigzagIterator(IteratorInterface):
    def __init__(self, matrix: List[List[int]]):
        self.list_iter = [ListIterator(row) for row in matrix if row]
        self.total = self.idx = 0
        for row in matrix:
            self.total += len(row)
        self.is_down = True

    def has_next(self):
        return self.total > 0

    def next(self):
        if self.has_next() is False:
            raise StopIteration("no more data for this ZigzagIterator")
        ans = self.list_iter[self.idx].next()
        self.total -= 1
        self._increase_idx()
        if self.total <= 0:
            return ans
        if self.idx < 0:
            self.idx = 0
            self.is_down = True
        elif self.idx >= len(self.list_iter):
            self.is_down = False
            self.idx = len(self.list_iter) - 1
        self._come_to_valid_row()
        return ans

    def _increase_idx(self):
        self.idx += 1 if self.is_down else -1

    def _come_to_valid_row(self):
        while self.list_iter[self.idx].has_next() is False:
            self._increase_idx()

def print_iterator(it: IteratorInterface):
    ans = []
    while it.has_next():
        ans.append(it.next())
    print(ans)

def test():
    test_cases = []
    test_cases.append([
        [1, 2, 3],
        [],
        [4, 5, 6],
        [7],
        [8, 9, 10]])
    for matrix in test_cases:
        sol = ZigzagIterator(matrix)
        print_iterator(sol)
test()