# If you downloaded words from the course website,
# change me to the path to the downloaded file.
DICTIONARY_FILE = '/usr/share/dict/words'


def load_english():
    with open(DICTIONARY_FILE) as f:
        return [word[:-1] for word in f if len(word) > 2]


if __name__ == '__main__':
    english = load_english()
    print(len(english))
