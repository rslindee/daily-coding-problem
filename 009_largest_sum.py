"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def largest_sum(nums):
    big = []
    bigger = []
    biggest = []
    for idx, val in enumerate(nums):
        if not biggest or val > biggest[0]:
            big = list(bigger)
            bigger = list(biggest)
            biggest = [val, idx]
        elif not bigger or val > bigger[0]:
            big = list(bigger)
            bigger = [val, idx]
        elif not big or val > big[0]:
            big = [val, idx]
    if (abs(biggest[1] - bigger[1]) > 1):
        return biggest[0] + bigger[0]
    else:
        if (abs(bigger[1] - big[1]) > 1):
            return bigger[0] + big[0]
        else:
            return biggest[0] + big[0]



assert largest_sum([2, 4, 6, 8]) == 12
assert largest_sum([5, 1, 1, 5]) == 10
