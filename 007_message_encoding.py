"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""
# Create mapping
mapping = [str(x) for x in range(1, 27)]

def number_ways_decoded(message):
    if not message:
        return 1
    count = 0
    for i in mapping:
        if message.startswith(i):
            # Recursively count rest of message permutations
            count += number_ways_decoded(message[len(i):])
    return count


assert number_ways_decoded('111') == 3
