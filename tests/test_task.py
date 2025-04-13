import datetime


def test_task_init(task):
    assert task.name == 'Нужен салат'
    assert task.description == 'Сделать салат когда принесут все овощи'
    assert task.status == 'Ожидает старта'
    assert task.created_at == '20.04.2024'