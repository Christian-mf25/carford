

def test_post_owner(test_app,):
    client = test_app.test_client()
    response = client.post(
        "/owners",
        content_type="application/json",
        data={"cnh": "32178965466", "name": "Name Test"}
    )

    assert response.status_code == 201
    assert response.content_type == "application/json"
