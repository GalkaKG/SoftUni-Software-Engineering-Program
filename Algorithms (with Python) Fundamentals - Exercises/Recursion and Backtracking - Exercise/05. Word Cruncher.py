def word_cruncher(idx, words_count, indexes_words, used_words, target):
    if idx >= len(target):
        print(' '.join(used_words))
        return
    if idx not in indexes_words:
        return
    for word in indexes_words[idx]:
        if words_count[word] == 0:
            continue
        used_words.append(word)
        words_count[word] -= 1

        word_cruncher(idx + len(word), words_count, indexes_words, used_words, target)

        used_words.pop()
        words_count[word] += 1


words = input().split(', ')
target = input()

words_count = {}
indexes_words = {}


for word in words:
    if word in words_count:
        words_count[word] += 1
        continue

    words_count[word] = 1

    try:
        index = 0
        while True:
            index = target.index(word, index)

            if index not in indexes_words:
                indexes_words[index] = []
            indexes_words[index].append(word)
            index += len(word)
    except ValueError:
        ...

# print(words_count)
# print(indexes_words)

word_cruncher(0, words_count, indexes_words, [], target)
