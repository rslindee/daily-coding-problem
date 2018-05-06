""" A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

TODO: Finish
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        else
            return False

    def is_unival(self, val):
        if self.val != val:
            return False
        else:
            # Check both sides, if they exist
            unival = True
            if self.left is not None and (if (is_unival(self.left, val) is not True)):
                unival = False
            if self.right is not None and (if (is_unival(self.right, val) is not True)):
                unival = False
            return unival


def count_unival(node):
    count = 0
    if node.is_leaf is True:
        return 1
    if node.is_unival(node.val):
        count += 1
    if (node.left is not None):
        count += count_unival(node.left)
    if (node.right is not None):
        count += count_unival(node.right)
    return count
