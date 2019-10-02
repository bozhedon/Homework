from lab1.special_words import load_english

english = load_english()


def character_gap(ch1, ch2):
    return abs(ord(ch1) - ord(ch2))


def is_surpassing_word(word):
    length = len(word)
    if length > 2:
        for i in range(2, length):
            if character_gap(word[i], word[i - 1]) < character_gap(word[i - 1], word[i - 2]):
                return False
    return True


def is_surpassing_phrase(phrase):
    word_list = phrase.split()
    for word in word_list:
        if not is_surpassing_word(word):
            return False
    return True


print(is_surpassing_phrase("superb subway"))  # => True
print(is_surpassing_phrase("excellent train"))  # => False
print(is_surpassing_phrase("porky hogs"))  # => True
print(is_surpassing_phrase("plump pigs"))  # => False
print(is_surpassing_phrase("turnip fields"))  # => True
print(is_surpassing_phrase("root vegetable lands"))  # => False
print(is_surpassing_phrase("a"))  # => True
print(is_surpassing_phrase(""))  # => True

# list of all surpassing words
surpassing_list = [word for word in english if is_surpassing_word(word)]
print(len(surpassing_list))
