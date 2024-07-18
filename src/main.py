# Импортируем функции для управления библиотекой из модуля library
from fieldForTests.test_task_effective_mobile.src.library import (add_book, remove_book, search_books,
                                                          display_books, change_status)

if __name__ == "__main__":
    while True:
        print("\nВыберите действие:\n1. Добавить книгу\n2. Удалить книгу\n3. Найти книгу\n4. Показать все книги\n"
              "5. Изменить статус книги\n6. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            # Добавление новой книги
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            book_id = add_book(title, author, year)
            print(f"Книга добавлена с ID: {book_id}")

        elif choice == "2":
            # Удаление книги
            book_id = input("Введите ID книги для удаления: ")
            if remove_book(book_id):
                print("Книга удалена успешно")
            else:
                print("Книга с таким ID не найдена")

        elif choice == "3":
            # Поиск книги по критериям
            criteria = input("Введите название, автора или год издания книги: ")
            results = search_books(criteria)
            if results:
                print("Результаты поиска:")
                for book in results:
                    print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, "
                          f"Year: {book.year}, Status: {book.status}")
            else:
                print("Книги по заданным критериям не найдены")

        elif choice == "4":
            # Вывод всех книг
            print("Список всех книг:")
            display_books()

        elif choice == "5":
            # Изменение статуса книги
            book_id = input("Введите ID книги для изменения статуса: ")
            new_status = input("Введите новый статус (в наличии или выдана): ").lower()
            if new_status == "в наличии" or new_status == "выдана":
                if change_status(book_id, new_status):
                    print("Статус книги изменен успешно")
                else:
                    print("Книга с таким ID не найдена")
            else:
                print("Неверно указан статус. Пожалуйста, введите 'в наличии' или 'выдана'")

        elif choice == "6":
            # Выход из программы
            print("Выход из программы.")
            break

        else:
            print("Неверный номер действия. Пожалуйста, выберите существующий номер.")
