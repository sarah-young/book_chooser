from bs4 import BeautifulSoup
import requests
from random import randrange
import time

library_uri = "http://themorningnews.org/article/the-year-in-fiction-2019"

def random_book(books, number_of_books, previous_pick = -1):
    """Chooses a random book from a list."""
    _index = randrange(0, number_of_books - 1)
    while _index == previous_pick:
        _index = randrange(0, number_of_books - 1)
    print()
    print()
    print("How about this book?")
    print(books[_index]['title'])
    print("More information: " + books[_index]['url'])
    print("Would you like to choose this book? (y/n/ar; ar = already read)")
    return _index

def get_book_list():
    r  = requests.get(library_uri)
    data = r.text
    soup = BeautifulSoup(data, features="html.parser")
    soupy_books = soup.find_all('h2')
    books = []
    for book in soupy_books:
        if book and book.em:
            url = book.a['href']
            title_and_author = book.text
            books.append({ "title": title_and_author, "url": url })
    return books

def run_prompts():
    books = get_book_list()
    number_of_books = len(books)
    if number_of_books < 1:
        print("Uh oh, no books to choose from!")
        return
    print("There are %s books to choose from." % number_of_books)
    print("Would you like to choose a book? (y/n): ")
    chosen_input = input()
    if chosen_input == 'n':
        print("OK, goodbye.")
    if chosen_input == 'y':
        selected_book = -1
        while True:
            selected_book = random_book(books, number_of_books, selected_book)
            book_response = input()
            if book_response == 'y':
                print("Hooray! Enjoy reading " + books[selected_book]['title'])
                break
            if book_response == 'ar':
                books.pop(selected_book)
                number_of_books = number_of_books = len(books)
                print("OK, I've removed that book from your library. There are now %s books to choose from." % number_of_books)
            if book_response == 'exit':
                break

if __name__ == "__main__":
    run_prompts()
