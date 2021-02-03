"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return "X"
    
    num_x = sum(i.count("X") for i in board)
    num_o = sum(i.count("O") for i in board)

    if num_x <= num_o:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    n = len(board)

    for row in range(n):
        for col in range(n):
            if board[row][col] == EMPTY:
                actions.add((row,col))
    # print("HERE is your error ",actions,type(actions))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy_board = deepcopy(board)
    row = action[0]
    col = action[1]

    try:
        if copy_board[row][col] == EMPTY:
            copy_board[row][col] = player(board)
        else:
            raise ValueError('Move already taken')
    
    except IndexError:
        print('That move is out of bounds')

    return copy_board



def row_win(board):
    n = len(board)
    for row in range(n):
        unique_row = set(board[row])
        if ( (len(unique_row) == 1) and EMPTY not in unique_row):
            if ("X" in unique_row):
                return "X"
            else:
                return "O"

def col_win(board):
    n = len(board[0])
    # for col in range(n):
    #     if ( ( board[ 0 ][col] == board[1][col] == board[2][col]) ) and (board[ 0 ][ col ] != None ) ):
    #         return board[0][col]
    for row in range(n):
        check_win = []
        for col in range(n):
            check_win.append(board[col][row])
        if (check_win.count(check_win[0]) == len(check_win)) and check_win[0] != EMPTY:
            return check_win[0]

def diag_win(board):
    n = len(board)
    l_diag = [ board[rc][ rc ] for rc in range(n) ]
    r_diag = [ board[idx][ val ] for idx,val in enumerate(reversed(range(n))) ]

    if ( r_diag.count(r_diag[0]) == len(r_diag) and r_diag[0] != EMPTY):
        return r_diag[0]

    if ( l_diag.count(l_diag[0]) == len(l_diag) and l_diag[0] != EMPTY):
        return l_diag[0]



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (row_win(board)):
        return row_win(board)
    
    if (col_win(board)):
        return col_win(board)

    if (diag_win(board)):
        return diag_win(board)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if ( ( winner(board) ) or ( len(actions(board)) == 0) ):
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board)) == "X":
        return 1
    elif (winner(board)) == "O":
        return -1
    else: 
        return 0
    

def min_val(board):
    if terminal(board):
        return utility(board),None
    v = float('inf')
    move = None
    for action in actions(board):
        # v = min(v,max_val(result(board,action)))
        temp,_ = max_val(result(board,action))

        if temp < v:
            v = temp
            move = action 
    
    return v,move


def max_val(board):
    if terminal(board):
        return utility(board),None
    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v,min_val(result(board,action)))
        temp,_ = min_val(result(board,action))

        if temp > v:
            v = temp
            move = action     
    return v,move


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (terminal(board)):
        return None
    
    else:
        if player(board) == "X":
            _,action = max_val(board)
        else:
            _, action = min_val(board)
        return action
    
