def alpha_score(upper_letters):
    """Return the alphanumeric sum of letters in a string, where A == 1 and Z == 26.

    The argument upper_letters must be composed entirely of capital letters.
    """
    return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))


print(alpha_score('ABC'))  # => 6 = 1 ('A') + 2 ('B') + 3 ('C')


def two_best(words):
    """Return the two words whose alphanumeric score of uppercase letters is the highest."""
    words.sort(key=lambda word: alpha_score(filter(lambda l: str.isupper(l), word)), reverse=True)
    return words[:2]


print(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))
