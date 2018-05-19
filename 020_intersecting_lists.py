"""Given two singly linked lists that intersect at some point, find the
intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
return the node with value 8.

In this example, assume nodes with the same value are the exact same node
objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and
constant space.

TODO: Test
"""


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


def intersecting_lists(list_1, list_2):
    # Find length of list 1
    length_1 = 0
    iter_node = list_1
    while iter_node.next_node:
        length_1 += 1
        iter_node = iter_node.next_node
    length_2 = 0
    iter_node = list_2
    while iter_node.next_node:
        length_2 += 1
        iter_node = iter_node.next_node

    length_diff = abs(length_1 - length_2)

    if length_1 > length_2:
        iter_node = length_1
        iter_node_alt = length_2
    else:
        iter_node = length_2
        iter_node_alt = length_1

    while length_diff > 0:
        iter_node = iter_node.next
        length_diff -= 1

    while iter_node is not iter_node_alt:
        iter_node = iter_node.next
        iter_node_alt = iter_node_alt.next

    return iter_node.val
