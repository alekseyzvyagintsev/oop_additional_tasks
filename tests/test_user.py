

def test_user_init(first_user, second_user):
    assert first_user.username == 'user1'
    assert first_user.imail == 'user1@mail.ru'
    assert first_user.first_name == 'User1'
    assert first_user.last_name == 'Useridse'
    assert len(first_user.task_list) == 2

    assert first_user.users_count == 2
    assert second_user.users_count == 2

    assert second_user.all_tasks_count == 5