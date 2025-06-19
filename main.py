#from stats import get_book_text
#from stats import count_words
#from stats import count_char
#from stats import sort_list
from stats import *
import sys


def main():
    #bookPath = "books/frankenstein.txt"
    bookPath = sys.argv[1]

    #get text
    book = get_book_text(bookPath)

    #get word count
    wordcount = count_words(book)

    #get charecter count
    bookCharCount = count_char(book)

    #get list of char in order
    orderedCharCount = sort_list(bookCharCount)

    #pretty print out
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {bookPath}')
    print('----------- Word Count ----------')
    print(f"Found {wordcount} total words")
    print('--------- Character Count -------')
    for dic in orderedCharCount:
        if dic['char'].isalpha():
            print(f'{dic["char"]}: {dic["num"]}')
    print('============= END ===============')


if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    main()