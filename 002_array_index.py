"""Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""

# Needed only for python 3
from functools import reduce

def modify_array(vals):
    modified_list = []
    for val in vals:
        # Use reduce and a simple multiplication lambda to multiply up all values in vals
        modified_list.append(reduce(lambda x, y: x * y, vals) / val)
    return modified_list


def modify_array_no_div(vals):
    modified_list = []
    for idx, val in enumerate(vals):
        # Create temporary removed_list which has all items in vals except for current idx iterator
        removed_list = [tempval for i, tempval in enumerate(vals) if i != idx]
        modified_list.append(reduce(lambda x, y: x * y, vals) / val)
    return modified_list

assert modify_array_no_div([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert modify_array_no_div([3, 2, 1]) == [2, 3, 6]

