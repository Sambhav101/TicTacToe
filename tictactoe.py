"""
Tic Tac Toe Player
"""

import math

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
        return X

    X_count = 0
    O_count = 0
    
    for row in range(3):
        for column in range(3):
            if board[row][column] == X:
                X_count+=1
            elif board[row][column] == O:
                O_count+=1

    return O if X_count > O_count else X

    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_actions = set()

    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                all_actions.add((row, column))

    return all_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    

    board_copy = [row[:] for row in board]      # making a deep copy of original board

    if board_copy[action[0]][action[1]] == EMPTY:
        board_copy[action[0]][action[1]] = player(board)  # put either X or O to the action postion
    else:
        raise Exception("Invalid Move")

    return board_copy




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # 3 in a row win
    for rows in board:
        if len(set(rows)) == 1 and (rows[0] is not None):
            return rows[0]

    # 3 in a column win
    for x, y, z in zip(*board):
        if x == y and y == z and (x is not None):
            return x


    # 3 in a diagonal win
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and (board[0][0] is not None):
        return board[1][1]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and (board[1][1] is not None):
        return board[1][1]

    return None

    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    board_list = [section for row in board for section in row]

    if board_list.count(EMPTY) == 0 or (winner(board) is not None):
        return True
        
    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) is None:
            return 0
        elif winner(board) == O:
            return -1
        else:
            return 1


def max_value(board):
    """
    returns the maximum value of a given board
    """
    if terminal(board):
        return utility(board)

    
    value = None

    for action in actions(board):
        point = min_value(result(board, action))
        if value is None or point > value:
            value = point

    return value





def min_value(board):
    """
    returns the minimum value of a given board

    """
    if terminal(board):
        return utility(board)

    
    value = None

    for action in actions(board):
        point = max_value(result(board, action))
        if value is None or point < value:
            value = point

    return value

    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    data = {}

    if player(board) == X:
        for action in actions(board):
            data[action] = min_value(result(board, action))
        return max(data, key=data.get)
    else:
        for action in actions(board):
            data[action] = max_value(result(board, action))
        return min(data, key=data.get)








