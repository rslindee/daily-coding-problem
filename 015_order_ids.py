""" You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""

import collections

N = 5

orders = collections.deque(maxlen=N)

def record(order_id):
    orders.appendleft(order_id)

def get_last(i):
    return orders[i-1]

record(1)
record(2)
record(3)
record(4)
record(5)
record(6)

assert get_last(1) == 6
assert get_last(N) == 2
