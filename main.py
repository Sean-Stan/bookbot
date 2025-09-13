from stats import *
import sys


def get_book_text(file_path):
    with open(file_path) as book:
        return book.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    bookpath = sys.argv[1]
    print(f"Analyzing book found at {bookpath}...")
    book = get_book_text(bookpath)
    word_count = count_words(book)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_characters = sort_character_count(count_characters(book))
    for character in sorted_characters:
        print(f"{character['name']}: {character['num']}")
    print("============= END ===============")

main()