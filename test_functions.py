import unittest
from unblock_me_functions import *

puzzle1 = [0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0,
           1, 1, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0]

puzzle1_1 = [0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0,
             0, 1, 1, 0, 0, 0,
             0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0]

puzzle2 = [0, 0, 0, 2, 0, 0,
           0, 0, 0, 2, 0, 0,
           1, 1, 0, 2, 0, 0,
           0, 0, 0, 0, 4, 0,
           0, 0, 3, 3, 4, 0,
           0, 0, 0, 0, 0, 0]

puzzle2_1 = [0, 0, 0, 2, 0, 0,
           0, 0, 0, 2, 0, 0,
           1, 1, 0, 2, 0, 0,
           0, 0, 0, 0, 4, 0,
           0, 3, 3, 0, 4, 0,
           0, 0, 0, 0, 0, 0]

puzzle2_2 = [0, 0, 0, 2, 0, 0,
             0, 0, 0, 2, 0, 0,
             1, 1, 0, 2, 4, 0,
             0, 0, 0, 0, 4, 0,
             0, 3, 3, 0, 0, 0,
             0, 0, 0, 0, 0, 0]

puzzle3 = [2,  2,  3,  3,  4,  5,
           6,  0,  0,  7,  4,  5,
           6,  1,  1,  7,  8,  9,
           10, 11, 11, 7,  8,  9,
           10, 12, 13, 0,  0,  0,
           0,  12, 13, 14, 14, 14]

puzzle3_1 = [2,  2,  3,  3,  4,  5,
           6,  0,  0,  7,  4,  5,
           6,  1,  1,  7,  8,  9,
           0, 11, 11, 7,  8,  9,
           10, 12, 13, 0,  0,  0,
           10,  12, 13, 14, 14, 14]


class TestCheckHorizontal(unittest.TestCase):
    """Test check_block_horizontal() function."""


    def test_vertical_block(self):
        """Can it return false for a vertical block?"""
        bool = check_block_horizontal(2, puzzle2)
        self.assertFalse(bool)


    def test_horizontal_block(self):
        """Can it return true for a horizontal block?"""
        bool = check_block_horizontal(11, puzzle3)
        self.assertTrue(bool)


class TestGetBlockPos(unittest.TestCase):
    """Test get_block_pos() function."""


    def test_vertical_block(self):
        """Can it return the position of block 2 in puzzle2?"""
        pos = get_block_pos(2, puzzle2)
        self.assertEqual(pos, [3, 9, 15])


    def test_horizontal_block(self):
        """Can it return the position of block 11 in puzzle3?"""
        pos = get_block_pos(11, puzzle3)
        self.assertEqual(pos, [19, 20])


class TestCheckLeftEdge(unittest.TestCase):
    """Test check_left_edge() function."""


    def test_touching_left_edge(self):
        """Can return true if a block is touching the left edge?"""
        bool = check_left_edge(1, puzzle2)
        self.assertTrue(bool)


    def test_not_touching_side(self):
        """Can return false if a block is not touching the side?"""
        bool = check_left_edge(3, puzzle2)
        self.assertFalse(bool)


class TestCheckTopEdge(unittest.TestCase):
    """Test check_top_edge() function."""


    def test_touching_top_edge(self):
        """Can return true if a block is touching the top edge?"""
        bool = check_top_edge(2, puzzle2)
        self.assertTrue(bool)


    def test_not_touching_vertical(self):
        """Can return false if a block is not touching the vertical?"""
        bool = check_top_edge(7, puzzle3)
        self.assertFalse(bool)


class TestCheckSideEdge(unittest.TestCase):
    """Test check_side_edge() function."""


    def test_touching_left_edge(self):
        """Can return true if a block is touching the left edge?"""
        bool = check_side_edge(1, puzzle2)
        self.assertTrue(bool)


    def test_touching_right_edge(self):
        """Can return true if a block is touching the right edge?"""
        bool = check_side_edge(14, puzzle3)
        self.assertTrue(bool)


    def test_not_touching_side(self):
        """Can return false if a block is not touching the side?"""
        bool = check_side_edge(3, puzzle2)
        self.assertFalse(bool)


class TestCheckVerticalEdge(unittest.TestCase):
    """Test check_vertical_edge() function."""


    def test_touching_top_edge(self):
        """Can return true if a block is touching the top edge?"""
        bool = check_vertical_edge(2, puzzle2)
        self.assertTrue(bool)


    def test_touching_bottom_edge(self):
        """Can return true if a block is touching the bottom edge?"""
        bool = check_vertical_edge(13, puzzle3)
        self.assertTrue(bool)


    def test_not_touching_vertical(self):
        """Can return false if a block is not touching the vertical?"""
        bool = check_vertical_edge(7, puzzle3)
        self.assertFalse(bool)



class TestCheckCanMoveBlock(unittest.TestCase):
    """Test check_can_move_block() function."""


    def test_trapped_horizontal_block(self):
        """Can return false if a horizontal block is between two others?"""
        bool = check_can_move_block(11, puzzle3)
        self.assertFalse(bool)


    def test_trapped_horizontal_block_with_edge(self):
        """Can return false if a horizontal block is between a block and an edge?"""
        bool = check_can_move_block(14, puzzle3)
        self.assertFalse(bool)


    def test_trapped_vertical_block(self):
        """Can return false if a vertical block is between two others?"""
        bool = check_can_move_block(6, puzzle3)
        self.assertFalse(bool)


    def test_trapped_vertical_block_with_edge(self):
        """Can return false if a vertical block is between a block and an edge?"""
        bool = check_can_move_block(12, puzzle3)
        self.assertFalse(bool)


    def test_both_direction_free_horizontal_block(self):
        """Can return true if a horizontal block is free to move both ways?"""
        bool = check_can_move_block(3, puzzle2)
        self.assertTrue(bool)


    def test_one_direction_free_horizontal_block(self):
        """Can return true if a horizontal block is free to move in one way?"""
        bool = check_can_move_block(1, puzzle2)
        self.assertTrue(bool)


    def test_both_direction_free_vertical_block(self):
        """Can return true if a vertical block is free to move both ways?"""
        bool = check_can_move_block(4, puzzle2)
        self.assertTrue(bool)


    def test_one_direction_free_vertical_block(self):
        """Can return true if a vertical block is free to move in one way?"""
        bool = check_can_move_block(2, puzzle2)
        self.assertTrue(bool)


class TestMoveBlock(unittest.TestCase):
    """Test move_block() function."""


    def test_step_right(self):
        """Can it step right?"""
        step = move_block(1, puzzle1)
        self.assertEqual(step, 'right')


    def test_step_left(self):
        """Can it step right?"""
        step = move_block(3, puzzle2)
        self.assertEqual(step, 'left')


    def test_step_up(self):
        """Can it step up?"""
        step = move_block(10, puzzle3_1)
        self.assertEqual(step, 'up')


    def test_step_down(self):
        """Can it step down?"""
        step = move_block(2, puzzle2)
        self.assertEqual(step, 'down')


class TestUpdateBoard(unittest.TestCase):
    """Test update_board() function."""


    def test_move_right(self):
        """Can it move a block right?"""
        board, list_board = update_board(1, puzzle1, [], 'right')
        self.assertEqual(board, puzzle1_1)

    def test_move_left(self):
        """Can it move a block left?"""
        board, list_board = update_board(3, puzzle2, [], 'left')
        self.assertEqual(board, puzzle2_1)

    def test_move_up(self):
        """Can it move a block up?"""
        board, list_board = update_board(4, puzzle2, [], 'up')
        self.assertEqual(board, puzzle2_2)

    def test_move_down(self):
        """Can it move a block down?"""
        board, list_board = update_board(10, puzzle3, [], 'down')
        self.assertEqual(board, puzzle3_1)


# class TestUnblockMe(unittest.TestCase):
#     """Test the main function unblock_me()."""
#     # the problem with testing this is that there are multiple paths to the solutions
#
#     def test_puzzle1(self):
#         """Can it solve puzzle1?."""
#         solution = unblock_me(puzzle1)
#         my_solution = ["Block 1; right 4"]
#         self.assertEqual(solution, my_solution)
#
#
#     def test_puzzle2(self):
#         """Can it solve puzzle2?."""
#         solution = unblock_me(puzzle2)
#         my_solution = ["Block 3; left 2", "Block 2; down 3", "Block 1; right 4"]
#         self.assertEqual(solution, my_solution)
#
#
#     def test_puzzle3(self):
#         """Can it solve puzzle3?."""
#         solution = unblock_me(puzzle3)
#         my_solution =  ["Block 7; down 1", "Block 8; down 1", "Block 9; down 1", "Block 4; down 1",
#           "Block 5; down 1", "Block 3; right 2", "Block 10; down 1", "Block 2; right 1",
#           "Block 6; up 1", "Block 1; left 1", "Block 11; left 1", "Block 13; up 3",
#           "Block 7; up 2", "Block 11; right 2", "Block 10; up 1", "Block 12; up 1",
#           "Block 14; left 3", "Block 8; down 1", "Block 9; down 1", "Block 11; right 2",
#           "Block 13; down 2", "Block 7; down 3", "Block 1; right 2", "Block 6; down 1",
#           "Block 2; left 1", "Block 3; left 2", "Block 4; up 1", "Block 5; up 1",
#           "Block 1; right 2"]
#         self.assertEqual(solution, my_solution)
#


unittest.main()
