import random

array = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

for row in array:
    print(row[0], row[1], row[2], row[3])

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

place_random_number(array)
