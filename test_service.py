import pytest
import Service 
import unittest.mock as mock


@mock.patch("Service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "mocked erfan"
    user_name = Service.get_user_from_db(1)
    assert user_name == "mocked erfan"