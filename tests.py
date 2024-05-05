import pytest

from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name_book', ['', 'Гидразинокарбонилметилбромфенилдигидробенздиазепин'])
    def test_add_new_book_not_add_invalid_name_book(self, collector, name_book):
        collector.add_new_book(name_book)

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_not_add_wrong_genre(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Хоррор')

        assert collector.get_book_genre('Оно') == ''

    def test_get_book_genre_shows_genre(self, collector):
        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')

        assert collector.get_book_genre('Солярис') == 'Фантастика'

    def test_get_books_for_children_not_add_genre_age_rating(self, collector):
        collector.add_new_book('Убийство на улице Морг')
        collector.set_book_genre('Убийство на улице Морг', 'Детективы')

        assert collector.get_books_for_children() == []

    def test_get_books_for_children_add_book_genre_for_children(self, collector):
        collector.add_new_book('Лев и птичка')
        collector.set_book_genre('Лев и птичка', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Лев и птичка']

    def test_get_books_with_specific_genre_get_books(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.add_new_book('Автостопом по галактике')
        collector.set_book_genre('Автостопом по галактике', 'Фантастика')

        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    @pytest.mark.parametrize('name_book, genre', [['Лев и птичка', 'Мультфильмы']])
    def test_get_books_genre_return_dict_books_genre(self, collector, name_book, genre):
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)

        assert collector.get_books_genre() == {'Лев и птичка': 'Мультфильмы'}

    def test_add_book_in_favorites_add_book(self, collector):
        collector.add_new_book('Убийство на улице Морг')
        collector.add_book_in_favorites('Убийство на улице Морг')

        assert 'Убийство на улице Морг' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_add_added_book(self, collector):
        collector.add_new_book('Убийство на улице Морг')
        collector.add_book_in_favorites('Убийство на улице Морг')
        collector.add_new_book('Убийство на улице Морг')
        collector.add_book_in_favorites('Убийство на улице Морг')

        assert collector.get_list_of_favorites_books().count('Убийство на улице Морг') == 1

    def test_delete_book_from_favorites_delete_book(self, collector):
        collector.add_new_book('Автостопом по галактике')
        collector.add_book_in_favorites('Автостопом по галактике')
        collector.delete_book_from_favorites('Автостопом по галактике')

        assert collector.get_list_of_favorites_books().count('Автостопом по галактике') == 0

    def test_get_list_of_favorites_books_shows_list(self, collector):
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_new_book('Гарри Поттер и тайная комната')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и тайная комната')

        assert len(collector.get_list_of_favorites_books()) == 2
