with open('books/frankenstein.txt') as f:
    file_contents = f.read()

words = file_contents.split()
letter_count = {}

for word in words:
    for letter in word:
        lowercase = letter.lower()
        if lowercase in letter_count:
            letter_count[lowercase] += 1
        else:
            letter_count[lowercase] = 1

print(letter_count)