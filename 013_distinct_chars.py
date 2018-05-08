""" Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def substring(s, k):
    longest_string = []
    # Turn into list
    list_s = list(s)
    # Iterate through entire list
    for idx, val in enumerate(list_s):
        # Start collecting characters until letters_left runs out
        letters_left = k
        used_letters = set()
        substring = []
        # Start building a substring
        for char in list_s[idx:]:
            used_letters.add(char)
            # If we reach the max size allowed, stop collecting
            if len(used_letters) > k:
                break
            else:
                substring.append(char)
        if len(substring) > len(longest_string):
            longest_string = substring
    return ''.join(longest_string)


assert substring("abcba", 2) == "bcb"
