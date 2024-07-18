import os
import sys

# Установим текущий рабочий каталог в корень проекта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from src.library import (add_book, remove_book, search_books, change_status, display_books, library)
from src.utils import save_library


class TestLibraryManagement(unittest.TestCase):

    def setUp(self):
        """Устанавливает начальные условия для тестов."""
        # Очищаем библиотеку перед каждым тестом
        self.original_library = library.copy()
        library.clear()
        save_library(library)

    def tearDown(self):
        """Восстанавливает начальные условия после тестов."""
        # Восстанавливаем оригинальную библиотеку после каждого теста
        global library
        library = self.original_library.copy()
        save_library(library)

    def test_add_book(self):
        """Тест добавления книги."""
        add_book("Test Book 1", "Test Author 1", 2021)
        self.assertEqual(len(library), 1)
        self.assertEqual(library[0].title, "Test Book 1")
        self.assertEqual(library[0].author, "Test Author 1")
        self.assertEqual(library[0].year, 2021)
        self.assertEqual(library[0].status, "в наличии")

    def test_remove_book(self):
        """Тест удаления книги."""
        book_id = add_book("Test Book 2", "Test Author 2", 2022)
        self.assertTrue(remove_book(book_id))
        self.assertEqual(len(library), 0)
        self.assertFalse(remove_book(book_id))  # Попытка удалить несуществующую книгу

    def test_search_books(self):
        """Тест поиска книг."""
        add_book("Test Book 3", "Test Author 3", 2023)
        add_book("Test Book 4", "Test Author 4", 2024)
        results = search_books("Test Book 3")
        self.assertEqual(len(results), 1)
        results = search_books("Test Author 3")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Test Book 3")

    def test_change_status(self):
        """Тест изменения статуса книги."""
        book_id = add_book("Test Book 5", "Test Author 5", 2025)
        self.assertTrue(change_status(book_id, "выдана"))
        self.assertFalse(change_status(999, "выдана"))  # Попытка изменить статус несуществующей книги


if __name__ == '__main__':
    unittest.main()
