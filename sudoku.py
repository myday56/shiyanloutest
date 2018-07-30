import random
import itertools
from copy import deepcopy

def make_board(m = 3):
    numbers = list(range(1, m**2 +1))
    board = None
    while board is None:
        board = attempt_board(m,numbers)
    return board

def attempt_board(m,numbers):
    n = m ** 2
    board = [[None for _ in range(n)] for _ in range(n)]

    for i,j in itertools.product(range(n), repeat=2):
        i0, j0 = i - i%m,j - j%m

        random.shuffle(numbers)
        for x in numbers:
            if(x not in board[i]
                and all(row[j] != for row in board)
                and all(x not in row[j0:j0+m]
                    for row in board[i0:i])):
                    board[i][j] = x
                    break
            else:
                return None
    return board


