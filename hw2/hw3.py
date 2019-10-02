def count_unique_codes(words):
    morse_base = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    ]
    alphabet = [chr(l) for l in range(ord('a'), ord('z') + 1)]
    alphabet_dict = {}
    for l, m in zip(alphabet, morse_base):
        alphabet_dict[l] = m

    # 1st method using built-in functions
    # return len({w.translate(str.maketrans(alphabet_dict)) for w in words})

    # 2nd method
    # new_words = set()
    # for w in words:
    #     morse_word = ''
    #     for i in range(len(w)):
    #         morse_word = morse_word + alphabet_dict[w[i]]
    #     new_words.add(morse_word)
    # return len(new_words)

    # 3rd method
    new_words = set()
    for w in words:
        morse_word = w
        for l in set(w):
            morse_word = morse_word.replace(l, alphabet_dict[l])
        new_words.add(morse_word)
    return len(new_words)


if __name__ == '__main__':
    list_words = input('words = ').split()
    print(count_unique_codes(list_words))
