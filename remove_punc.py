import string


def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)


sentence = str(input('Enter a sentence: '))

print(remove_punctuation(sentence))
