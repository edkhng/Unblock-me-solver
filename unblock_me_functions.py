

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
            if check_left_edge(block, board) and board[pos[1] + 1] != 0:
                return False
            elif not check_left_edge(block, board) and board[pos[0] - 1] != 0:
                return False
            else:
                return True
        else:
            if board[pos[0] - 1] != 0 and board[pos[1] + 1] != 0:
                return False
            else:
                return True

    else:
        if check_vertical_edge(block, board):
            if check_top_edge(block, board) and board[pos[1] + 6] != 0:
                return False
            elif not check_top_edge(block, board) and board[pos[0] - 6] != 0:
                return False
            else:
                return True
        else:
            if board[pos[0] - 6] != 0 and board[pos[1] + 6] != 0:
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


def check_vertical_edge(block, board):
    """Check if the block is touching the top or bottom of the grid
       Return True if it is False if not."""


def check_left_edge(block, board):
    """Check if the block is touching the left side of the grid
       Return True if it is False if not."""
       left_edge = [0, 6, 12, 18, 24, 30]
       try:
           



def check_top_edge(block, board):
    """Check if the block is touching the top of the grid
       Return True if it is False if not."""
