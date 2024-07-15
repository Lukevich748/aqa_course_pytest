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
        assert response.status_code == status_code
