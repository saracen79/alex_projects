import pytest


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Alex'
        self.second_name = 'Morozov'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


    def test_change_name(user):
        assert user.name == 'Alex'


    def test_change_second_name(user):
        assert user.second_name == 'Morozov'
        
