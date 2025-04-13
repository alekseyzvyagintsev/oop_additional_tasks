import json
import os

from src.user import User
from src.task import Task

def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def create_object_from_json(data):
    users = []
    for user in data:
        tasks = []
        for task in user.get('task_list'):
            tasks.append(Task(**task))
        user['task_list'] = tasks
        users.append(User(**user))

    return users

if __name__ == '__main__':
    data_tasks = read_json('../data/data.json')
    last_dict = create_object_from_json(data_tasks)
    print(last_dict)

    print(last_dict[0].username)
    print(last_dict[0].task_list)