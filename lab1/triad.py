from lab1.special_words import load_english

english = load_english()


def is_triad_word(word):
    return word[::2] in english and word[1::2] in english


def is_triad_phrase(phrase):
    word_list = phrase.split()
    for word in word_list:
        if not is_triad_word(word):
            return False
    return word_list != []


print(is_triad_phrase("learned theorem"))  # => True
print(is_triad_phrase("studied theories")) # => False
print(is_triad_phrase("wooded agrarians"))  # => True
print(is_triad_phrase("forrested farmers"))  # => False
print(is_triad_phrase("schooled oriole"))  # => True
print(is_triad_phrase("educated small bird"))  # => False
print(is_triad_phrase("a"))  # => False
print(is_triad_phrase(""))  # => False

# bonus task - kol-vo slov triad
print(len([word for word in english if is_triad_word(word)]))
