import json
import os

# Определяем абсолютный путь к файлу library.json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'library.json')


def save_library(library):
    """
    Сохраняет библиотеку в файл JSON.

    Args:
        library (list): Список объектов книг (объекты класса Book).

    Returns:
        None

    Переводит каждый объект книги в его словарное представление (используя __dict__)
    и сохраняет список этих словарей в файл JSON с отступами для улучшения читаемости.
    """
    library_data = [book.__dict__ for book in library]  # Преобразование книг в словари
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(library_data, file, ensure_ascii=False, indent=4)
