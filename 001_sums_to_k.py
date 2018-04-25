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

print 'k is: ', check_sum(values, sum_val)

