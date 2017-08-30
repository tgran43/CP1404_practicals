text = input("Enter string: ")
word_count = {}
words = text.split()
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
max_length = 0
words = list(word_count.keys())
words.sort()
for word in words:
    if len(word) > max_length:
        max_length = len(word)
for word in words:
    print("{:{}} = {}".format(word, max_length, word_count[word]))
