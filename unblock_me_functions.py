def get_block_pos(block, board):
    """Return the position of the block on the board."""
    pos = []
    for i in range(36):
        if board[i] == block:
            pos.append(i)
    return pos


def check_can_move_block(block, board):
    """Check if the block can be moved.
       Return true if it can and false if not."""
    pos = get_block_pos(block, board)
    # must be a neater way to code this
    if check_block_horizontal(block, board):
        if check_side_edge(block, board):
            if check_left_edge(block, board) and board[pos[-1] + 1] != 0:
                return False
            elif not check_left_edge(block, board) and board[pos[0] - 1] != 0:
                return False
            else:
                return True
        else:
            if board[pos[0] - 1] != 0 and board[pos[-1] + 1] != 0:
                return False
            else:
                return True

    else:
        if check_vertical_edge(block, board):
            if check_top_edge(block, board) and board[pos[-1] + 6] != 0:
                return False
            elif not check_top_edge(block, board) and board[pos[0] - 6] != 0:
                return False
            else:
                return True
        else:
            if board[pos[0] - 6] != 0 and board[pos[-1] + 6] != 0:
                return False
            else:
                return True


def check_block_horizontal(block, board):
    """Check if the block is vertical or horizontal.
       Return True if horizontal and False if vertical."""
    pos = get_block_pos(block, board)
    if pos[1] - pos[0] == 1:
        return True
    else:
        return False


def check_side_edge(block, board):
    """Check if the block is touching the side of the grid
       Return True if it is False if not."""
    pos = get_block_pos(block, board)
    if pos[0] % 6 == 0 or pos[-1] % 6 == 5:
        return True
    else:
        return False


def check_vertical_edge(block, board):
    """Check if the block is touching the top or bottom of the grid
       Return True if it is False if not."""
    pos = get_block_pos(block, board)
    if pos[0] - 5 <= 0 or pos[-1] + 5 >= 35:
        return True
    else:
        return False


def check_left_edge(block, board):
    """Check if the block is touching the left side of the grid
       Return True if it is False if not."""
    pos = get_block_pos(block, board)
    if pos[0] % 6 == 0:
        return True
    else:
        return False


def check_top_edge(block, board):
    """Check if the block is touching the top of the grid
       Return True if it is False if not."""
    pos = get_block_pos(block, board)
    if pos[0] - 5 <= 0:
        return True
    else:
        return False


def move_block(block, board):
    """Return the correct movement for the block, if more
       than one option then choose randomly."""
    pos = get_block_pos(block, board)
    # must be a neater way to code this
    if check_block_horizontal(block, board):
        if check_side_edge(block, board):
            if check_left_edge(block, board):
                return 'right'
            else:
                return 'left'

        else:
            if board[pos[0] - 1] == 0 and board[pos[-1] + 1] == 0:
                from numpy.random import rand
                if rand() < 0.5:
                    step = 'right'
                else:
                    step ='left'
                return step
            elif board[pos[0] - 1] == 0:
                return 'left'
            else:
                return 'right'

    else:
        if check_vertical_edge(block, board):
            if check_top_edge(block, board):
                return 'down'
            else:
                return 'up'
        else:
            if board[pos[0] - 6] == 0 and board[pos[-1] + 6] == 0:
                from numpy.random import rand
                if rand() < 0.5:
                    step = 'up'
                else:
                    step ='down'
                return step
            elif board[pos[0] - 6] == 0:
                return 'up'
            else:
                return 'down'


def update_board(block, board, step):
    """Implement the step and update the board accordingly."""
    pos = get_block_pos(block, board)
    new_board = board.copy()
    if step == 'right':
        new_board[pos[0]] = 0
        new_board[pos[-1] + 1] = block
    elif step == 'left':
        new_board[pos[-1]] = 0
        new_board[pos[0] - 1] = block
    elif step == 'up':
        new_board[pos[-1]] = 0
        new_board[pos[0] - 6] = block
    elif step == 'down':
        new_board[pos[0]] = 0
        new_board[pos[-1] + 6] = block

    return new_board


def visualize_solution(list_board):
    """Print the board to show the progression of steps."""
    for i in range(len(list_board)):
        visualize_board(list_board[i])


def visualize_board(board):
    """Print the list of numbers representing the board
       in a 6x6 grid for visualization."""
    print("[{:2d} {:2d} {:2d} {:2d} {:2d} {:2d}\n"
          " {:2d} {:2d} {:2d} {:2d} {:2d} {:2d}\n"
          " {:2d} {:2d} {:2d} {:2d} {:2d} {:2d}\n"
          " {:2d} {:2d} {:2d} {:2d} {:2d} {:2d}\n"
          " {:2d} {:2d} {:2d} {:2d} {:2d} {:2d}\n"
          " {:2d} {:2d} {:2d} {:2d} {:2d} {:2d}]\n".format(*board))
