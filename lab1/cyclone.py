from lab1.special_words import load_english

english = load_english()


def alphabetical_order(ch1, ch2):
    return ord(ch2) - ord(ch1) >= 0


def is_cyclone_word(word):
    n = 0
    for i in range(1, len(word)):
        if not alphabetical_order(word[n], word[n + i * (-1) ** i]):
            return False
        n = n + i * (-1) ** i
    return True


def is_cyclone_phrase(phrase):
    word_list = phrase.split()
    for word in word_list:
        if not is_cyclone_word(word):
            return False
    return True


print(is_cyclone_phrase("adjourned"))  # => True
print(is_cyclone_phrase("settled"))  # => False
print(is_cyclone_phrase("all alone at noon"))  # => True
print(is_cyclone_phrase("by myself at twelve pm"))  # => False
print(is_cyclone_phrase("acb"))  # => True
print(is_cyclone_phrase(""))  # => True

# list of all cyclone words
cyclone_list = [word for word in english if is_cyclone_word(word)]
print(len(cyclone_list))
