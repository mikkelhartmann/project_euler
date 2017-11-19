"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top 
to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is 
the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever 
method! ;o)
"""
class Node:
    def __init__(self, number, left_child, right_child):
        self.value = number
        self.children = [left_child, right_child]

    def getMaxChild(self):
        return max(self.children)

def turn_row_to_nodes(row, row_below):
    node_row = []
    for num_idx, number in enumerate(row):
        node = Node(number, row_below[num_idx], row_below[num_idx+1])
        node_row.append(node)
    return node_row

def reduce_row(node_row):
    new_row = []
    for node in node_row:
        new_row.append(node.value + node.getMaxChild())
    return new_row

def print_triangle(triangle):
    for row in triangle:
        print(row)

triangle_as_strings = [
"75",
"95 64",
"17 47 82",
"18 35 87 10",
"20 04 82 47 65",
"19 01 23 75 03 34",
"88 02 77 73 07 63 67",
"99 65 04 28 06 16 70 92",
"41 41 26 56 83 40 80 70 33",
"41 48 72 33 47 32 37 16 94 29",
"53 71 44 65 25 43 91 52 97 51 14",
"70 11 33 28 77 73 17 78 39 68 17 57",
"91 71 52 38 17 14 91 43 58 50 27 29 48",
"63 66 04 68 89 53 67 30 73 16 69 87 40 31",
"04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
]

triangle = [[int(number) for number in row.split()] for row in triangle_as_strings]

# Starting from the second to last row and moving up, do the folllowing:
# For each each node in the row, calculate the maximal outcome from that node.
# Replace the row above with the new row and start again.
row_idx = len(triangle)-2
while row_idx>=0:
    print_triangle(triangle)
    print("")
    
    row = triangle[row_idx]
    row_below = triangle[row_idx+1]

    node_row = turn_row_to_nodes(row, row_below)
    triangle[row_idx] = reduce_row(node_row)
    del triangle[row_idx+1]
    
    row_idx = row_idx - 1

print("The answer is:", triangle[row_idx+1][0])
