import time
import unittest
from unittest.mock import patch, Mock, MagicMock

import random

from ..view_model import ViewModel, ViewWindows


def put_random_value(model):
    model.user_name = str(random.randint(0, 1000))
    model.window = random.choice(list(ViewWindows))
    model.user_id = random.randint(0, 1000)
    model.user_login = str(random.randint(0, 1000))
    model.card = [random.randint(0, 1000) for _ in range(random.randint(1, 5))]
    model.game_id = random.randint(0, 1000)
    model.info_window = None


class TestClientRequests(unittest.TestCase):

    def setUp(self):
        self.model = ViewModel()
        put_random_value(model=self.model)

    def assert_empty_info(self, model):
        self.assertEqual(model.info_window, None)
        self.assertEqual(model.user_name, None)
        self.assertEqual(model.user_id, None)
        self.assertEqual(model.user_login, None)
        self.assertEqual(model.game_id, None)
        self.assertEqual(model.card, [])

    def test_init(self):
        new_model = ViewModel()
        self.assert_empty_info(model=new_model)

    def test_put_info_window(self):
        self.model.put_info_window("Test name", 0.5)
        self.assertEqual(self.model.info_window, "Test name")
        self.model.put_info_window("Second info", 1)
        self.assertEqual(self.model.info_window, "Test name")
        time.sleep(1)
        self.assertEqual(self.model.info_window, "Second info")

    def test_go_to_main_menu_window(self):
        put_random_value(self.model)
        self.model.go_to_main_menu_window()
        self.assertEqual(self.model.window, ViewWindows.main_menu)

    def test_go_to_login_window(self):
        put_random_value(self.model)
        self.model.go_to_login_window()
        self.assertEqual(self.model.window, ViewWindows.login)

    def test_go_to_registration_window(self):
        put_random_value(self.model)
        self.model.go_to_registration_window()
        self.assertEqual(self.model.window, ViewWindows.registration)
        self.assert_empty_info(model=self.model)

    def test_go_to_initial_window(self):
        put_random_value(self.model)
        self.model.go_to_initial_window()
        self.assert_empty_info(model=self.model)
        self.assertEqual(self.model.window, ViewWindows.initial_menu)

    def test_go_to_game_menu(self):
        self.model.game_id = 1
        self.model.user_id = 2
        self.model.user_login = "test"
        self.model.user_name = "gab1k"
        self.model.go_to_game_menu()
        self.assertEqual(self.model.window, ViewWindows.game)
        self.assertEqual(self.model.game_id, 1)
        self.assertEqual(self.model.user_id, 2)
        self.assertEqual(self.model.user_login, "test")
        self.assertEqual(self.model.user_name, "gab1k")

    def test_sign_out(self):
        put_random_value(self.model)
        self.model.sign_out()
        self.assertEqual(self.model.window, ViewWindows.initial_menu)
        self.assert_empty_info(model=self.model)

    @patch("client.view_model.ClientRequests.login_user")
    def test_login_not_ok(self, req_mock):
        response = MagicMock()
        response.status = 42
        req_mock.return_value = response

        self.model.login_user("gab1k", "abacaba")

        req_mock.assert_called_once_with(_user_login="gab1k", _password="abacaba")
        self.assertEqual(self.model.info_window, "42")

    @patch("client.view_model.ClientRequests.login_user")
    def test_login_ok(self, req_mock):
        put_random_value(model=self.model)
        response = MagicMock()
        response.status = 0
        response.user_info.id = 42
        response.user_info.name = "test_name"
        response.user_info.login = "test_login"
        req_mock.return_value = response

        self.model.login_user("test_login", "test_password")

        req_mock.assert_called_once_with(_user_login="test_login", _password="test_password")
        self.assertEqual(self.model.user_login, "test_login")
        self.assertEqual(self.model.user_name, "test_name")
        self.assertEqual(self.model.user_id, 42)
        self.assertEqual(self.model.window, ViewWindows.main_menu)

    @patch("client.view_model.ClientRequests.register_user")
    def test_register_not_ok(self, req_mock):
        response = MagicMock()
        response.status = 42
        req_mock.return_value = response
        self.model.register_user("login", "name", "123", "321")
        req_mock.assert_called_once_with(_user_login="login", _user_name="name", _password1="123", _password2="321")
        self.assertEqual(self.model.info_window, "42")

    @patch("client.view_model.ClientRequests.register_user")
    def test_register_ok(self, req_mock):
        response = MagicMock()
        response.status = 0
        req_mock.return_value = response
        self.model.register_user("login", "name", "123", "123")
        req_mock.assert_called_once_with(_user_login="login", _user_name="name", _password1="123", _password2="123")
        self.assertEqual(self.model.info_window, "Пользователь успешно добавлен")
        self.assertEqual(self.model.window, ViewWindows.initial_menu)


if __name__ == "__main__":
    print("\n")
    print(("=" * 20) + "\nTest Client Facade\n" + ("=" * 20))
    unittest.main()