import pytest
import requests


class TestAPI:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    @pytest.mark.parametrize(
        "endpoint, status_code", [
            ("/posts", 200),
            ("/posts/missing_post", 404)
        ]
    )
    def test_get_methods(self, endpoint, status_code):
        response = requests.get(
            url=f"{self.BASE_URL}{endpoint}"
        )
        assert response.status_code == status_code, f"Expected status code {status_code}, but got {response.status_code}."

    @pytest.mark.parametrize(
        "payload, status_code", [
            ({"title": "foo", "body": "bar", "id": 1488}, 201),
            ({}, 201)
        ]
    )
    def test_post_methods(self, payload, status_code):
        response = requests.post(
            url=f"{self.BASE_URL}/posts",
            json=payload
        )
        assert response.status_code == status_code, f"Expected status code {status_code}, but got {response.status_code}."

    @pytest.mark.parametrize(
        "post_id, payload, status_code", [
            (1, {"id": 1, "title": "foo", "body": "bar", "userId": 1}, 200),
            (0, {"id": 0, "title": "foo", "body": "bar", "userId": 1}, 500),
            (1488, {}, 500),
        ]
    )
    def test_put_requests(self, post_id, payload, status_code):
        response = requests.put(
            url=f"{self.BASE_URL}/posts/{post_id}",
            json=payload
        )
        assert response.status_code == status_code, f"Expected status code {status_code}, but got {response.status_code}."

    @pytest.mark.parametrize(
        "post_id, status_code", [
            (1, 200),
            (65, 200),
            ("", 404)
        ]
    )
    def test_delete_requests(self, post_id, status_code):
        response = requests.delete(
            url=f"{self.BASE_URL}/posts/{post_id}"
        )
        assert response.status_code == status_code, f"Expected status code {status_code}, but got {response.status_code}."