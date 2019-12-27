import unittest
import mock
from bs4 import BeautifulSoup
import requests
from random import randrange
from tournamentofbooks import random_book, get_book_list, run_prompts

class NamesTestCase(unittest.TestCase):

    def test_random_book(self):
       books = [{'title': '1', 'url': 'www.google.com'}, {'title': '2', 'url': 'apple.com' }, {'title': '3', 'url': 'www.facebook.com'}]
       books_length = len(books)
       result = random_book(books, books_length)
       self.assertIn(result, range(0, len(books)))

    def test_get_book_list(self):
        result = get_book_list()
        self.assertEqual(len(result), 62)