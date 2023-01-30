import pytest

from conftest import get_user_from_db_by_id


@pytest.mark.parametrize("username", ["luchanos", "dancherry", "valery"])
def test_create_handler(test_client, username):
    resp = test_client.post(f'/user/{username}')
    assert resp.status_code == 200
    data_from_resp = resp.json()
    assert data_from_resp["msg"] == 'User has been created'
    user_id = data_from_resp["user_id"]
    user_from_database = get_user_from_db_by_id(user_id=user_id, db_connection=test_client.app.state.db)
    assert user_from_database[0] == user_id
    assert user_from_database[1] == username
    assert user_from_database[2] is False
