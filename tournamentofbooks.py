from bs4 import BeautifulSoup
import requests
from random import randrange

def random_book(books, number_of_books):
    "Chooses a random book from a list."
    _index = randrange(number_of_books-1)
    print()
    print()
    print("How about this book?")
    print(books[_index]['title'])
    print("More information: " + books[_index]['url'])
    print("Would you like to choose this book? (y/n/ar; ar = already read)")
    return _index

def get_book_list():
    r  = requests.get("http://themorningnews.org/article/the-year-in-fiction-2019")
    data = r.text
    soup = BeautifulSoup(data, features="html.parser")
    soupy_books = soup.find_all('h2')
    books = []
    for book in soupy_books:
        if book and book.em:
            url = book.a['href']
            title_and_author = book.text
            books.append({"title": title_and_author, "url": url})
    return books

def first_question(books):
    number_of_books = len(books)
    return "There are " + str(number_of_books) + " books to choose from. \nWould you like to choose a book? (y/n): "

def handle_answer(chosen_input, books):
    if chosen_input == 'n':
        print("OK, goodbye.")
    if chosen_input == 'y':
        number_of_books = len(books)
        choosing_a_book = True
        while choosing_a_book == True:
            selected_book = random_book(books, number_of_books)
            book_chosen = input()
            if book_chosen == 'y':
                print("Hooray! Enjoy reading " + books[selected_book]['title'])
                choosing_a_book = False
            if book_chosen == 'ar':
                books.pop(selected_book)
                number_of_books = len(books)
                print("OK, I've removed that book from your library. There are now " + str(number_of_books) + " books to choose from.")

def run_prompts():
    books = get_book_list()
    message = first_question(books)
    print(message)
    chosen_input = input()
    handle_answer(chosen_input, books)

if __name__ == "__main__":
    run_prompts()





