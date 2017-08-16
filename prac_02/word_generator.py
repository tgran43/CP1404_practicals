"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
import time

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
FORMAT = 'cv'
word_format = ""
word_length = random.randint(2, 8)
start_time = time.time()
for i in range(word_length):
    word_format += random.choice(FORMAT)
# word_format = "ccvcvvc"
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
counter = 0
dog_counter = 0
trey_counter = 0
while word != 'quizzed':
    counter += 1
    word_format = ""
    word_length = random.randint(2, 8)
    for i in range(word_length):
        word_format += random.choice(FORMAT)
    # word_format = "ccvcvvc"
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    # print(word)
    if word == 'dog':
        dog_counter += 1
        print(dog_counter)
    if word == 'trey':
        trey_counter += 1

elapsed_time = time.time() - start_time
print(counter)
print(dog_counter)
print(trey_counter)
print(elapsed_time)
