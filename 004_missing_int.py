""" Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

TODO: Improve time
"""


def find_missing(nums):
    # Check every potential value up to the length
    for i in range(len(nums)):
        found = False
        # Check to see if the number already exists in our list
        for x in nums:
            if ((x > 0) and (x == (i+1))):
                found = True
                break
        # The value was not found and thus is our lowest
        if (found == False):
            return (i+1)
    # We never found a missing value, so it must be the next highest
    return len(nums)+1

assert find_missing([3, 4, -1, 1]) == 2
assert find_missing([1, 2, 0]) == 3
print ('Tests passed!')
