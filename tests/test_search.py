import unittest
from src.search import search_book

class TestSearchBook(unittest.TestCase):
    def test_search_book_found(self):
        isbn = "978-0-13-110362-7"  
        result = search_book(isbn)
        self.assertIsNotNone(result['gerente'])
        self.assertEqual(result['gerente']['title'], "Livro D")
        
    def test_search_book_not_found(self):
        isbn = "000-0-00-000000-0"
        result = search_book(isbn)
        self.assertIsNone(result['bibliotecária'])
        self.assertIsNone(result['gerente'])

if __name__ == "__main__":
    unittest.main()

