import random
import getch
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('2048')

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

def check_if_grid_is_full(grid):
    cells = []
    i = 0
    for x in grid:
        for y in x:
            cells.append(y)
    if i in cells:
        return False
    else:
        return True

array = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

place_random_number(array)
for row in array:
    print(row[0], row[1], row[2], row[3])
print('\n\nh = up\nj = down\nk = left\nl = right')

# Move Up Functionality
def get_columns_top_empty_cell(grid, row_index, cell_index):
    for x in reversed(range(row_index + 1)):
        # next, if its any row, and any cell above is full, return index before full cell
        if is_cell_free(grid, x - 1, cell_index) is False:
            return([x, cell_index])
        # next, if its any row, and above cell is (empty && row 1) -> return row 1 index
        elif is_cell_free(grid, x - 1, cell_index) and x == 1:
            return([x - 1, cell_index])


def move_cell_up(grid, row_index, cell_index):
    target_index = get_columns_top_empty_cell(grid, row_index, cell_index)
    cell_value = grid[row_index][cell_index]

    grid[int(target_index[0])][cell_index] = cell_value

    if row_index != target_index[0]:
        grid[row_index][cell_index] = 0
    return grid

def move_grid_up(grid):
    for x in range(4):
        row = grid[x]
        for y in range(4):
            current_cell = grid[x][y]
            if x != 0 and current_cell == grid[x - 1][y] and current_cell != 0:
                # merge cells 
                grid[x - 1][y] = current_cell + current_cell
                grid[x][y] = 0
            elif is_cell_free(grid, x, y) is False and x != 0 and is_cell_free(grid, x - 1, y) is True:
                grid = move_cell_up(grid, x, y)

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
                grid[x][y] = 0
            elif is_cell_free(grid, x, y) is False and x != 0:
                move_cell_up(grid, x, y)

    grid.reverse()

    place_random_number(array)
    for row in array:
        print(row[0], row[1], row[2], row[3])

# Move Left Functionality
def get_rows_leftmost_empty_cell(grid, row_index, cell_index):
    for x in reversed(range(cell_index + 1)):
        # if its any cell, and any cell to the left is full, return index before full cell
        if is_cell_free(grid, row_index, x - 1) is False:
            return([row_index, x])
        # next, if its any row, and left cell is (empty && col 1) -> return col 1 index
        elif is_cell_free(grid, row_index, x - 1) and x == 1:
            return([row_index, x - 1])

def move_cell_left(grid, row_index, cell_index):
    target_index = get_rows_leftmost_empty_cell(grid, row_index, cell_index)
    cell_value = grid[row_index][cell_index]

    grid[row_index][int(target_index[1])] = cell_value

    if cell_index != target_index[1]:
        grid[row_index][cell_index] = 0
    return grid

def move_grid_left(grid):
    for x in range(4):
        for y in range(4):
            current_cell = grid[x][y]
            if y == 0:
                continue
            if current_cell == grid[x][y - 1] and current_cell != 0:
                # merge cells
                grid[x][y - 1] = current_cell + current_cell
                grid[x][y] = 0
            elif is_cell_free(grid, x, y) is False and is_cell_free(grid, x, y - 1) is True:
                move_cell_left(grid, x, y)

    place_random_number(array)
    for row in array:
        print(row[0], row[1], row[2], row[3])

# Move Right Functionality
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

def move_cell_right(grid, row_index, cell_index):
    target_index = get_rows_rightmost_empty_cell(grid, row_index, cell_index)
    cell_value = grid[row_index][cell_index]

    grid[row_index][int(target_index[1])] = cell_value

    if cell_index != target_index[0]:
        grid[row_index][cell_index] = 0
    return grid

def move_grid_right(grid):
    for x in range(4):
        for y in reversed(range(4)):
            current_cell = grid[x][y]
            if y == 3:
                continue
            #print([x], [y])
            #print(current_cell, grid[x][y + 1])
            # merge cells
            if current_cell == grid[x][y + 1] and current_cell != 0:
                #print(f'merge {current_cell} + {grid[x][y + 1]}')
                grid[x][y + 1] = current_cell + current_cell
                grid[x][y] = 0
            # move any full cell to the right
            elif is_cell_free(grid, x, y) is False and is_cell_free(grid, x, y + 1) is True:
                move_cell_right(grid, x, y)

    place_random_number(array)
    for row in array:
        print(row[0], row[1], row[2], row[3])

# SCOREBOARD
def count_score(grid):
    cell_list = []
    for x in range(4):
        for y in range(4):
            cell_list.append(grid[x][y])
    
    current_score = max(cell_list)
    return(current_score)

# Google sheets
scores = SHEET.worksheet('scoreboard')
data = scores.get_all_values()
print('data:', data)

def update_high_score(data):
    print(f'Updating google sheet high score.. {data}')

    scoreboard = SHEET.worksheet('scoreboard')
    high_score = scoreboard.acell('A2').value
    if int(data) > int(high_score):
        scoreboard.update('A2', data)
        print('New high score: ', data)
    else:
        print('Play again to try beat the high score')


# User presses h, j, k, l to play
while True:
    char = getch.getch()

    if char == 'h':
        if check_if_grid_is_full(array) is False:
            print("\033c")
            move_grid_up(array)
            print('\n\nh = up\nj = down\nk = left\nl = right')
        elif check_if_grid_is_full(array) is True:
            print('GAME OVER')
            score = count_score(array)
            update_high_score(score)

    elif char == 'j':
        if check_if_grid_is_full(array) is False:
            print("\033c")
            move_grid_down(array)
            print('\n\nh = up\nj = down\nk = left\nl = right')
        if check_if_grid_is_full(array) is True:
            print('GAME OVER')
            score = count_score(array)
            update_high_score(score)

    elif char == 'k':
        if check_if_grid_is_full(array) is False:
            print("\033c")
            move_grid_left(array)
            print('\n\nh = up\nj = down\nk = left\nl = right')
        if check_if_grid_is_full(array) is True:
            print('GAME OVER')
            score = count_score(array)
            update_high_score(score)

    elif char == 'l':
        if check_if_grid_is_full(array) is False:
            print("\033c")
            move_grid_right(array)
            print('\n\nh = up\nj = down\nk = left\nl = right')
        if check_if_grid_is_full(array) is True:
            print('GAME OVER')
            score = count_score(array)
            update_high_score(score)

