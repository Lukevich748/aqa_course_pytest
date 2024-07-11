import requests


class TestChuckNorrisJokes:

    def test_get_random_chuck_joke(self):
        response = requests.get(
            url="https://api.chucknorris.io/jokes/random"
        )
        assert response.status_code == 200, f"Status Code Error: Expected 200, but got {response.status_code}"
        assert response.json() != [], "Response body is empty"

    def test_get_jokes_categories(self):
        response = requests.get(
            url="https://api.chucknorris.io/jokes/categories"
        )
        assert response.status_code == 200, f"Status Code Error: Expected 200, but got {response.status_code}"
        assert "sport" in response.json(), "Category 'sport' not found in the response"

    def test_invalid_url(self):
        response = requests.get(
            url="https://api.chucknorris.io/jokes"
        )
        assert response.status_code != 200, f"Status Code Error: Expected non-200, but got {response.status_code}"