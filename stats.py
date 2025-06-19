def get_book_text(bookPath):
    with open(bookPath) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

def count_char(book):
    book = book.lower()
    count = dict()

    for char in book:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_list(dict):
    orderedList = []

    def sort_by(dicList):
        return dicList['num']

    for key in dict:
        orderedList.append({"char" : key, "num" : dict[key]})

    orderedList.sort(key=sort_by, reverse=True)

    return orderedList
