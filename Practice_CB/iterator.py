"""
[[1,2,3],
[4,5],
[6],
[],
[7,8,9]]
=>  [1,4,6,7,2,5,8,3,9]

"""
from typing import *
class MatrixIterator:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.cur_row = 0
        self.cur_col = 0

        self._get_to_the_next_available_row()

    def has_next(self):
       # print("move: ", self.cur_row, self.cur_col)
        return self._is_valid_cell(self.cur_row, self.cur_col)

    def next(self):
        ans = self.matrix[self.cur_row][self.cur_col]
        self.cur_col += 1
        if self.cur_col >= len(self.matrix[self.cur_row]):
            self.cur_col = 0
            self.cur_row += 1
            self._get_to_the_next_available_row()

        return ans

    def _get_to_the_next_available_row(self):
        while self.cur_row < len(self.matrix) and len(self.matrix[self.cur_row]) == 0:
            self.cur_row += 1
       # print(self.cur_row, " is ok")

    def _is_valid_cell(self, row: int, col: int) -> bool:
        return 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[row])

class ColumnBaseIterator:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.row = self.col = 0
        self._come_to_valid_row()

    def next(self):
        if not self.has_next():
            raise Exception("no more element")
        ans = self.matrix[self.row][self.col]
        self.row += 1
        if self.row >= len(self.matrix):
            self.row = 0
            self.col += 1

        self._come_to_valid_row()

        return ans
    def _come_to_valid_row(self):
        while self.row < len(self.matrix) and self.col >= len(self.matrix[self.row]):
            self.row += 1

    def has_next(self):
        return self._is_valid_cell(self.row, self.col)

    def _is_valid_cell(self, row, col):
        return 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[row])

def print_iterator(it):
    ans = []
    while it.has_next():
        ans.append(it.next())
    print(ans)

def test():
    test_cases = []
    test_cases.append([[1, 2, 3], [], [3, 4], [5, 6]])
    test_cases.append([[], [], [1, 2, 3], [], [4, 5], [], [6]])
    test_cases.append([[1,2,3],[4,5],[6],[],[7,8,9]])

    for matrix in test_cases:
        #sol = MatrixIterator(matrix)
        sol = ColumnBaseIterator(matrix)
        print_iterator(sol)
test()
