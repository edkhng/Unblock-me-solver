"""
==================
Unblock me solver
==================

Description of the game:

Unblock Me is a mobile game by Kira Games that contains numerous puzzles of
different difficulty. The puzzle involves blocks that are 2 units or 3 units
long, oriented vertically or horizontally placed in a 6x6 grid. The blocks can
only move parallel to their orientation. There is a single red block in the
puzzle oriented horizontally, and an opening in the right edge of the grid with
a width of 1 unit placed 2 units from the top of the grid and 3 from the
bottom. The puzzle is complete when the red block can be moved into the
opening without any other blocks in the way.


Outline:
- '0' represents an empty space
- blocks are represented with numbers
- the red block is '1'
- hard to visualize, and initialize but hopefully simple to code without
  needing to make different classes to represent the blocks

Example 1 (Trivial Case)

Starting State:            End State:
0  0  0  0  0  0           0  0  0  0  0  0
0  0  0  0  0  0           0  0  0  0  0  0
1  1  0  0  0  0  ------>  0  0  0  0  1  1
0  0  0  0  0  0           0  0  0  0  0  0
0  0  0  0  0  0           0  0  0  0  0  0
0  0  0  0  0  0           0  0  0  0  0  0

Steps: (Not sure how to save the steps yet, formate might change)
[(Block 1, right 4)]



Example 2

Starting State:            End State: (There are several end states)
0  0  0  2  0  0           0  0  0  0  0  0      0  0  0  0  0  0      0  0  0  0  0  0
0  0  0  2  0  0           0  0  0  0  0  0      0  0  0  0  0  0      0  0  0  0  0  0
1  1  0  2  0  0  ------>  0  0  0  0  1  1  or  0  0  0  0  1  1  or  0  0  0  0  1  1
0  0  0  0  0  0           0  0  0  2  0  0      0  0  0  2  0  0      0  0  0  2  0  0
0  0  3  3  0  0           0  3  3  2  0  0      3  3  0  2  0  0      0  0  0  2  3  3
0  0  0  0  0  0           0  0  0  2  0  0      0  0  0  2  0  0      0  0  0  2  0  0

Steps: (Several end states and several different steps to get to each end state)
This is just an example set of steps to get to the first end state
[(Block 3, left 2), (Block 2, down 3), (Block 1, right 4)]


Example 3 (From advanced puzzle 33 in the game)

Starting State:            End State: (There are several end states)
2   2   3   3   4   5           2   2   3   3  4   5
6   0   0   7   4   5           6   0   0   0  4   5
6   1   1   7   8   9  ------>  6   0   0   0  1   1
10  11  11  7   8   9           10  12  13  7  11  11
10  12  13  0   0   0           10  12  13  7  8   9
0   12  13  14  14  14          14  14  14  7  8   9

Steps: (The ones I used in solving this)
 [(Block 7, down 1), (Block 8, down 1), (Block 9, down 1), (Block 4, down 1),
  (Block 5, down 1), (Block 3, right 2), (Block 10, down 1), (Block 2, right 1),
  (Block 6, up 1), (Block 1, left 1), (Block 11, left 1), (Block 13, up 3),
  (Block 7, up 2), (Block 11, right 2), (Block 10, up 1), (Block 12, up 1),
  (Block 14, left 3), (Block 8, down 1), (Block 9, down 1), (Block 11, right 2),
  (Block 13, down 2), (Block 7, down 3), (Block 1, right 2), (Block 6, down 1),
  (Block 2, left 1), (Block 3, left 2), (Block 4, up 1), (Block 5, up 1),
  (Block 1, right 2)]

"""
import unblock_me_functions as uf
# How to input the puzzle, as a 1D list/array? I'm just using numbers to represent all the blocks

# puzzle is list of numbers 36 elements long
# horizontal blocks are numbers next to each other, vertical are seperated by 6 apart

grid_pos = [ 0,  1,  2,  3,  4,  5,
             6,  7,  8,  9, 10, 11,
            12, 13, 14, 15, 16, 17,
            18, 19, 20, 21, 22, 23,
            24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35]

# block is Int
# board is listofInt
# step is String
# solution is listofString

def unblock_me(puzzle):
    """Main function that takes the puzzle and returns a list of moves
       that solves the puzzle. """

    # board is the current state of the puzzle
    board = puzzle
    solution = []
    list_board = []  # keep track of all the iterations of board
    list_board.append(board)
    N_blocks = max(puzzle)

    flag = False  # change to true when complete
    while flag == False:
        # iterate through every block
        # don't know how to backtrack
        for i in range(1, N_blocks+1):
            if uf.check_can_move_block(i, board):
                step = uf.move_block(i, board)
                uf.update_board(i, board, list_board, step)
                uf.update_solution(i, step, solution)

                # solved when block 1 is at the left edge
                if uf.get_block_pos(1, board) == 16, 17:
                    flag = True

    return solution
