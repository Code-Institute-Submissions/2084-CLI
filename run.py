import random

def is_cell_free(grid, row, cell):
    return grid[row][cell] == 0

def get_free_cells(grid):
    free_cells = []
    row_count = -1
    
    for row in grid:
        row_count = row_count + 1
        index_count = -1
        for value_index in row:
            index_count = index_count + 1
            if value_index == 0:
                free_cells.append([row_count, index_count])
    return(free_cells)

def get_random_free_cell(grid):
    free_cells = get_free_cells(grid)
    random_free_cell = random.choice(free_cells)

    return(random_free_cell)

def place_random_number(grid):
    random_cell = get_random_free_cell(grid)

    array[random_cell[0]][random_cell[1]] = 2

array = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 0],
]

# place_random_number(array)

for row in array:
    print(row[0], row[1], row[2], row[3])
print('---------')

#Move Up Functionality
def get_columns_top_empty_cell(grid, row_index, cell_index):
    for x in reversed(range(row_index + 1)):
        if row_index == 0 and is_cell_free(grid, x, cell_index):
            return('1', [row_index, cell_index])
            break
        # next, if its any row, and any cell above is full, return index before full cell
        elif is_cell_free(grid, x - 1, cell_index) is False:
            return([x, cell_index])
            break
        # next, if its any row, and above cell is (empty && row 1) -> return row 1 index
        elif is_cell_free(grid, x, cell_index) and x == 1:
            return([x - 1, cell_index])
            break


def move_cell_up(grid, row_index, cell_index):
    target_index = get_columns_top_empty_cell(grid, row_index, cell_index)
    cell_value = grid[row_index][cell_index]

    array[int(target_index[0])][cell_index] = cell_value

    if row_index != target_index[0]:
        array[row_index][cell_index] = 0
