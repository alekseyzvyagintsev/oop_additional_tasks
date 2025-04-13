import pytest

from src.task import Task
from src.user import User


@pytest.fixture
def first_user():
    return User(
        'user1',
        'user1@mail.ru',
        'User1',
        'Useridse',
        [
            Task('Купить огурцы', 'Огурцы нужны для салата на вечер'),
            Task('Купить помидоры', 'Помидоры нужны для салата на вечер')
        ]
    )


@pytest.fixture
def second_user():
    return User(
        'user2',
        'user2@mail.ru',
        'User2',
        'Userovich',
        [
            Task('Купить лук', 'Лук нужен для салата на вечер'),
            Task('Купить перец', 'Перец нужен для салата на вечер'),
            Task('Купить масло', 'Масло нужно для салата на вечер')

        ]
    )


@pytest.fixture
def task():
    return Task('Нужен салат', 'Сделать салат когда принесут все овощи', created_at='20.04.2024')