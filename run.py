import random
import getch

print("\033c")

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
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

place_random_number(array)

for row in array:
    print(row[0], row[1], row[2], row[3])
print('---------')

# Move Up Functionality
def get_columns_top_empty_cell(grid, row_index, cell_index):
    for x in reversed(range(row_index + 1)):
        if row_index == 0 and is_cell_free(grid, x, cell_index):
            return([row_index, cell_index])
            break
        # next, if its any row, and any cell above is full, return index before full cell
        elif is_cell_free(grid, x - 1, cell_index) is False:
            return([x, cell_index])
            break
        # next, if its any row, and above cell is (empty && row 1) -> return row 1 index
        elif is_cell_free(grid, x - 1, cell_index) and x == 1:
            return([x - 1, cell_index])
            break


def move_cell_up(grid, row_index, cell_index):
    target_index = get_columns_top_empty_cell(grid, row_index, cell_index)
    cell_value = grid[row_index][cell_index]

    array[int(target_index[0])][cell_index] = cell_value

    if row_index != target_index[0]:
        array[row_index][cell_index] = 0

def move_grid_up(grid):
    for x in range(4):
        row = grid[x]
        for y in range(4):
            current_cell = grid[x][y]
            if x != 0 and current_cell == grid[x - 1][y]:
                # merge cells
                grid[x - 1][y] = current_cell + current_cell
                current_cell = 0
            elif is_cell_free(grid, x, y) is False and x != 0:
                move_cell_up(grid, x, y)

    place_random_number(array)
    for row in array:
        print(row[0], row[1], row[2], row[3])

# Move Down Functionality
def move_grid_down(grid):
    grid.reverse()

    for x in range(4):
        row = grid[x]
        for y in range(4):
            current_cell = grid[x][y]
            if x != 0 and current_cell == grid[x - 1][y]:
                # merge cells
                grid[x - 1][y] = current_cell + current_cell
                current_cell = 0
            elif is_cell_free(grid, x, y) is False and x != 0:
                move_cell_up(grid, x, y)

    grid.reverse()

    place_random_number(array)
    for row in array:
        print(row[0], row[1], row[2], row[3])

# Move Left Functionality
def get_rows_leftmost_empty_cell(grid, row_index, cell_index):
    for x in reversed(range(cell_index + 1)):
        if cell_index == 0 and is_cell_free(grid, row_index, cell_index):
            return([row_index, cell_index])
            break
        # next, if its any cell, and any cell to the left is full, return index before full cell
        elif is_cell_free(grid, row_index, x - 1) is False:
            return([row_index, x])
            break
        # next, if its any row, and left cell is (empty && col 1) -> return col 1 index
        elif is_cell_free(grid, row_index, x - 1) and x == 1:
            return([row_index, x - 1])
            break

def move_cell_left(grid, row_index, cell_index):
    target_index = get_rows_leftmost_empty_cell(grid, row_index, cell_index)
    cell_value = grid[row_index][cell_index]

    array[row_index][int(target_index[1])] = cell_value

    if cell_index != target_index[0]:
        array[row_index][cell_index] = 0

def move_grid_left(grid):
    for x in range(4):
        row = grid[x]
        for y in range(4):
            current_cell = grid[x][y]
            if y != 0 and current_cell == grid[x][y - 1]:
                # merge cells
                grid[x][y - 1] = current_cell + current_cell
                current_cell = 0
            elif is_cell_free(grid, x, y) is False and y != 0:
                move_cell_left(grid, x, y)

    place_random_number(array)
    for row in array:
        print(row[0], row[1], row[2], row[3])


while True:
    char = getch.getch()

    if char == 'h':
        print("\033c")
        print('Move Up')
        move_grid_up(array)
    elif char == 'j':
        print("\033c")
        print('Move Down')
        move_grid_down(array)
    elif char == 'k':
        print("\033c")
        print('Move Left')
        move_grid_left(array)
    elif char == 'l':
        print("\033c")
        print('Move Right')
