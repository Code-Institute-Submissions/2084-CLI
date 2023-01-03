import unittest

# TEST is_cell_free
def is_cell_free(grid, row, cell):
    return grid[row][cell] == 0

class TestIsCellFree(unittest.TestCase):
    def test_is_cell_free(self):
        array = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
        self.assertEqual(is_cell_free(array, 1, 1), False)

# TEST get_columns_top_empty_cell
def get_columns_top_empty_cell(grid, row_index, cell_index):
    for x in reversed(range(row_index + 1)):
        # if its any row, and any cell above is full, return index before full cell
        if is_cell_free(grid, x - 1, cell_index) is False:
            return([x, cell_index])
        # if its any row, and above cell is (empty && row 1) -> return row 1 index
        elif is_cell_free(grid, x - 1, cell_index) and x == 1:
            return([x - 1, cell_index])

class TestGetTopEmptyCell(unittest.TestCase):
    def test_top_empty_cell_of_full_row(self):
        array = [
            [0, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
        self.assertEqual(get_columns_top_empty_cell(array, 1, 0), [0, 0])

# TEST get_columns_rightmost_empty_cell
def get_rows_rightmost_empty_cell(grid, row_index, cell_index):
    for x in reversed(range(cell_index + 1)):
        # check column 3 with one empty ceel to right
        if x == 2 and grid[row_index][x + 1] == 0:
            return[row_index,x + 1]
        # check column 2 with two empty cells to right
        elif x == 1 and grid[row_index][x + 1] == 0 and grid[row_index][x + 2] == 0:
            return[row_index,x + 2]
        # check column 1 with three empty cells to right
        elif x == 0 and grid[row_index][x + 1] == 0 and grid[row_index][x + 2] == 0  and grid[row_index][x + 3] == 0:
            return[row_index,x + 3]
        # check column 2 with one empty cells to right
        elif x == 1 and  grid[row_index][x + 1] == 0 and grid[row_index][x + 2] != 0:
            return[row_index,x + 1]
        # check column 1 with two empty cells to right
        elif x == 0 and  grid[row_index][x + 1] == 0 and grid[row_index][x + 2] == 0  and grid[row_index][x + 3] != 0:
            return[row_index,x + 2]
        # check column 1 with one empty cell to right
        elif x == 0 and  grid[row_index][x + 1] == 0 and grid[row_index][x + 2] != 0  and grid[row_index][x + 3] != 0:
            return[row_index, x + 1]

class TestGetRightmostEmptyCell(unittest.TestCase):
    def test_right_empty_cell_of_full_row(self):
        array = [
            [0, 2, 2, 0],
            [2, 2, 0, 0],
            [4, 0, 0, 0],
            [4, 4, 0, 2],
        ]
        self.assertEqual(get_rows_rightmost_empty_cell(array, 0, 2), [0, 3])
        self.assertEqual(get_rows_rightmost_empty_cell(array, 1, 1), [1, 3])
        self.assertEqual(get_rows_rightmost_empty_cell(array, 2, 0), [2, 3])
        self.assertEqual(get_rows_rightmost_empty_cell(array, 3, 1), [3, 2])