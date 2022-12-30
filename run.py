array = [
    [0, 0, 0, 0],
    [2, 2, 2, 0],
    [0, 3, 3, 0],
    [4, 4, 0, 0],
]

for row in array:
    print(row[0], row[1], row[2], row[3])

def is_cell_free(grid, row, cell):
    return grid[row][cell] == 0

def get_free_cells(grid):
    free_cells = []
    row_count = 0
    
    for row in grid:
        row_count = row_count + 1
        index_count = 0
        for value_index in row:
            index_count = index_count + 1
            if value_index == 0:
                free_cells.append([row_count, index_count])
    
    return(free_cells)
