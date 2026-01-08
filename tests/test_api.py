def test_create_summary(client, monkeypatch):
    async def mock_generate(text):
        return "Mocked summary"

    monkeypatch.setattr(
        "app.routers.summary.generate_summary",
        mock_generate
    )

    response = client.post(
        "/summaries",
        json={
            "text": "This is a long input text used for testing. " * 5
        }
    )
    # Create
    create_resp = client.post(
        "/summaries",
        json={"text": "Testing GET and DELETE" * 5}
    )
    assert create_resp.status_code == 201

    summary_id = create_resp.json()["id"]

    # Update summary
    update_resp = client.put(
        f"/summaries/{summary_id}",
        json={"summary_text": "Updated summary"}
    )
    assert update_resp.status_code == 200
    assert update_resp.json()["summary_text"] == "Updated summary"

    # Get
    get_resp = client.get(f"/summaries/{summary_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["summary_text"] == "Mocked summary"

    # Delete
    delete_resp = client.delete(f"/summaries/{summary_id}")
    assert delete_resp.status_code == 204

    # Get again (if fail)
    get_again = client.get(f"/summaries/{summary_id}")
    assert get_again.status_code == 404
    assert response.status_code == 201
    assert response.json()["summary_text"] == "Mocked summary"
