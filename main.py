#importing necessary libraries, and functions from stats.py
import sys
from stats import word_count, char_count, char_sort

def get_book_text(path_to_file):  #function designed to open and return the contents of a .txt file as a string
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():  #primary function designed to run bookbot
    if len(sys.argv) != 2:  #check to verify that the proper command is used when initiating bookbot, if not then proper usage is printed and bookbot closes
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        book_file = get_book_text(sys.argv[1])  #function call to convert the given files contents into a string

        num_words = word_count(book_file)  #function calls to generate statistics about the book provided
        char_nums = char_count(book_file)

        sorted_chars = char_sort(char_nums)  #function call to sort the counted characters in descending order

        print("============ BOOKBOT ============")  #series of print statements used to output a report of the provided book to the terminal
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for pair in sorted_chars:  #loop used to iterate over the characters found a remove any non-alphabetical characters
            if pair["char"].isalpha() == True:
                print(f"{pair['char']}: {pair['count']}")
        print("============= END ===============")

main()  #call to main that runs bookbot