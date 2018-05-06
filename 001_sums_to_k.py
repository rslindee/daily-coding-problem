""" Given a list of numbers, return whether any two sums to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def check_sum(vals, k):
    found = False;
    for idx, first_val in enumerate(vals[:-1]):
        for second_val in vals[idx+1:]:
            if (first_val + second_val == k):
                found = True;
                break;
        if (found == True):
            break;
    return found;

values = [1, 2, 3, 4]
sum_val = 5

assert check_sum([10, 15, 3, 7], 17) == True
