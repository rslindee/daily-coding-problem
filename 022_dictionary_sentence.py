"""

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

"""


def decode_sentence(sentence, dictionary):
    found_words = []
    idx = 0
    # While we're not finished with sentence
    while idx < len(sentence):
        # Iterate through each word in dictionary
        found = False
        for word in dictionary:
            # Check if slice starting at iter starts with word
            if sentence[idx:].startswith(word):
                # Increment iter count by length of successful word
                idx += len(word)
                found = True
                found_words.append(word)
                break
        # return null if no match
        if not found:
            return None
    return found_words


assert decode_sentence('thequickbrownfox',
                       ['quick', 'brown', 'the', 'fox']) == ['the', 'quick',
                                                             'brown', 'fox']
