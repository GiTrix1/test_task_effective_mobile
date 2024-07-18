import random

# # Разкоммитить две строчки для тестов
# from src.book import Book  # Импорт класса Book из модуля book
# from src.utils import save_library  # Импорт функции save_library из модуля utils

from book import Book  # Импорт класса Book из модуля book
from utils import save_library  # Импорт функции save_library из модуля utils

# Глобальная переменная для хранения библиотеки книг
library = []


def add_book(title, author, year):
    """
    Добавляет новую книгу в библиотеку.

    Args:
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.

    Returns:
        str: Уникальный идентификатор добавленной книги.
    """
    random_book_id = str(random.randint(1, 1000000))  # Генерация случайного ID для книги
    book = Book(title, author, year)  # Создание экземпляра книги
    book.id = random_book_id  # Присвоение ID книге
    library.append(book)  # Добавление книги в библиотеку
    save_library(library)  # Сохранение библиотеки в файл
    return book.id  # Возвращение ID добавленной книги


def remove_book(book_id):
    """
    Удаляет книгу из библиотеки по её идентификатору.

    Args:
        book_id (str): Идентификатор книги для удаления.

    Returns:
        bool: True, если книга была успешно удалена, False в противном случае.
    """
    global library  # Объявление глобальной переменной library
    for book in library:
        if book.id == book_id:
            library.remove(book)  # Удаление книги из библиотеки
            save_library(library)  # Сохранение библиотеки в файл
            return True
    return False


def search_books(criteria):
    """
    Поиск книг в библиотеке по заданным критериям.

    Args:
        criteria (str): Критерий поиска (название, автор или год издания книги).

    Returns:
        list: Список книг, удовлетворяющих критериям поиска.
    """
    results = []
    for book in library:
        if criteria.lower() in book.title.lower() \
                or criteria.lower() in book.author.lower() \
                or criteria == str(book.year):
            results.append(book)
    return results


def display_books():
    """
    Выводит информацию о всех книгах в библиотеке.
    """
    for book in library:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")


def change_status(book_id, new_status):
    """
    Изменяет статус книги в библиотеке по её идентификатору.

    Args:
        book_id (str): Идентификатор книги.
        new_status (str): Новый статус книги.

    Returns:
        bool: True, если статус книги был успешно изменен, False в противном случае.
    """
    for book in library:
        if book.id == book_id:
            book.status = new_status  # Изменение статуса книги
            save_library(library)  # Сохранение библиотеки в файл
            return True
    return False
