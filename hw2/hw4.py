def get_most_frequent(words, k):
    n_words = [[w, words.count(w)] for w in set(words)]
    n_words.sort(key=lambda w: w[0])
    n_words.sort(key=lambda w: w[1], reverse=True)
    n_words = [w[0] for w in n_words]
    return n_words[:k]


if __name__ == '__main__':
    list_words = input('Введите слова: ').split()
    n = int(input('Введите k: '))
    print(get_most_frequent(list_words, n))
