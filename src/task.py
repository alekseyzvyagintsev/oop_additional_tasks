import datetime


class Task:
    name = str,
    description = str,
    status = str,
    created_at = str


    def __init__(self, name, description, status="Ожидает старта", created_at=None):
        self.name = name
        self.description = description
        self.status = status
        self.created_at = created_at if created_at else datetime.date.today().strftime('%d.%m.%Y')


if __name__ == '__main__':
    my_task = Task('Купить овощей', 'Овощи нужны для салата на вечер')

    print(my_task.name)
    print(my_task.description)
    print(my_task.status)
    print(my_task.created_at)