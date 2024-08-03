def count_words(sentence):
    # split the sentence, and store it in words variable
    words = sentence.split()
    # initiate a dict for lookup and store
    words_count = {}

    # loop through split sentence, which stored in words variable
    for word in words:
        if word in words_count:
            words_count[word] += 1

        else:
            words_count[word] = 1

    return words_count


print(count_words('happy happy happy This handy tool helps you create dummy text for all your layout needs.'))
