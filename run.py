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
