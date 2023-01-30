def test_client_handler(test_client):
    username = "luchanos"
    resp = test_client.post(f'/user/{username}')
    assert resp.status_code == 200
    data_from_resp = resp.json()
    assert data_from_resp["msg"] == 'User has been created'
