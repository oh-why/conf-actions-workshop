from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestNotes:

    def test_get_note(self):
        response = client.get("/notes/1")
        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "created_by": "admin",
            "content": "test",
            "tags": []
        }

    def test_get_all_notes(self):
        response = client.get("/notes")
        assert response.status_code == 200
        assert response.json() is not []

    def test_create_note(self):
        response = client.post("/notes", json={"content": "123", "tags": []})
        assert response.status_code == 200
        assert response.json() == {
            "id": 3, "created_by": "default", "content": "123", "tags": []
        }


class TestNotesNegative:

    def test_error_when_get_nonexistent_note(self):
        response = client.get("/notes/9999999")
        assert response.status_code == 200
        assert response.json() == {'error': 'note_id = 9999999 not found'}

    def test_error_when_get_note_invalid_id(self):
        response = client.get("/notes/test")
        assert response.status_code != 200
        assert 'Input should be a valid integer' in response.text

    def test_get_all_notes_empty_when_skip_greater_than_limit(self):
        response = client.get("/notes?skip=10&limit=1")
        assert response.status_code == 200
        assert response.json()["items"] == []

    def test_error_when_create_note_invalid(self):
        response = client.post(url="/notes", json={"tags": "test"})
        assert response.status_code != 200
        assert 'Input should be a valid list' in response.text
