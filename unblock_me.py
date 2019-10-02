"""
Unblock me solver
"""

'''
- '0' represents an empty space
- blocks are represented with numbers
- the red block is '1'
- hard to visualize and initialize but hopefully simple to code without
  needing to make different classes to represent the blocks

Example 1

Starting State:            End State:
0  0  0  0  0  0           0  0  0  0  0  0
0  0  0  0  0  0           0  0  0  0  0  0
1  1  0  0  0  0  ------>  0  0  0  0  1  1
0  0  0  0  0  0           0  0  0  0  0  0
0  0  0  0  0  0           0  0  0  0  0  0
0  0  0  0  0  0           0  0  0  0  0  0

Steps: (Not sure how to save the steps yet, formate might change)
(There are several steps to get to the same end state)
e.g., [(Block 1, right 4)] or [(Block 1, right 2), (Block 1, right 2)] as an example


Example 2

Starting State:            End State: (There are several end states)
0  0  0  2  0  0           0  0  0  0  0  0      0  0  0  0  0  0      0  0  0  0  0  0
0  0  0  2  0  0           0  0  0  0  0  0      0  0  0  0  0  0      0  0  0  0  0  0
1  1  0  2  0  0  ------>  0  0  0  0  1  1  or  0  0  0  0  1  1  or  0  0  0  0  1  1
0  0  0  0  0  0           0  0  0  2  0  0      0  0  0  2  0  0      0  0  0  2  0  0
0  0  3  3  0  0           0  3  3  2  0  0      3  3  0  2  0  0      0  0  0  2  3  3
0  0  0  0  0  0           0  0  0  2  0  0      0  0  0  2  0  0      0  0  0  2  0  0

Steps: (Several end states and several different steps to get to each end state)
This is just an example
[(Block 3, left 2), (Block 2, down 3), (Block 1, right 4)]


Example 3 (Puzzle 33 Advanced)

Starting State:            End State: (There are several end states)
2   2   3   3   4   5           2   2   3   3  4   5
6   0   0   7   4   5           6   0   0   0  4   5
6   1   1   7   8   9  ------>  6   0   0   0  1   1
10  11  11  7   8   9           10  12  13  7  11  11
10  12  13  0   0   0           10  12  13  7  8   9
0   12  13  14  14  14          14  14  14  7  8   9

Steps: (The ones I used in solving this)
 [(Block 7, down 1), (Block 8, down 1), (Block 9, down 1), (Block 4, down 1), 
 (Block 5, down 1),]
'''
