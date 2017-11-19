"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum 
total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K 
text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this 
problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take 
over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
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

f = open('problem_67_data.txt')
triangle = []
for line in f.readlines():
    triangle.append( [int(num) for num in line.split()] )

row_idx = len(triangle)-2
while row_idx>-1:
    row = triangle[row_idx]
    row_below = triangle[row_idx+1]
    node_row = turn_row_to_nodes(row, row_below)
    row = reduce_row(node_row)
    triangle[row_idx] = row
    row_idx = row_idx - 1
print(row[0])