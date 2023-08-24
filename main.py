source = 'books/frankenstein.txt'  #creating variable for source text

with open(source) as f:   #obtain source text and convert to string
    file_contents = f.read()

words = file_contents.split()   #separate string on whitespace into list
word_count = len(words) #count words
letter_count = {}   #create dictionary to index letters with count

for word in words:  #statement separating characters from list then counting, case insensitive
    for letter in word:
        lowercase = letter.lower()
        if lowercase in letter_count:
            letter_count[lowercase] += 1
        else:
            letter_count[lowercase] = 1

letter_list = []    #creating list solely for letters

for letter in letter_count: #separating letters into intended list
    if letter.isalpha():
        letter_list.append(letter)

letter_list.sort()  #sorting letters

print(f"--- Begin report of {source} ---")  #print report on source text
print(f"{word_count} words found in the document")
print("")

for letter in letter_list:
    print(f"The {letter} character was found {letter_count[letter]} times")
print("--- End report ---")