""" A builder is looking to build a row of N houses that can be of K different
colors. He has a goal of minimizing cost while ensuring that no two neighboring
houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to
build the nth house with kth color, return the minimum cost which achieves this
goal.


n = 3
k = 3
matrix = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]

1 2 3
4 5 6
7 8 9

=>

1 2 3
12 12 13


=>

13 14 15

=>

13
"""


def min_cost(matrix, curr_row, skip_index):
    # Find lowest cost in row except for skip_index

    # If last row, just return min
    if curr_row == len(matrix)-1:
        # Get all costs except for skip_index
        costs = [x for i, x in enumerate(matrix[curr_row]) if i != skip_index]
        return min(costs)
    else:
        costs = []
        for i, x in enumerate(matrix[curr_row]):
            if i != skip_index:
                costs.append(x+min_cost(matrix, curr_row+1, i))
        return min(costs)


def calc_cost(matrix):
    # Iterate through each col
    return min_cost(matrix, 0, -1)


assert calc_cost([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13
