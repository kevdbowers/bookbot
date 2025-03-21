import sys
from stats import word_count, char_count, char_sort

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        book_file = get_book_text(sys.argv[1])

        num_words = word_count(book_file)
        char_nums = char_count(book_file)

        sorted_chars = char_sort(char_nums)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for pair in sorted_chars:
            if pair["char"].isalpha() == True:
                print(f"{pair['char']}: {pair['count']}")
        print("============= END ===============")

main()