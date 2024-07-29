import threading
import time
import random
from src.available_books import available_books
from src.borrowed_books import borrowed_books

def search_available_books(isbn, result, role):
    time.sleep(random.uniform(0.1, 0.3))  # Simula tempo de pesquisa
    if isbn in available_books:
        result[role] = available_books[isbn]
    else:
        result[role] = None

def search_borrowed_books(isbn, result, role):
    time.sleep(random.uniform(0.1, 0.3))  # Simula tempo de pesquisa
    if isbn in borrowed_books:
        result[role] = borrowed_books[isbn]
    else:
        result[role] = None

def search_book(isbn):
    result = {"bibliotecária": None, "gerente": None}
    
    librarian_thread = threading.Thread(target=search_available_books, args=(isbn, result, "bibliotecária"))
    manager_thread = threading.Thread(target=search_borrowed_books, args=(isbn, result, "gerente"))
    
    librarian_thread.start()
    manager_thread.start()
    
    librarian_thread.join()
    manager_thread.join()
    
    return result

if __name__ == "__main__":
    isbn_to_search = "978-0-13-110362-7"
    search_result = search_book(isbn_to_search)
    
    print(f"Resultado da pesquisa para o ISBN {isbn_to_search}:")
    print(f"Bibliotecária encontrou: {search_result['bibliotecária']}")
    print(f"Gerente encontrou: {search_result['gerente']}")
