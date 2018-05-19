"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find
the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

NOTES:
    Order all events into a single lists and apply a type: arrival or departure
    Walk through the list, increment the num_classrooms for arrival, subtract for departure
"""


def get_time(pair):
    return pair[0]


def min_rooms(intervals):
    # Create list of events
    events = []
    for interval in intervals:
        events.append([interval[0], 'start'])
        events.append([interval[1], 'end'])

    # Sort list of events by time
    events.sort(key=get_time)
    # Walk through list and get highest count
    num_classes = 0
    max_classes = 0
    for event in events:
        if event[1] == 'start':
            num_classes += 1
        else:
            num_classes -= 1
        if num_classes > max_classes:
            max_classes = num_classes

    return max_classes


assert min_rooms([[30, 75], [0, 50], [60, 150]]) == 2
