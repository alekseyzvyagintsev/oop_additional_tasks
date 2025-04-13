from src.task import Task


class User:
    username = str
    email = str
    first_name = str
    last_name = str
    task_list = list
    users_count = 0
    all_tasks_count = 0

    def __init__(self, username, email, first_name, last_name, task_list=None):
        self.username = username
        self.imail = email
        self.first_name = first_name
        self.last_name = last_name
        self.task_list = task_list if task_list else []
        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0


if __name__ == '__main__':
    task1 = Task('Полёт на воздушном шаре', 'Кругосветка на воздушном шаре')
    task2 = Task('Поход на подводной лодке', 'Кругосветка на подводной лодке')
    task3 = Task('Полёт через Альпы', 'Кругосветка через Альпы на Вашингтон')
    task4 = Task('Поход в баню', 'Кругосветка через баню')
    user = User('fyodor', 'fyodor@gmail.com', 'Фёдор', 'Конюхов', [task1, task2, task3, task4])

    print(user.username)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.task_list)
    print(user.users_count)
    print(user.all_tasks_count)