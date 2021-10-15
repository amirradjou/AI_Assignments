import time
import matplotlib.pyplot as plt
import numpy as np


def show_GameBoard(matrix):
    for row in matrix:
        print(row)


def number_of_collisions(matrix, row, column):
    collisions = 0
    for i in range(0, len(matrix)):
        if matrix[row][i] == 1:
            collisions += 1
        if matrix[i][column] == 1:
            collisions += 1

    for i, j in zip(range(row, -1, -1),
                    range(column, -1, -1)):
        if matrix[i][j] == 1:
            collisions += 1

    for i, j in zip(range(row, len(matrix), 1),
                    range(column, -1, -1)):
        if matrix[i][j] == 1:
            collisions += 1

    return collisions


def number_of_collisions_full(matrix, row, column):
    collisions = 0
    for i in range(0, len(matrix)):
        if matrix[row][i] == 1:
            collisions += 1
        if matrix[i][column] == 1:
            collisions += 1

    for k in range(0, len(matrix)):
        for l in range(0, len(matrix)):
            if (k + l == row + column) or (k - l == row - column):
                if matrix[k][l] == 1:
                    collisions += 1

    return collisions


def numberOfFreePositions(board, column):
    free_pos = 0
    for i in range(0, len(board)):
        if number_of_collisions_full(board, i, column) == 0:
            free_pos += 1
    return free_pos


def colMinFree(board, list_of_cols):
    min_free = len(board)
    min_free_col = None
    for item in list_of_cols:
        free_pos = numberOfFreePositions(board, item)
        if free_pos < min_free:
            min_free = free_pos
            min_free_col = item
    return min_free_col, min_free


def backtrackSolver(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if number_of_collisions(board, i, col) == 0:
            board[i][col] = 1
            if backtrackSolver(board, col + 1):
                return True
            board[i][col] = 0
    return False


def backtrackMRVSolver(board, col, col_list):
    for i in range(len(board)):
        if number_of_collisions_full(board, i, col) == 0:
            board[i][col] = 1
            if not col_list:
                return True
            new_list = col_list.copy()
            new_col, min_free_pos = colMinFree(board, new_list)
            if min_free_pos != 0:
                new_list.remove(new_col)
                if backtrackMRVSolver(board, new_col, new_list):
                    return True
            board[i][col] = 0
    return False


# Initializing The Board
n = int(input("Please Enter the size of Game board you wanna have: "))
game_board = [[0 for _ in range(n)] for _ in range(n)]

tic = time.time()
# Simple bactrack
if not backtrackSolver(game_board, 0):
    print("Could not find any possible solution!")
else:
    show_GameBoard(game_board)
toc = time.time()
print("Time for simple backtracking: " + str(toc - tic))

print('----------------------')

# Initializing The Board
game_board = [[0 for _ in range(n)] for _ in range(n)]

tic = time.time()
# MRV-backtrack
if not backtrackMRVSolver(game_board, 0, [i for i in range(1, len(game_board))]):
    print("Could not find any possible solution!")
else:
    show_GameBoard(game_board)
toc = time.time()
print("Time for MRV backtracking: " + str(toc - tic))
'''
x = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y1 = []
y2 = []
for num in x:
    game_board = [[0 for _ in range(num)] for _ in range(num)]
    tic = time.time()
    # Simple bactrack
    if not backtrackSolver(game_board, 0):
        print("Could not find any possible solution!")
    else:
        show_GameBoard(game_board)
    toc = time.time()
    y1.append(toc - tic)

    game_board = [[0 for _ in range(num)] for _ in range(num)]
    tic = time.time()
    # MRV-backtrack
    if not backtrackMRVSolver(game_board, 0, [i for i in range(1, len(game_board))]):
        print("Could not find any possible solution!")
    else:
        show_GameBoard(game_board)
    toc = time.time()
    y2.append(toc - tic)

plt.plot(x, y1, label="Simple Backtrack")
plt.plot(x, y2, label="MRV + Backtracking")
plt.xlabel('Size of the board')
plt.ylabel('Solving time')
plt.title('Comparison Between Backtrack and MRV+Backtrack in Different Boards.')
plt.legend()
plt.show()
'''