# qa_python

В рамках проекта 4-го спринта написаны юнит тесты для класса class BooksCollector. 
Для тестирования методов класса были применены инструменты: фреймфорк pytest, параметризация, фикстуры.

Создана фикстура на создание объекта класса BooksCollector
Протестированы следующие тестовые сценарии:
1. Добавление двух книг test_add_new_book_add_two_books
2. Книги с невалидным названием не добавляются в словарь test_add_new_book_not_add_invalid_name_book
3. Для добавленной книги не устанавливается недоступный жанр test_set_book_genre_not_add_wrong_genre
4. Получение жанра книги по ее названию test_get_book_genre_shows_genre
5. Книги с возрастным рейтингом отсутствуют в списке книг для детей test_get_books_for_children_not_add_genre_age_rating
6. Книги без возрастного рейтинга присутствуют в списке книг для детей test_get_books_for_children_add_book_genre_for_children
7. Получение списка книг с определенным жанром test_get_books_with_specific_genre_get_books
8. Получение словаря с книгой и жанром test_get_books_genre_return_dict_books_genre
9. Добавление книги в избранное test_add_book_in_favorites_add_book
10. Книга не добавляется в избранное повторно test_add_book_in_favorites_not_add_added_book
11. Удаление книги из избранного test_delete_book_from_favorites_delete_book
12. Получение списка избранных книг test_get_list_of_favorites_books_shows_list