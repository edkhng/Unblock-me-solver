import unittest


puzzle1 = [0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0,
           1, 1, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0]

puzzle2 = [0, 0, 0, 2, 0, 0,
           0, 0, 0, 2, 0, 0,
           1, 1, 0, 2, 0, 0,
           0, 0, 0, 0, 0, 0,
           0, 0, 3, 3, 0, 0,
           0, 0, 0, 0, 0, 0]

puzzle3 = [2,  2,  3,  3,  4,  5,
           6,  0,  0,  7,  4,  5,
           6,  1,  1,  7,  8,  9,
           10, 11, 11, 7,  8,  9,
           10, 12, 13, 0,  0,  0,
           0,  12, 13, 14, 14, 14]

class TestGetBlockPos(unittest.TestCase):
    """Test get_block_pos() function."""


    def test_vertical_block(self):
        """Can it return the position of block 2 in puzzle2?"""
        pos == get_block_pos(2, puzzle2)
        self.assertEqual(pos, [3, 9, 15])


    def test_horizontal_block(self):
        """Can it return the position of block 11 in puzzle3?"""
        pos == get_block_pos(11, puzzle3)
        self.assertEqual(pos, [19, 20])


class TestUnblockMe(unittest.TestCase):
    """Test the main function unblock_me()."""
    # the problem with testing this is that there are multiple paths to the solutions

    def test_puzzle1(self):
        """Can it solve puzzle1?."""
        solution = unblock_me(puzzle1)
        my_solution = ["Block 1; right 4"]
        self.assertEqual(solution, my_solution)


    def test_puzzle2(self):
        """Can it solve puzzle2?."""
        solution = unblock_me(puzzle2)
        my_solution = ["Block 3; left 2", "Block 2; down 3", "Block 1; right 4"]
        self.assertEqual(solution, my_solution)


    def test_puzzle3(self):
        """Can it solve puzzle3?."""
        solution = unblock_me(puzzle3)
        my_solution =  ["Block 7; down 1", "Block 8; down 1", "Block 9; down 1", "Block 4; down 1",
          "Block 5; down 1", "Block 3; right 2", "Block 10; down 1", "Block 2; right 1",
          "Block 6; up 1", "Block 1; left 1", "Block 11; left 1", "Block 13; up 3",
          "Block 7; up 2", "Block 11; right 2", "Block 10; up 1", "Block 12; up 1",
          "Block 14; left 3", "Block 8; down 1", "Block 9; down 1", "Block 11; right 2",
          "Block 13; down 2", "Block 7; down 3", "Block 1; right 2", "Block 6; down 1",
          "Block 2; left 1", "Block 3; left 2", "Block 4; up 1", "Block 5; up 1",
          "Block 1; right 2"]
        self.assertEqual(solution, my_solution)
