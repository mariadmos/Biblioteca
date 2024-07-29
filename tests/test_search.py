import unittest
from src.search import search_book

class TestSearchBook(unittest.TestCase):
    def test_search_book(self):
        isbn_to_search = "978-0-13-110362-7"
        result = search_book(isbn_to_search)
        self.assertIsNotNone(result["bibliotecária"])
        self.assertIsNotNone(result["gerente"])

if __name__ == '__main__':
    unittest.main()

